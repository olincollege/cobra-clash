"""
Running the snake game
"""

from snake_game_model import SnakeGameModel
from snake_game_view import GraphicalView
from snake_game_controller import GraphicalController


def main():
    """
    Play a game of snake
    """

    game = SnakeGameModel()
    graphics = GraphicalView(game, 1400, 1050)
    controller = GraphicalController(game)

    while True:
        controller.fetch_events()  # Update events at the start of each frame
        if game.game_state == 2:
            controller.move()
            if True in game.snake_won():
                game.set_game_state(3)

        graphics.draw(7)


if __name__ == "__main__":
    main()
