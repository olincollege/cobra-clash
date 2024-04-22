"""
Running the snake game
"""

import sys
import pygame
from double_snake_game_model import SnakeGameModel
from snake_game_view import TextView, GraphicalView
from snake_game_controller import GraphicalController

# game = SnakeGameModel()
# view = TextView(game)
# view.draw()
# print(game.move_snakes("RIGHT", "LEFT"))
# view.draw()
# game.move_snakes("RIGHT", "LEFT")
# view.draw()
# print(game.move_snakes("RIGHT", "LEFT"))
# view.draw()
# print(game.move_snakes("RIGHT", "UP"))
# view.draw()
# print(game.move_snakes("RIGHT", "UP"))
# view.draw()

game = SnakeGameModel()
graphics = GraphicalView(game)
controller = GraphicalController(game)
while True:
    controller.move()
    graphics.draw()
