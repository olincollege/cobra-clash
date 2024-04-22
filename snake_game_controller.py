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
        self._snake_one_direction = "RIGHT"
        self._snake_two_direction = "LEFT"

    @abstractmethod
    def move(self):
        """_summary_"""


class GraphicalController(SnakeGameController):
    """_summary_

    Args:
        SnakeGameController (_type_): _description_
    """

    def move(self):
        """summary"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._snake_one_direction = "UP"
                elif event.key == pygame.K_DOWN:
                    self._snake_one_direction = "DOWN"
                elif event.key == pygame.K_LEFT:
                    self._snake_one_direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    self._snake_one_direction = "RIGHT"

                if event.key == pygame.K_w:
                    self._snake_two_direction = "UP"
                elif event.key == pygame.K_s:
                    self._snake_two_direction = "DOWN"
                elif event.key == pygame.K_a:
                    self._snake_two_direction = "LEFT"
                elif event.key == pygame.K_d:
                    self._snake_two_direction = "RIGHT"

        self._model.move_snakes(
            self._snake_one_direction, self._snake_two_direction
        )
