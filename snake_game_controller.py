"""Controller class for snake game"""

import sys
from abc import ABC, abstractmethod
import pygame


class SnakeGameController(ABC):
    """
    An abstract class used for controlling the board according to
    the input provided from the user

    Attributes:
        _model: An instance of the SnakeGameModel class
    """

    def __init__(self, model):
        """
        Initializes an instance of the SnakeGameController class

        Parameters:
            model: An instance of the SnakeGameModel class
        """
        super().__init__()
        self._model = model

    @property
    def model(self):
        """
        A property that returns the snake game model stored in the
        SnakeGameModel instance
        """
        return self._model

    @abstractmethod
    def move(self):
        """
        An abstract method to move the snakes according to the input
        of the user, defined in the following class
        """


class GraphicalController(SnakeGameController):
    """
    A class inheriting from the SnakeGameController class to control
    the snakes according to the inputs

    Parameters:
        SnakeGameController: An instance of the SnakeGameController class
    """

    _player_one_moves = {
        pygame.K_w: "UP",
        pygame.K_s: "DOWN",
        pygame.K_a: "LEFT",
        pygame.K_d: "RIGHT",
    }

    _player_two_moves = {
        pygame.K_UP: "UP",
        pygame.K_DOWN: "DOWN",
        pygame.K_LEFT: "LEFT",
        pygame.K_RIGHT: "RIGHT",
    }

    def __init__(self, model):
        """
        Initializes the GraphicController class

        Parameters:
            model: An instance of the SnakeGameModel class
        """
        super().__init__(model)
        self._player_one_cue = ["RIGHT"]
        self._player_two_cue = ["LEFT"]
        self.events = []

    def reset(self):
        """
        Resets the different variables used to move the snakes
        """
        self._player_one_cue = ["RIGHT"]
        self._player_two_cue = ["LEFT"]
        self.events = []

    def fetch_events(self):
        """Fetch all pygame events and store them internally."""
        self.events = pygame.event.get()
        self._process_events()

    def _process_events(self):
        """Process the stored events to update game state accordingly."""
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self._model.game_state == 1:
                    if event.key == pygame.K_SPACE:
                        self._model.set_game_state(2)
                elif self._model.game_state == 2:
                    if event.key in self._player_one_moves:
                        if len(self._player_one_cue) < 3:
                            self._player_one_cue.append(
                                self._player_one_moves[event.key]
                            )
                    elif event.key in self._player_two_moves:
                        if len(self._player_two_cue) < 3:
                            self._player_two_cue.append(
                                self._player_two_moves[event.key]
                            )
                else:
                    if event.key == pygame.K_SPACE:
                        self._model.reset()
                        self.reset()
                        self._model.set_game_state(2)

    def move(self):
        """Update game state based on the first command in the queue,
        if available."""
        if len(self._player_one_cue) > 1:
            self._player_one_cue.pop(0)
        if len(self._player_two_cue) > 1:
            self._player_two_cue.pop(0)

        self._model.move_snakes(
            self._player_one_cue[0], self._player_two_cue[0]
        )
        if len(self._player_one_cue) > 1:
            self._player_one_cue.pop(0)
        if len(self._player_two_cue) > 1:
            self._player_two_cue.pop(0)
