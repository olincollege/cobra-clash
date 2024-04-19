"""
Test the snake class
"""

import pytest
from snake import Snake

init_cases = [
    # Test snake facing right
    (
        5,
        5,
        "RIGHT",
        3,
        None,
        None,
        [[5, 5], [5, 4], [5, 3]],
        ["RIGHT", "RIGHT", "RIGHT"],
    ),
    # Test snake facing left
    (
        5,
        5,
        "LEFT",
        3,
        None,
        None,
        [[5, 5], [5, 6], [5, 7]],
        ["LEFT", "LEFT", "LEFT"],
    ),
    # Test snake up
    (5, 5, "UP", 3, None, None, [[5, 5], [6, 5], [7, 5]], ["UP", "UP", "UP"]),
    # Test snake down
    (
        5,
        5,
        "DOWN",
        3,
        None,
        None,
        [[5, 5], [4, 5], [3, 5]],
        ["DOWN", "DOWN", "DOWN"],
    ),
    # Test can be negative coords
    (
        -1,
        -0,
        "DOWN",
        3,
        None,
        None,
        [[-1, 0], [-2, 0], [-3, 0]],
        ["DOWN", "DOWN", "DOWN"],
    ),
    # Test can be length 1
    (3, 3, "RIGHT", 1, None, None, [[3, 3]], ["RIGHT"]),
    # Test define explicitly
    (
        0,
        0,
        "RIGHT",
        1,
        [[5, 5], [5, 4], [4, 4]],
        ["DOWN", "DOWN", "RIGHT"],
        [[5, 5], [5, 4], [4, 4]],
        ["DOWN", "DOWN", "RIGHT"],
    ),
    # test define explicitly length 1
    (0, 0, "RIGHT", 1, [[0, 0]], ["LEFT"], [[0, 0]], ["LEFT"]),
]


@pytest.mark.parametrize(
    "head_row, head_col, direction, length, "
    + "locations, directions, output_locations, output_directions",
    init_cases,
)
def test_init(
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
    Test that it initializes correctly

    Parameters:
        head_row: Integer representing the row location of snake head
        head_col: Integer representing the col location of snake head
        direction: String representing direction the snake is facing
        length: Integer greater than 0 representing the length of the snake
        locations: List of lists int with locations of snake or None
        directions: List of strings of directions of segments or None
        output_locations: List of lists of int with output locations of snake
        output_directions: List of strings of directions of segments for output
    """
    snake_one = Snake(
        head_row,
        head_col,
        direction,
        length,
        locations=locations,
        directions=directions,
    )

    assert snake_one.locations == output_locations
    assert snake_one.directions == output_directions


# @pytest.mark.parametrize
