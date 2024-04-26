"""Controller class for snake game"""

import sys
import pygame
from abc import ABC, abstractmethod


class SnakeGameController(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, model):
        """_summary_"""
        super().__init__()
        self._model = model

    @abstractmethod
    def move(self):
        """_summary_"""


class GraphicalController(SnakeGameController):
    """_summary_

    Args:
        SnakeGameController (_type_): _description_
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
        super().__init__(model)
        self._player_one_cue = ["RIGHT"]
        self._player_two_cue = ["LEFT"]
        self.events = []
        self.space_pressed = False

    def reset(self):
        self._player_one_cue = ["RIGHT"]
        self._player_two_cue = ["LEFT"]
        self.events = []
        self.space_pressed = False

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
                elif event.key == pygame.K_SPACE:
                    self.space_pressed = True

    def start_game(self):
        """Check if the game should start based on internal state."""
        if self.space_pressed:
            self.space_pressed = False  # Reset the flag
            return True
        return False

    def move(self):
        """Update game state based on the first command in the queue, if available."""
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
