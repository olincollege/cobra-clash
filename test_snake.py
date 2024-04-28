"""
Test the snake class
"""

# pylint: disable=too-many-arguments
import pytest
from snake import Snake

init_cases = [
    # Test snake facing left
    (
        [5, 5],
        "LEFT",
        3,
        [None, None],
        [[[5, 5], [5, 6], [5, 7]], ["LEFT", "LEFT", "LEFT"]],
    ),
    # Test snake up
    (
        [5, 5],
        "UP",
        3,
        [None, None],
        [[[5, 5], [6, 5], [7, 5]], ["UP", "UP", "UP"]],
    ),
    # Test snake down
    (
        [5, 5],
        "DOWN",
        3,
        [None, None],
        [[[5, 5], [4, 5], [3, 5]], ["DOWN", "DOWN", "DOWN"]],
    ),
    # Test can be negative coords
    (
        [-1, 0],
        "DOWN",
        3,
        [None, None],
        [[[-1, 0], [-2, 0], [-3, 0]], ["DOWN", "DOWN", "DOWN"]],
    ),
    # Test can be length 1
    (
        [3, 3],
        "RIGHT",
        1,
        [None, None],
        [[[3, 3]], ["RIGHT"]],
    ),
    # Test define explicitly
    (
        [0, 0],
        "RIGHT",
        1,
        [[[5, 5], [5, 4], [4, 4]], ["DOWN", "DOWN", "RIGHT"]],
        [[[5, 5], [5, 4], [4, 4]], ["DOWN", "DOWN", "RIGHT"]],
    ),
    # Test define explicitly length 1
    (
        [0, 0],
        "RIGHT",
        1,
        [[[0, 0]], ["LEFT"]],
        [[[0, 0]], ["LEFT"]],
    ),
]

move_cases = [
    # Test move right
    (
        ["RIGHT"],
        5,
        5,
        "RIGHT",
        3,
        None,
        None,
        [[5, 6], [5, 5], [5, 4]],
        ["RIGHT", "RIGHT", "RIGHT"],
    ),
    # Test move up
    (
        ["UP"],
        5,
        5,
        "RIGHT",
        3,
        None,
        None,
        [[4, 5], [5, 5], [5, 4]],
        ["UP", "RIGHT", "RIGHT"],
    ),
    # Test move down
    (
        ["DOWN"],
        5,
        5,
        "RIGHT",
        3,
        None,
        None,
        [[6, 5], [5, 5], [5, 4]],
        ["DOWN", "RIGHT", "RIGHT"],
    ),
    # Test move left
    (
        ["LEFT"],
        5,
        5,
        "LEFT",
        3,
        None,
        None,
        [[5, 4], [5, 5], [5, 6]],
        ["LEFT", "LEFT", "LEFT"],
    ),
    # Test move left if facing right will move to right and update direction
    (
        ["LEFT"],
        5,
        5,
        "RIGHT",
        3,
        None,
        None,
        [[5, 6], [5, 5], [5, 4]],
        ["RIGHT", "RIGHT", "RIGHT"],
    ),
    # Test multiple moves in different directions
    (
        ["UP", "LEFT"],
        5,
        5,
        "RIGHT",
        3,
        None,
        None,
        [[4, 4], [4, 5], [5, 5]],
        ["LEFT", "UP", "RIGHT"],
    ),
    # Test can overlap with self, so model logic can find it died
    (
        ["UP", "LEFT", "DOWN"],
        5,
        5,
        "RIGHT",
        5,
        None,
        None,
        [[5, 4], [4, 4], [4, 5], [5, 5], [5, 4]],
        ["DOWN", "LEFT", "UP", "RIGHT", "RIGHT"],
    ),
    # Test can move out of bounds, so model logic can find it died
    (
        ["LEFT"],
        3,
        0,
        "LEFT",
        3,
        None,
        None,
        [[3, -1], [3, 0], [3, 1]],
        ["LEFT", "LEFT", "LEFT"],
    ),
    # Test snake of length 1 moves correctly
    (
        ["UP"],
        5,
        5,
        "RIGHT",
        1,
        None,
        None,
        [[4, 5]],
        ["UP"],
    ),
]

