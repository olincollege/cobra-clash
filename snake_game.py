"""
Running the snake game
"""

import sys
import pygame
from double_snake_game_model import SnakeGameModel
from snake_game_view import TextView, GraphicalView


game = SnakeGameModel()
view = TextView(game)
view.draw()
print(game.move_snakes("RIGHT", "LEFT"))
view.draw()
game.move_snakes("RIGHT", "LEFT")
view.draw()
print(game.move_snakes("RIGHT", "LEFT"))
view.draw()
print(game.move_snakes("RIGHT", "UP"))
view.draw()
print(game.move_snakes("RIGHT", "UP"))
view.draw()

game = SnakeGameModel()
graphics = GraphicalView(game)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game.move_snakes("DOWN", "LEFT")
    graphics.draw()
