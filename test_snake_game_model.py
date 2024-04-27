"""
Test snake game model class
"""

import pytest
from snake_game_model import SnakeGameModel

init_and_setup_cases = [
    # Test default initializations
    (
        None,
        None,
        None,
        None,
        [[9, 4], [9, 3], [9, 2], [9, 1]],
        ["RIGHT", "RIGHT", "RIGHT", "RIGHT"],
        [[9, 14], [9, 15], [9, 16], [9, 17]],
        ["LEFT", "LEFT", "LEFT", "LEFT"],
    ),
    # Test snake one precise initialization
    (
        [[5, 4], [5, 3], [4, 3]],
        ["RIGHT", "RIGHT", "DOWN"],
        None,
        None,
        [[5, 4], [5, 3], [4, 3]],
        ["RIGHT", "RIGHT", "DOWN"],
        [[9, 14], [9, 15], [9, 16], [9, 17]],
        ["LEFT", "LEFT", "LEFT", "LEFT"],
    ),
    # Test snake two precise initialization
    (
        None,
        None,
        [[4, 12], [4, 13], [5, 13]],
        ["LEFT", "LEFT", "UP"],
        [[9, 4], [9, 3], [9, 2], [9, 1]],
        ["RIGHT", "RIGHT", "RIGHT", "RIGHT"],
        [[4, 12], [4, 13], [5, 13]],
        ["LEFT", "LEFT", "UP"],
    ),
    # Test both with precise initialization
    (
        [[5, 4], [5, 3], [4, 3]],
        ["RIGHT", "RIGHT", "DOWN"],
        [[4, 12], [4, 13], [5, 13]],
        ["LEFT", "LEFT", "UP"],
        [[5, 4], [5, 3], [4, 3]],
        ["RIGHT", "RIGHT", "DOWN"],
        [[4, 12], [4, 13], [5, 13]],
        ["LEFT", "LEFT", "UP"],
    ),
]

collision_cases = [
    # Test no collision with default initialization
    (
        None,
        None,
        None,
        None,
        False,
        False,
    ),
    # Test both snakes heads collide
    (
        [[5, 4], [5, 3], [5, 2]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[5, 4], [5, 5], [5, 6]],
        ["LEFT", "LEFT", "LEFT"],
        True,
        True,
    ),
    # Test snake two collide snake one
    (
        [[5, 4], [5, 3], [5, 2]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[5, 3], [6, 3], [7, 3]],
        ["UP", "UP", "UP"],
        False,
        True,
    ),
    # Test snake one collide snake two
    (
        [[5, 3], [6, 3], [7, 3]],
        ["UP", "UP", "UP"],
        [[5, 4], [5, 3], [5, 2]],
        ["RIGHT", "RIGHT", "RIGHT"],
        True,
        False,
    ),
    # Test snake one collide with bottom wall
    (
        [[19, 5], [18, 5], [17, 5]],
        ["DOWN", "DOWN", "DOWN"],
        None,
        None,
        True,
        False,
    ),
    # Test snake two collide with left wall and snake one right wall
    (
        [[9, 19], [9, 18], [9, 17]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[9, -1], [9, 0], [9, 1]],
        ["LEFT", "LEFT", "LEFT"],
        True,
        True,
    ),
    # Test snake one collide with top wall and snake two snake one
    (
        [[-1, 5], [0, 5], [1, 5]],
        ["UP", "UP", "UP"],
        [[0, 5], [0, 1], [0, 2]],
        ["LEFT", "LEFT", "LEFT"],
        True,
        True,
    ),
]


@pytest.mark.parametrize(
    "snake_one_locations, snake_one_directions, snake_two_locations, "
    + "snake_two_directions, snake_one_output_locations, "
    + "snake_one_output_directions, snake_two_output_locations, "
    + "snake_two_output_directions",
    init_and_setup_cases,
)
def test_init(
    snake_one_locations,
    snake_one_directions,
    snake_two_locations,
    snake_two_directions,
    snake_one_output_locations,
    snake_one_output_directions,
    snake_two_output_locations,
    snake_two_output_directions,
):
    """
    Check that the model initializes correctly

    Parameters:
    snake_one_locations: list of lists initial integer coordinates for segments
    snake_one_directions: list of strings with initial directions for segments
    snake_two_locations: list of lists with initial integer coordinates for
    segments
    snake_two_directions: list of strings with initial directions for segments
    snake_one_output_locations: list of lists final integer coordinates for
    segments
    snake_one_output_directions: list of strings with final directions for
    segments
    snake_two_output_locations: list of lists final integer coordinates for
    segments
    snake_two_output_directions: list of strings with final directions for
    segments

    """
    game = SnakeGameModel(
        snake_one_locations=snake_one_locations,
        snake_two_locations=snake_two_locations,
        snake_one_directions=snake_one_directions,
        snake_two_directions=snake_two_directions,
    )

    assert game.snake_one.locations == snake_one_output_locations
    assert game.snake_two.locations == snake_two_output_locations
    assert game.snake_one.directions == snake_one_output_directions
    assert game.snake_two.directions == snake_two_output_directions
    assert game.apples == [[9, 9]]
    assert game.game_state == 1


def test_reset():
    """
    Check that it resets the attributes to default state
    """
    game = SnakeGameModel()
    game.move_snakes("RIGHT", "LEFT")
    game.reset()

    assert game.snake_one.locations == [[9, 4], [9, 3], [9, 2], [9, 1]]
    assert game.snake_two.locations == [[9, 14], [9, 15], [9, 16], [9, 17]]
    assert game.snake_one.directions == ["RIGHT", "RIGHT", "RIGHT", "RIGHT"]
    assert game.snake_two.directions == ["LEFT", "LEFT", "LEFT", "LEFT"]
    assert game.apples == [[9, 9]]
    assert game.game_state == 1


@pytest.mark.parametrize(
    "snake_one_locations, snake_one_directions, snake_two_locations, "
    + "snake_two_directions, snake_one_collision, snake_two_collision",
    collision_cases,
)
def test_collision(
    snake_one_locations,
    snake_one_directions,
    snake_two_locations,
    snake_two_directions,
    snake_one_collision,
    snake_two_collision,
):
    """
    Check that the collision logic is correct

    Parameters:
    snake_one_locations: list of lists initial integer coordinates for segments
    snake_one_directions: list of strings with initial directions for segments
    snake_two_locations: list of lists with initial integer coordinates for
    segments
    snake_two_directions: list of strings with initial directions for segments
    snake_one_collision: boolean of if snake one is colliding
    snake_two_collision: boolean of if snake one is colliding
    """
    game = SnakeGameModel(
        snake_one_locations=snake_one_locations,
        snake_two_locations=snake_two_locations,
        snake_one_directions=snake_one_directions,
        snake_two_directions=snake_two_directions,
    )

    snake_one, snake_two = game.collision()

    assert snake_one == snake_one_collision
    assert snake_two == snake_two_collision
