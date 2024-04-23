"""
Running the snake game
"""

import time
import sys
from double_snake_game_model import SnakeGameModel
from snake_game_view import GraphicalView
from snake_game_controller import GraphicalController


def main():
    """
    Play a game of snake
    """

    game = SnakeGameModel()
    graphics = GraphicalView(game)
    controller = GraphicalController(game)

    while True:
        graphics.draw()

        while True:
            if controller.start_game():
                graphics.draw()
                break

        while True:
            controller.move()
            one_collision, two_collision = game.collision()
            graphics.draw()
            if one_collision or two_collision:
                break

        game.reset()


if __name__ == "__main__":
    main()
