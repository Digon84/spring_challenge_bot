from hex import Coor, Tree, ActionType, Action

# radius, start_cell, expected_result
POSSIBLE_MOVE_CANDITATES_TEST_DATA = [(0, Coor(0, 0, 0), {Coor(0, 0, 0)}),
                                      (0, Coor(-2, 3, -1), {Coor(-2, 3, -1)}),
                                      (1, Coor(0, 0, 0), {Coor(0, 0, 0), Coor(1, -1, 0), Coor(1, 0, -1), Coor(0, 1, -1),
                                                          Coor(-1, 1, 0), Coor(-1, 0, 1), Coor(0, -1, 1)}),
                                      (3, Coor(0, 0, 0), {Coor(0, 0, 0),
                                                          Coor(1, -1, 0), Coor(2, -2, 0), Coor(3, -3, 0),
                                                          Coor(1, 0, -1), Coor(2, 0, -2), Coor(3, 0, -3),
                                                          Coor(0, 1, -1), Coor(0, 2, -2), Coor(0, 3, -3),
                                                          Coor(-1, 1, 0), Coor(-2, 2, 0), Coor(-3, 3, 0),
                                                          Coor(-1, 0, 1), Coor(-2, 0, 2), Coor(-3, 0, 3),
                                                          Coor(0, -1, 1), Coor(0, -2, 2), Coor(0, -3, 3)})]
# class Tree:
#     def __init__(self, cell_index, size, is_mine, is_dormant):
#         self.cell_index = cell_index
#         self.size = size
#         self.is_mine = is_mine
#         self.is_dormant = is_dormant
# board_radius, cell_index, cell_coordinates, cell_richness, cell_neighbors, tree, expected_result
POSSIBLE_MOVES_TEST_DATA = [(3, 0, Coor(0, 0, 0), 0, [], Tree(0, 0, True, False),
                             [Action(type=ActionType.GROW, target_cell_id=0)])]
