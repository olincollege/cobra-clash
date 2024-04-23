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
        pygame.K_UP: "UP",
        pygame.K_DOWN: "DOWN",
        pygame.K_LEFT: "LEFT",
        pygame.K_RIGHT: "RIGHT",
    }

    _player_two_moves = {
        pygame.K_w: "UP",
        pygame.K_s: "DOWN",
        pygame.K_a: "LEFT",
        pygame.K_d: "RIGHT",
    }

    def __init__(self, model):
        super().__init__(model)
        self._player_one_cue = ["RIGHT"]
        self._player_two_cue = ["LEFT"]

    def move(self):
        """summary"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        self._model.move_snakes(
            self._player_one_cue[0], self._player_two_cue[0]
        )

        if len(self._player_one_cue) > 1:
            self._player_one_cue.pop(0)
        if len(self._player_two_cue) > 1:
            self._player_two_cue.pop(0)

    def start_game(self):
        """
        Returns true if space is pressed
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True
            return False
