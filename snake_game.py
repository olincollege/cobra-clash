from double_snake_game_model import SnakeGameModel
from snake_view import SnakeGameTextView

game = SnakeGameModel()
view = SnakeGameTextView(game)
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
