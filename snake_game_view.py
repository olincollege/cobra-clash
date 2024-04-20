from abc import ABC, abstractmethod
import pygame


class SnakeGameView(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, model):
        super().__init__()
        self._model = model

    @abstractmethod
    def draw(self):
        """_summary_"""


class TextView(SnakeGameView):
    """
    Class to view a snake game as text

    Attributes:
        _model: instance of SnakeGameModel that contains game state
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
        height = self._model.model_height
        width = self._model.board_width
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
                    if [
                        board_row,
                        board_col,
                    ] in self._model.snake_one.locations:
                        if [
                            board_row,
                            board_col,
                        ] != self._model.snake_one.locations[0]:
                            line += self.snake_one_body
                        else:
                            line += self.snake_one_heads[
                                self._model.snake_one.directions[0]
                            ]
                    elif [
                        board_row,
                        board_col,
                    ] in self._model.snake_two.locations:
                        if [
                            board_row,
                            board_col,
                        ] != self._model.snake_two.locations[0]:
                            line += self.snake_two_body
                        else:
                            line += self.snake_two_heads[
                                self._model.snake_two.directions[0]
                            ]
                    elif [board_row, board_col] in self._model.apples:
                        line += self.apple

                    else:
                        line += self.empty_space
            print(line)


class GraphicalView(SnakeGameView):
    """summary"""

    def __init__(self, model):
        super().__init__(model)
        self.screen = pygame.display.set_mode((960, 1280))
        pygame.display.set_caption("Cobra Clash")
        self._clock = pygame.time.Clock()
        self._snake_map = pygame.Surface((960, 960))
        self._snake_map.fill("White")
        # board size 19 x 19
        self._snake_head = pygame.image.load("images/snake_head.png")
        self._snake_body_1 = pygame.Surface((50, 50))
        self._snake_body_1.fill("Green")

        self._snake_body_2 = pygame.Surface((50, 50))
        self._snake_body_2.fill("Red")

    def draw(self):
        """summary"""
        self.screen.blit(self._snake_map, (0, 310))

        # Draw the self._snake 1
        for i in range(self._model.sn)
        self.screen.blit(self._snake_head, (0, 360))
        self.screen.blit(self._snake_body_1, (0, 310))

        # Draw the self._snake 2
        self.screen.blit(self._snake_head, (910, 360))
        self.screen.blit(self._snake_body_2, (910, 310))
        # Update the display
        pygame.display.update()

        # Set the frames per second for the game
        self._clock.tick(60)