grow_cases = [
    # Test grow left
    (
        5,
        5,
        "RIGHT",
        3,
        None,
        None,
        [[5, 5], [5, 4], [5, 3], [5, 2]],
        ["RIGHT", "RIGHT", "RIGHT", "RIGHT"],
    ),
    # Test grow up
    (
        5,
        5,
        "DOWN",
        3,
        None,
        None,
        [[5, 5], [4, 5], [3, 5], [2, 5]],
        ["DOWN", "DOWN", "DOWN", "DOWN"],
    ),
    # Test grow right
    (
        5,
        5,
        "LEFT",
        3,
        None,
        None,
        [[5, 5], [5, 6], [5, 7], [5, 8]],
        ["LEFT", "LEFT", "LEFT", "LEFT"],
    ),
    # Test grow down
    (
        5,
        5,
        "UP",
        3,
        None,
        None,
        [[5, 5], [6, 5], [7, 5], [8, 5]],
        ["UP", "UP", "UP", "UP"],
    ),
    # Test grow with different directions in snake
    (
        None,
        None,
        None,
        None,
        [[5, 5], [6, 5], [6, 6], [7, 6]],
        ["UP", "LEFT", "UP", "LEFT"],
        [[5, 5], [6, 5], [6, 6], [7, 6], [7, 7]],
        ["UP", "LEFT", "UP", "LEFT", "LEFT"],
    ),
    # Test grow snake length 1
    (
        5,
        5,
        "UP",
        1,
        None,
        None,
        [[5, 5], [6, 5]],
        ["UP", "UP"],
    ),
    # Test snake can grow into self
    (
        None,
        None,
        None,
        None,
        [[5, 7], [5, 6], [5, 5], [4, 5], [4, 6]],
        ["RIGHT", "RIGHT", "DOWN", "LEFT", "UP"],
        [[5, 7], [5, 6], [5, 5], [4, 5], [4, 6], [5, 6]],
        ["RIGHT", "RIGHT", "DOWN", "LEFT", "UP", "UP"],
    ),
]


@pytest.mark.parametrize(
    "head_location, direction, length, "
    + "input_locations_and_directions, output_locations_and_directions",
    init_cases,
)
def test_init(
    head_location,
    direction,
    length,
    input_locations_and_directions,
    output_locations_and_directions,
):
    """
    Test that it initializes correctly

    Parameters:
        head_location: list of two integers for row and col of head
        direction: String representing direction the snake is facing
        length: Integer greater than 0 representing the length of the snake
        input_locations_and_directions: List of lists with the first index
            being a list of lists of int with starting coordinates of segments
            and the second a list of strings of starting directions of segments
        output_locations_and_directions: List of lists with the first index
            being a list of lists of int with ending coordinates of segments
            and the second a list of strings of ending directions of segments
    """
    snake_one = Snake(
        head_location,
        direction,
        length,
        locations_and_directions=input_locations_and_directions,
    )

    assert snake_one.locations == output_locations_and_directions[0]
    assert snake_one.directions == output_locations_and_directions[1]


@pytest.mark.parametrize(
    "move_directions, head_row, head_col, direction, length, "
    + "locations, directions, output_locations, output_directions",
    move_cases,
)
def test_move(
    move_directions,
    head_row,
    head_col,
    direction,
    length,
    locations,
    directions,
    output_locations,
    output_directions,
):
    """
    Test that the snake moves correctly

    Parameters:
        move_directions: List of strings representing moves
        head_row: Integer representing the row location of snake head
        head_col: Integer representing the col location of snake head
        direction: String representing direction the snake is facing
        length: Integer greater than 0 representing the length of the snake
        locations: List of lists int with locations of snake or None
        directions: List of strings of directions of segments or None
        output_locations: List of lists of int with final locations of snake
        output_directions: List of strings of directions of final location
    """
    snake_one = Snake(
        [head_row, head_col],
        direction,
        length,
        locations_and_directions=[locations, directions],
    )

    for move in move_directions:
        snake_one.move(move)

    assert snake_one.locations == output_locations
    assert snake_one.directions == output_directions


@pytest.mark.parametrize(
    "head_row, head_col, direction, length, "
    + "locations, directions, output_locations, output_directions",
    grow_cases,
)
def test_grow(
    head_row,
    head_col,
    direction,
    length,
    locations,
    directions,
    output_locations,
    output_directions,
):
    """
    Test that the snake grows correctly

    Parameters:
        move_directions: List of strings representing moves
        head_row: Integer representing the row location of snake head
        head_col: Integer representing the col location of snake head
        direction: String representing direction the snake is facing
        length: Integer greater than 0 representing the length of the snake
        locations: List of lists int with locations of snake or None
        directions: List of strings of directions of segments or None
        output_locations: List of lists of int with final locations of snake
        output_directions: List of strings of directions of final location
    """
    snake_one = Snake(
        [head_row, head_col],
        direction,
        length,
        locations_and_directions=[locations, directions],
    )

    snake_one.grow()

    assert snake_one.locations == output_locations
    assert snake_one.directions == output_directions
