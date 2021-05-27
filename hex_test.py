import pytest
from hex import Cell, Board, Coor
from hex_test_data import POSSIBLE_MOVE_CANDITATES_TEST_DATA, POSSIBLE_MOVES_TEST_DATA


@pytest.mark.parametrize("radius, start_cell, expected_result", POSSIBLE_MOVE_CANDITATES_TEST_DATA)
def test_possible_moves_coordinates(radius, start_cell, expected_result):
    board = Board(radius=radius)
    possible_move_coordinates = board.get_move_coordinates(start_cell)
    print(len(possible_move_coordinates))
    assert set(possible_move_coordinates) == expected_result


@pytest.mark.parametrize("board_radius, cell_index, cell_coordinates, cell_richness, cell_neighbors, tree,"
                         "expected_result", POSSIBLE_MOVES_TEST_DATA)
def test_possible_actions(board_radius, cell_index, cell_coordinates, cell_richness, cell_neighbors, tree,
                          expected_result):
    board = Board(radius=board_radius)
    # def __init__(self, cell_index, coor, richness, neighbors, possible_moves, tree=None):
    cell = Cell(cell_index=cell_index, coor=cell_coordinates, richness=cell_richness, neighbors=cell_neighbors,
                possible_moves=board.get_move_coordinates(cell_coordinates), tree=tree)
    assert cell.possible_actions == expected_result
