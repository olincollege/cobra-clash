from abc import ABC, abstractmethod


class SnakeGameView(ABC):
    """
    Abstract base class to view snake game

    Attributes:
        model: instance of SnakeGameModel that contains game state
    """

    def __init__(self, game_model):
        """
        Initialize a SnakeGameView object

        Attributes:
        model: instance of SnakeGameModel that contains game state
        """
        self._model = game_model

    @property
    def model(self):
        """
        Returns the current game model
        """
        return self._model

    @abstractmethod
    def draw(self):
        """
        Abstract method to draw the snake game
        """


class SnakeGameTextView(SnakeGameView):
    """
    Class to view a snake game as text

    Attributes:
        model: instance of SnakeGameModel that contains game state
    """

    empty_space = " "
    snake_one_body = "■"
    snake_two_body = "□"
    snake_one_heads = {"UP": "▲", "DOWN": "▼", "LEFT": "◀", "RIGHT": "▶"}
    snake_two_heads = {"UP": "△", "DOWN": "▽", "LEFT": "◁", "RIGHT": "▷"}
    apple = "◈"
    wall = "▩"

    def draw(self):
        """
        Prints the state of the snake game
        """
        height = self.model.board_height
        width = self.model.board_width
        for row in range(height + 2):
            line = ""
            for col in range(width + 2):
                if row == 0 or col == 0:
                    line += self.wall
                elif row == height + 1 or col == width + 1:
                    line += self.wall
                else:
                    board_row = row - 1
                    board_col = col - 1
                    if [board_row, board_col] in self.model.snake_one.locations:
                        if [
                            board_row,
                            board_col,
                        ] != self.model.snake_one.locations[0]:
                            line += self.snake_one_body
                        else:
                            line += self.snake_one_heads[
                                self.model.snake_one.directions[0]
                            ]
                    elif [
                        board_row,
                        board_col,
                    ] in self.model.snake_two.locations:
                        if [
                            board_row,
                            board_col,
                        ] != self.model.snake_two.locations[0]:
                            line += self.snake_two_body
                        else:
                            line += self.snake_two_heads[
                                self.model.snake_two.directions[0]
                            ]
                    elif [board_row, board_col] in self.model.apples:
                        line += self.apple

                    else:
                        line += self.empty_space
            print(line)
