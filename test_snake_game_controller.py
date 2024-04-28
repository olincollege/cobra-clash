"""
Test the graphical controller class
"""

# pylint: disable=redefined-outer-name
# pylint: disable=protected-access
from unittest.mock import Mock, patch
import pytest
import pygame

from snake_game_controller import GraphicalController


@pytest.fixture(autouse=True)
def mock_pygame_init():
    """
    Automatically mock pygame initialization and display setup.
    """
    with patch("pygame.init"), patch("pygame.display.set_mode"):
        yield


@pytest.fixture
def mock_model():
    """
    Create a mock model to pass to the GraphicalController.

    Returns:
        Mock: A mock object with methods and attributes to simulate the
        behavior of the game model.
    """
    model = Mock()
    model.move_snakes = Mock()
    model.set_game_state = Mock()
    model.reset = Mock()
    model.game_state = 2  # Assuming default game state is '2' for active
    return model


@pytest.fixture
def controller(mock_model):
    """
    Create an instance of GraphicalController with a mocked model.

    Parameters:
        mock_model (Mock): The mocked game model used for testing.

    Yields:
        Tuple[GraphicalController, MagicMock]: A tuple containing the
        GraphicalController instance and the mocked pygame event getter.
    """
    with patch("pygame.event.get") as mock_pygame_event_get:
        controller = GraphicalController(mock_model)
        yield controller, mock_pygame_event_get


def test_reset(controller):
    """
    Test the reset method to ensure it properly reinitializes the
    controller's internal state.

    Parameters:
        controller (Fixture[Tuple[GraphicalController, MagicMock]]): The
        controller fixture from pytest with a mocked model.
    """
    ctrl, _ = controller
    ctrl.reset()
    assert ctrl._player_one_cue == [
        "RIGHT"
    ], "Player one cue should be reset to ['RIGHT']"
    assert ctrl._player_two_cue == [
        "LEFT"
    ], "Player two cue should be reset to ['LEFT']"
    assert ctrl.events == [], "Events should be cleared"


def test_fetch_events(controller):
    """
    Test the fetch_events method to ensure it processes input events correctly.

    Parameters:
        controller (Fixture[Tuple[GraphicalController, MagicMock]]): The
        controller fixture from pytest with a mocked model.
    """
    ctrl, mock_pygame_event_get = controller
    mock_event = Mock()
    mock_event.type = pygame.KEYDOWN
    mock_event.key = pygame.K_w
    mock_pygame_event_get.return_value = [mock_event]

    ctrl.fetch_events()

    assert mock_pygame_event_get.called, "pygame.event.get should be called"
    assert ctrl._player_one_cue == [
        "RIGHT",
        "UP",
    ], "Player one cue should contain 'UP'"


def test_move(controller, mock_model):
    """
    Test the move method to ensure it properly processes the movement cues and
    interacts with the model.

    Parameters:
        controller (Fixture[Tuple[GraphicalController, MagicMock]]): The
        controller fixture from pytest with a mocked model.
        mock_model (Mock): The mocked game model used for testing.
    """
    ctrl, _ = controller
    ctrl._player_one_cue = ["RIGHT", "UP", "DOWN"]
    ctrl._player_two_cue = ["LEFT", "DOWN", "UP"]
    ctrl.move()

    # Check if model.move_snakes is called with the right parameters
    mock_model.move_snakes.assert_called_with("UP", "DOWN")
    assert ctrl._player_one_cue == [
        "DOWN"
    ], "Player one cue should be processed"
    assert ctrl._player_two_cue == ["UP"], "Player two cue should be processed"


def test_process_events_game_state_changes(controller, mock_model):
    """
    Test how game state changes are handled specific events during the game.

    Parameters:
        controller (Fixture[Tuple[GraphicalController, MagicMock]]): The
        controller fixture from pytest with a mocked model.
        mock_model (Mock): The mocked game model used for testing.
    """
    ctrl, mock_pygame_event_get = controller
    # Simulate a space key press event when game state is 1
    mock_event_space = Mock(type=pygame.KEYDOWN, key=pygame.K_SPACE)
    mock_model.game_state = 1
    mock_pygame_event_get.return_value = [mock_event_space]

    ctrl.fetch_events()

    # Check if game state is set correctly upon pressing space
    mock_model.set_game_state.assert_called_with(2)
