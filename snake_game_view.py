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
        height = self._model.board_height
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
        self._head_directions = {
            "UP": pygame.transform.rotate(self._snake_head, 180),
            "DOWN": pygame.transform.rotate(self._snake_head, 0),
            "RIGHT": pygame.transform.rotate(self._snake_head, 90),
            "LEFT": pygame.transform.rotate(self._snake_head, -90),
        }
        self._snake_body_one = pygame.Surface((50, 50))
        self._snake_body_one.fill("Green")

        self._snake_body_two = pygame.Surface((50, 50))
        self._snake_body_two.fill("Red")

        self._apple = pygame.image.load("images/apple.png")

    def draw(self):
        """summary"""
        self.screen.blit(self._snake_map, (0, 310))

        # Draw the self._snake 1
        for index, location in enumerate(self._model.snake_one.locations):
            x = location[1]
            y = location[0]
            direction = self._model.snake_one.directions[0]
            if index == 0:
                self.screen.blit(
                    self._head_directions[direction], (x * 50, y * 50 + 310)
                )
                continue
            self.screen.blit(self._snake_body_one, (x * 50, y * 50 + 310))
            self.screen.blit(self._snake_body_one, (x * 50, y * 50 + 310))

        # Draw the self._snake 2
        for index, location in enumerate(self._model.snake_two.locations):
            x = location[1]
            y = location[0]
            direction = self._model.snake_two.directions[0]
            if index == 0:
                self.screen.blit(
                    self._head_directions[direction], (x * 50, y * 50 + 310)
                )
                continue
            self.screen.blit(self._snake_body_two, (x * 50, y * 50 + 310))

        # Draw the apple
        for apple in self._model.apples:
            self.screen.blit(self._apple, (apple[1] * 50, apple[0] * 50 + 310))

        # Update the display
        pygame.display.update()

        # Set the frames per second for the game
        self._clock.tick(3)
