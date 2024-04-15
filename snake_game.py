from snake_game_model import SnakeGameModel
from snake_view import SnakeGameTextView

game = SnakeGameModel()
view = SnakeGameTextView(game)
view.draw()
print(game.move_snake("RIGHT"))
view.draw()
print(game.move_snake("RIGHT"))
view.draw()
print(game.move_snake("RIGHT"))
view.draw()
print(game.move_snake("RIGHT"))
view.draw()
