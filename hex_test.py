import pytest
from hex import Cell, Board, Coor, Tree
from hex_test_data import POSSIBLE_MOVE_CANDITATES_TEST_DATA, POSSIBLE_ACTIONS_TEST_DATA, FIND_SHADOW_TEST_DATA


@pytest.mark.parametrize("radius, start_cell, expected_result", POSSIBLE_MOVE_CANDITATES_TEST_DATA)
def test_possible_moves_coordinates(radius, start_cell, expected_result):
    board = Board(radius=radius)
    possible_move_coordinates = board.get_move_coordinates(start_cell)
    assert set(possible_move_coordinates) == expected_result


@pytest.mark.parametrize("board_radius, cell_index, cell_coordinates, cell_richness, cell_neighbors, tree,"
                         "expected_result", POSSIBLE_ACTIONS_TEST_DATA)
def test_possible_actions(board_radius, cell_index, cell_coordinates, cell_richness, cell_neighbors, tree,
                          expected_result):
    board = Board(radius=board_radius)
    # def __init__(self, cell_index, coor, richness, neighbors, possible_moves, tree=None):
    cell = Cell(cell_index=cell_index, coor=cell_coordinates, richness=cell_richness, neighbors=cell_neighbors,
                possible_moves=board.get_move_coordinates(cell_coordinates), tree=tree)
    assert set(cell.possible_actions) == expected_result


@pytest.mark.parametrize("cell_to_check, sun_direction, expected_result", FIND_SHADOW_TEST_DATA)
def test_check_if_cell_shadowed(cell_to_check, sun_direction, expected_result):
    board = Board(radius=3)
    board.board[0] = Cell(cell_index=0, coor=Coor(0, 0, 0), richness=0, neighbors=[], possible_moves=[],
                          tree=Tree(cell_index=0, size=2, is_mine=True, is_dormant=True))
    board.board[4] = Cell(cell_index=4, coor=Coor(-1, 1, 0), richness=0, neighbors=[], possible_moves=[],
                          tree=Tree(cell_index=4, size=3, is_mine=True, is_dormant=True))
    board.board[7] = Cell(cell_index=7, coor=Coor(2, -2, 0), richness=0, neighbors=[], possible_moves=[],
                          tree=Tree(cell_index=7, size=3, is_mine=True, is_dormant=True))
    board.board[9] = Cell(cell_index=9, coor=Coor(2, 0, -2), richness=0, neighbors=[], possible_moves=[],
                          tree=Tree(cell_index=9, size=3, is_mine=True, is_dormant=True))
    board.board[11] = Cell(cell_index=11, coor=Coor(0, 2, -2), richness=0, neighbors=[], possible_moves=[],
                           tree=Tree(cell_index=11, size=2, is_mine=True, is_dormant=True))
    board.board[34] = Cell(cell_index=34, coor=Coor(0, -3, 3), richness=0, neighbors=[], possible_moves=[],
                           tree=Tree(cell_index=34, size=1, is_mine=True, is_dormant=True))
    board.board[36] = Cell(cell_index=36, coor=Coor(2, -3, 1), richness=0, neighbors=[], possible_moves=[],
                           tree=Tree(cell_index=36, size=1, is_mine=True, is_dormant=True))

    assert board.is_cell_shadowed(cell_to_check=cell_to_check, sun_direction=sun_direction) == expected_result
