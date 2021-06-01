from hex import Coor, Tree, ActionType, Action, Cell

# radius, start_cell, expected_result
POSSIBLE_MOVE_CANDITATES_TEST_DATA = [
    (0, Coor(0, 0, 0), {Coor(0, 0, 0)}),
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

# board_radius, cell_index, cell_coordinates, cell_richness, cell_neighbors, tree, expected_result
POSSIBLE_ACTIONS_TEST_DATA = [
    (3, 0, Coor(0, 0, 0), 0, [], None,
     {Action(type=ActionType.WAIT)}),
    (3, 0, Coor(0, 0, 0), 0, [], Tree(cell_index=0, size=0, is_mine=True, is_dormant=False),
     {Action(type=ActionType.GROW, target_cell_id=0), Action(type=ActionType.WAIT)}),
    (3, 0, Coor(0, 0, 0), 0, [], Tree(cell_index=0, size=1, is_mine=True, is_dormant=False),
     {Action(type=ActionType.GROW, target_cell_id=0), Action(type=ActionType.WAIT),
      Action(type=ActionType.SEED, target_cell_id=1, origin_cell_id=0),
      Action(type=ActionType.SEED, target_cell_id=2, origin_cell_id=0),
      Action(type=ActionType.SEED, target_cell_id=3, origin_cell_id=0),
      Action(type=ActionType.SEED, target_cell_id=4, origin_cell_id=0),
      Action(type=ActionType.SEED, target_cell_id=5, origin_cell_id=0),
      Action(type=ActionType.SEED, target_cell_id=6, origin_cell_id=0)}),
    (3, 34, Coor(0, -3, 3), 0, [], Tree(cell_index=34, size=3, is_mine=True, is_dormant=False),
     {Action(type=ActionType.WAIT), Action(type=ActionType.COMPLETE, target_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=33, origin_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=32, origin_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=31, origin_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=17, origin_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=6, origin_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=0, origin_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=35, origin_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=36, origin_cell_id=34),
      Action(type=ActionType.SEED, target_cell_id=19, origin_cell_id=34)}),
    (3, 18, Coor(1, -2, 1), 0, [], Tree(cell_index=18, size=3, is_mine=True, is_dormant=False),
     {Action(type=ActionType.WAIT), Action(type=ActionType.COMPLETE, target_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=7, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=20, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=17, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=33, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=35, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=36, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=6, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=5, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=14, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=1, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=2, origin_cell_id=18),
      Action(type=ActionType.SEED, target_cell_id=10, origin_cell_id=18)}),
    (3, 0, Coor(0, 0, 0), 0, [], Tree(cell_index=0, size=1, is_mine=False, is_dormant=False),
     {Action(ActionType.WAIT)}),
    (3, 0, Coor(0, 0, 0), 0, [], Tree(cell_index=0, size=3, is_mine=True, is_dormant=True),
     {Action(ActionType.WAIT)}),
]

# cell_to_check, sun_direction, expected_result
FIND_SHADOW_TEST_DATA = [
    (0, 3, True),   # size 3 (cell 7) shadows size 2 (cell 0)
    (4, 3, True),   # size 2 (cell 0) doesn't shadow 3 (cell 4), but 3 (cell 7) does - border
    (7, 0, True),   # size 3 (cell 4) shadows size 3 (cell 7) - border
    (11, 2, True),  # size 2 (cell 0) shadows size 2 (cell 11) - border
    (9, 0, False),  # size 2 (cell 11) does not shadow size 3 (cell 9), even if it reaches the cell
    (34, 4, False)  # size 1 (cell 36) does not shadow size 1 (cell 34) - no reach
]

# tree, expected_player_cells, expected_growing_seeding_cost
PLACE_TREE_PLAYER = [
    (Tree(cell_index=4, size=0, is_mine=True, is_dormant=False), [4], {0: 1, 1: 1, 2: 3, 3: 7}),
    (Tree(cell_index=9, size=3, is_mine=True, is_dormant=False), [9], {0: 0, 1: 1, 2: 3, 3: 8}),
    (Tree(cell_index=34, size=1, is_mine=True, is_dormant=False), [34], {0: 0, 1: 2, 2: 3, 3: 7})
]

# tree, expected_player_cells, expected_growing_seeding_cost
PLACE_TREE_OPPONENT = [
    (Tree(cell_index=4, size=0, is_mine=False, is_dormant=False), [4], {0: 1, 1: 1, 2: 3, 3: 7}),
    (Tree(cell_index=9, size=3, is_mine=False, is_dormant=False), [9], {0: 0, 1: 1, 2: 3, 3: 8}),
    (Tree(cell_index=34, size=1, is_mine=False, is_dormant=False), [34], {0: 0, 1: 2, 2: 3, 3: 7})
]