from double_snake_game_model import SnakeGameModel
from snake_view import SnakeGameTextView

game = SnakeGameModel()
print(game.snake_one.locations)
print(game.snake_two.locations)
view = SnakeGameTextView(game)
view.draw()
