"""
Running the snake game
"""

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

    running = True
    game_active = False

    graphics.draw()
    while running:
        controller.fetch_events()  # Update events at the start of each frame

        if not game_active and controller.start_game():
            game_active = True
            game.reset()
            controller.reset()
            continue

        if game_active:
            controller.move()
            graphics.draw()
            one_collision, two_collision = game.collision()
            if one_collision or two_collision:
                game_active = False


if __name__ == "__main__":
    main()
