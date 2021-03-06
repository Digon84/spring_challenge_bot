import attr
import math
from enum import Enum


@attr.s(frozen=True)
class Coor:
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()

    def calculate_distance(self, other):
        x = math.fabs(math.fabs(self.x) - math.fabs(other.x))
        y = math.fabs(math.fabs(self.y) - math.fabs(other.y))
        z = math.fabs(math.fabs(self.z) - math.fabs(other.z))
        return Coor(x, y, z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Coor(x, y, z)

    def __mul__(self, value):
        x = self.x * value
        y = self.y * value
        z = self.z * value
        return Coor(x, y, z)

    def __str__(self):
        return f'({self.x} {self.y} {self.z})'


class ActionType(Enum):
    WAIT = "WAIT"
    SEED = "SEED"
    GROW = "GROW"
    COMPLETE = "COMPLETE"


class Action:
    def __init__(self, type, target_cell_id=None, origin_cell_id=None):
        self.type = type
        self.target_cell_id = target_cell_id
        self.origin_cell_id = origin_cell_id

    def __str__(self):
        if self.type == ActionType.WAIT:
            return 'WAIT'
        elif self.type == ActionType.SEED:
            return f'SEED {self.origin_cell_id} {self.target_cell_id}'
        else:
            return f'{self.type.name} {self.target_cell_id}'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __hash__(self):
        return hash(self.__str__())

    @staticmethod
    def parse(action_string):
        split = action_string.split(' ')
        if split[0] == ActionType.WAIT.name:
            return Action(ActionType.WAIT)
        if split[0] == ActionType.SEED.name:
            return Action(ActionType.SEED, int(split[2]), int(split[1]))
        if split[0] == ActionType.GROW.name:
            return Action(ActionType.GROW, int(split[1]))
        if split[0] == ActionType.COMPLETE.name:
            return Action(ActionType.COMPLETE, int(split[1]))


class Tree:
    def __init__(self, cell_index, size, is_mine, is_dormant):
        self.cell_index = cell_index
        self.size = size
        self.is_mine = is_mine
        self.is_dormant = is_dormant


class Cell:
    def __init__(self, cell_index, coor, richness, neighbors, possible_moves, tree=None):
        self.cell_index = cell_index
        self.coor = coor
        self.richness = richness
        self.neighbors = neighbors
        self.possible_actions = None
        self.radius = -1
        self.possible_moves = possible_moves
        self.tree = tree
        if tree is None:
            self.possible_actions = self.get_possible_actions()

    def __str__(self):
        return f'cell_index: {self.cell_index}\n \
                 coor: {self.coor}\n \
                 richness: {self.richness}\n \
                 neighbors: {self.neighbors}\n \
                 possible_moves: {self.possible_moves}\n \
                 possible_actions: {self.possible_actions}\n'

    @property
    def tree(self):
        return self.__tree

    @tree.setter
    def tree(self, tree: Tree):
        if tree is not None:
            self.__tree = tree
            self.radius = tree.size
            self.possible_actions = self.get_possible_actions()
        else:
            self.__tree = tree
            self.radius = -1
            self.possible_actions = self.get_possible_actions()

    def get_possible_actions(self):
        possible_actions = [Action(ActionType.WAIT)]
        if self.radius == -1:
            pass
        elif self.tree.is_dormant:
            pass
        elif not self.tree.is_mine:
            pass
        elif self.radius == 0:
            possible_actions.append(Action(ActionType.GROW, self.cell_index))
        else:
            if self.radius == 3:
                possible_actions.append(Action(ActionType.COMPLETE, self.cell_index))
            else:
                possible_actions.append(Action(ActionType.GROW, self.cell_index))
            for possible_move in self.possible_moves:
                temp = self.coor.calculate_distance(possible_move)
                if temp.x <= self.radius and temp.y <= self.radius and temp.z <= self.radius and \
                        Board.COORDINATES_TO_INDEX[possible_move] != self.cell_index:
                    possible_actions.append(Action(ActionType.SEED, Board.COORDINATES_TO_INDEX[possible_move],
                                                   self.cell_index))
        return possible_actions


class Board:
    DIRECTIONS = [Coor(1, -1, 0), Coor(1, 0, -1), Coor(0, 1, -1),
                  Coor(-1, 1, 0), Coor(-1, 0, 1), Coor(0, -1, 1)]
    INDEX_TO_COORDINATES = {0: Coor(0, 0, 0), 1: Coor(1, -1, 0), 2: Coor(1, 0, -1), 3: Coor(0, 1, -1),
                            4: Coor(-1, 1, 0), 5: Coor(-1, 0, 1), 6: Coor(0, -1, 1), 7: Coor(2, -2, 0),
                            8: Coor(2, -1, -1), 9: Coor(2, 0, -2), 10: Coor(1, 1, -2), 11: Coor(0, 2, -2),
                            12: Coor(-1, 2, -1), 13: Coor(-2, 2, 0), 14: Coor(-2, 1, 1), 15: Coor(-2, 0, 2),
                            16: Coor(-1, -1, 2), 17: Coor(0, -2, 2), 18: Coor(1, -2, 1), 19: Coor(3, -3, 0),
                            20: Coor(3, -2, -1), 21: Coor(3, -1, -2), 22: Coor(3, 0, -3), 23: Coor(2, 1, -3),
                            24: Coor(1, 2, -3), 25: Coor(0, 3, -3), 26: Coor(-1, 3, -2), 27: Coor(-2, 3, -1),
                            28: Coor(-3, 3, 0), 29: Coor(-3, 2, 1), 30: Coor(-3, 1, 2), 31: Coor(-3, 0, 3),
                            32: Coor(-2, -1, 3), 33: Coor(-1, -2, 3), 34: Coor(0, -3, 3), 35: Coor(1, -3, 2),
                            36: Coor(2, -3, 1)}
    COORDINATES_TO_INDEX = {item: key for key, item in INDEX_TO_COORDINATES.items()}

    def __init__(self, radius):
        self.board = {}
        self.radius = radius
        self.player_growing_seeding_cost = {0: 0, 1: 1, 2: 3, 3: 7}
        self.opponent_growing_seeding_cost = {0: 0, 1: 1, 2: 3, 3: 7}
        self.opponent_cells = []
        self.player_cells = []

    def get_move_coordinates(self, origin_cell_coor):
        move_coordinates = [origin_cell_coor]
        for i in range(1, self.radius + 1):
            move_coordinates.extend([origin_cell_coor + mc * i for mc in self.DIRECTIONS
                                     if str(origin_cell_coor + mc * i) in
                                     [str(key) for key in self.COORDINATES_TO_INDEX.keys()]])
        return move_coordinates

    def is_cell_shadowed(self, cell_to_check, sun_direction):
        opposite_direction = {0: 3, 1: 4, 2: 5, 3: 0, 4: 1, 5: 2}[sun_direction]
        cell_tree_size = self.board[cell_to_check].tree.size
        cell_coor = self.board[cell_to_check].coor
        for distance in range(1, 4):
            possible_shadowing = self.COORDINATES_TO_INDEX[cell_coor + self.DIRECTIONS[opposite_direction] * distance]
            cell = self.board.get(possible_shadowing, None)
            if cell:
                if self.board[possible_shadowing].tree.size >= distance and \
                        self.board[possible_shadowing].tree.size >= cell_tree_size:
                    return True
        return False

    def create_board(self, cells_amount):
        for i in cells_amount:
            self.board[i] = None

    def add_cell(self, cell):
        self.board[cell.cell_index] = cell

    def place_tree(self, tree):
        self.board[tree.cell_index].tree = tree
        if tree.is_mine:
            self.player_cells.append(tree.cell_index)
            self.player_growing_seeding_cost[tree.size] = self.player_growing_seeding_cost[tree.size] + 1
        else:
            self.opponent_cells.append(tree.cell_index)
            self.opponent_growing_seeding_cost[tree.size] += 1

    def complete_tree(self, index):
        tree = self.board[index].tree
        if tree.is_mine:
            del self.player_cells[index]
            self.player_growing_seeding_cost[tree.size] -= 1
        else:
            del self.opponent_cells[index]
            self.opponent_growing_seeding_cost[tree.size] -= 1
        self.board[index].tree = None


class Game:
    RADIUS = 3
    DAYS_TO_PLAY = 24

    def __init__(self):
        self.board = Board(radius=self.RADIUS)

    def evaluate_board(self, opponent=False):
        pass

    def minimax(self, state, depth, maximizingPlayer):
        pass

