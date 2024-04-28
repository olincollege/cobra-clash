"""
Test snake game model class
"""

# pylint: disable=too-many-arguments
import pytest
from snake_game_model import SnakeGameModel

init_and_setup_cases = [
    # Test default initializations
    (
        None,
        None,
        None,
        None,
        [[8, 4], [8, 3], [8, 2], [8, 1]],
        ["RIGHT", "RIGHT", "RIGHT", "RIGHT"],
        [[10, 14], [10, 15], [10, 16], [10, 17]],
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
        [[10, 14], [10, 15], [10, 16], [10, 17]],
        ["LEFT", "LEFT", "LEFT", "LEFT"],
    ),
    # Test snake two precise initialization
    (
        None,
        None,
        [[4, 12], [4, 13], [5, 13]],
        ["LEFT", "LEFT", "UP"],
        [[8, 4], [8, 3], [8, 2], [8, 1]],
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

move_cases = [
    # Test move initializations
    (
        None,
        None,
        None,
        None,
        [[8, 5], [8, 4], [8, 3], [8, 2]],
        ["RIGHT", "RIGHT", "RIGHT", "RIGHT"],
        [[10, 13], [10, 14], [10, 15], [10, 16]],
        ["LEFT", "LEFT", "LEFT", "LEFT"],
        [("RIGHT", "LEFT")],
    ),
    # Test moving both snakes straight without any direction change
    (
        [[8, 5], [8, 4], [8, 3]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[10, 12], [10, 13], [10, 14]],
        ["LEFT", "LEFT", "LEFT"],
        [[8, 6], [8, 5], [8, 4]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[10, 11], [10, 12], [10, 13]],
        ["LEFT", "LEFT", "LEFT"],
        [("RIGHT", "LEFT")],
    ),
    # Test turning the snake while moving, snake one turns up,
    # snake two turns down
    (
        [[8, 4], [8, 5], [8, 6]],
        ["LEFT", "LEFT", "LEFT"],
        [[12, 8], [11, 8], [10, 8]],
        ["UP", "UP", "UP"],
        [[5, 4], [6, 4], [7, 4]],
        ["UP", "UP", "UP"],
        [[12, 11], [12, 10], [12, 9]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [("UP", "RIGHT"), ("UP", "RIGHT"), ("UP", "RIGHT")],
    ),
    # Test opposite directions: both snakes move towards each other
    (
        [[10, 7], [10, 8], [10, 9]],
        ["LEFT", "LEFT", "LEFT"],
        [[10, 13], [10, 12], [10, 11]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[10, 6], [10, 7], [10, 8]],
        ["LEFT", "LEFT", "LEFT"],
        [[10, 14], [10, 13], [10, 12]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [("LEFT", "RIGHT")],
    ),
    # Test coords can go negative to indicate out of bounds
    (
        [[0, 5], [1, 5], [2, 5]],
        ["UP", "UP", "UP"],
        [[10, 10], [10, 11], [10, 12]],
        ["LEFT", "LEFT", "LEFT"],
        [[-1, 5], [0, 5], [1, 5]],
        ["UP", "UP", "UP"],
        [[10, 9], [10, 10], [10, 11]],
        ["LEFT", "LEFT", "LEFT"],
        [("UP", "LEFT")],
    ),
]

snake_won_cases = [
    # Test no player winning with default initialization
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
    # Test snake two collides with snake one
    (
        [[5, 4], [5, 3], [5, 2]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[5, 3], [6, 3], [7, 3]],
        ["UP", "UP", "UP"],
        True,
        False,
    ),
    # Test snake one collides with snake two
    (
        [[5, 3], [6, 3], [7, 3]],
        ["UP", "UP", "UP"],
        [[5, 4], [5, 3], [5, 2]],
        ["RIGHT", "RIGHT", "RIGHT"],
        False,
        True,
    ),
    # Test snake one collides with bottom wall
    (
        [[19, 5], [18, 5], [17, 5]],
        ["DOWN", "DOWN", "DOWN"],
        None,
        None,
        False,
        True,
    ),
    # Test snake two collides with left wall and snake one with right wall
    (
        [[9, 19], [9, 18], [9, 17]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[9, -1], [9, 0], [9, 1]],
        ["LEFT", "LEFT", "LEFT"],
        True,
        True,
    ),
    # Test snake one collides with top wall and snake two with snake one
    (
        [[-1, 5], [0, 5], [1, 5]],
        ["UP", "UP", "UP"],
        [[0, 5], [0, 1], [0, 2]],
        ["LEFT", "LEFT", "LEFT"],
        True,
        True,
    ),
    # Neither snake collides with anything
    (
        [[5, 5], [5, 6], [5, 7]],
        ["RIGHT", "RIGHT", "RIGHT"],
        [[15, 5], [15, 6], [15, 7]],
        ["LEFT", "LEFT", "LEFT"],
        False,
        False,
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

    assert game.snake_one.locations == [[8, 4], [8, 3], [8, 2], [8, 1]]
    assert game.snake_two.locations == [[10, 14], [10, 15], [10, 16], [10, 17]]
    assert game.snake_one.directions == ["RIGHT", "RIGHT", "RIGHT", "RIGHT"]
    assert game.snake_two.directions == ["LEFT", "LEFT", "LEFT", "LEFT"]
    assert game.apples == [[9, 9]]
    assert game.game_state == 1


@pytest.mark.parametrize(
    "snake_one_locations, snake_one_directions, snake_two_locations, "
    + "snake_two_directions, snake_one_output_locations, "
    + "snake_one_output_directions, snake_two_output_locations, "
    + "snake_two_output_directions, snake_moves",
    move_cases,
)
def test_move_snakes(
    snake_one_locations,
    snake_one_directions,
    snake_two_locations,
    snake_two_directions,
    snake_one_output_locations,
    snake_one_output_directions,
    snake_two_output_locations,
    snake_two_output_directions,
    snake_moves,
):
    """
    Check that the model initializes correctly

    Parameters:
        snake_one_locations: list of lists initial integer coords for segments
        snake_one_directions: list of strings of directions for segments
        snake_two_locations: list of lists initial integer coords for segments
        snake_two_directions: list of strings with directions for segments
        snake_one_output_locations: list of lists final integer coordinates for
        segments
        snake_one_output_directions: list of strings with final directions for
        segments
        snake_two_output_locations: list of lists final integer coordinates for
        segments
        snake_two_output_directions: list of strings with final directions for
        segments
        snake_moves: list of tuples with snake_one_moves as strings
    """
    game = SnakeGameModel(
        snake_one_locations=snake_one_locations,
        snake_two_locations=snake_two_locations,
        snake_one_directions=snake_one_directions,
        snake_two_directions=snake_two_directions,
    )

    for move in snake_moves:
        game.move_snakes(*move)

    assert game.snake_one.locations == snake_one_output_locations
    assert game.snake_two.locations == snake_two_output_locations
    assert game.snake_one.directions == snake_one_output_directions
    assert game.snake_two.directions == snake_two_output_directions
    assert game.apples == [[9, 9]]
    assert game.game_state == 1


@pytest.mark.parametrize(
    "snake_one_locations, snake_one_directions, snake_two_locations, "
    + "snake_two_directions, snake_one_won, snake_two_won",
    snake_won_cases,
)
def test_snake_won(
    snake_one_locations,
    snake_one_directions,
    snake_two_locations,
    snake_two_directions,
    snake_one_won,
    snake_two_won,
):
    """
    Check that the collision logic is correct

    Parameters:
    snake_one_locations: list of lists initial integer coordinates for segments
    snake_one_directions: list of strings with initial directions for segments
    snake_two_locations: list of lists with initial integer coordinates for
    segments
    snake_two_directions: list of strings with initial directions for segments
    snake_one_won: boolean of if snake one has won
    snake_two_won: boolean of if snake one has won
    """
    game = SnakeGameModel(
        snake_one_locations=snake_one_locations,
        snake_two_locations=snake_two_locations,
        snake_one_directions=snake_one_directions,
        snake_two_directions=snake_two_directions,
    )

    snake_one, snake_two = game.snake_won()

    assert snake_one == snake_one_won
    assert snake_two == snake_two_won


def test_snake_won_from_length():
    """
    Test that if a snake has eaten 10 apples it wins
    """
    game = SnakeGameModel()
    game.snake_one._apples_eaten = 10  # pylint: disable=protected-access
    snake_one, snake_two = game.snake_won()

    assert snake_one
    assert not snake_two
