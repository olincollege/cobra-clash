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
    def draw(self, frame_rate):
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

    def draw(self, frame_rate):
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

    def __init__(self, model, width, height):
        super().__init__(model)

        # Initializing pygame
        self._screen = pygame.display.set_mode((width, height))
        self._clock = pygame.time.Clock()
        pygame.display.set_caption("Cobra Clash")

        # Snake map with a 19 x 19 grid
        self._snake_map = pygame.image.load("images/snake_map.jpeg")

        # To place the assets properly on the board
        self._shift = height - width

        # Assets
        self._start_screen = pygame.image.load("images/start_screen.png")
        self._snake_one_wins = pygame.image.load("images/snake_one_wins.png")
        self._snake_two_wins = pygame.image.load("images/snake_two_wins.png")
        self._tie = pygame.image.load("images/tie.jpeg")

        self._snake_one_head = pygame.image.load("images/snake_head_one.png")
        self._snake_one_body = pygame.Surface((50, 50))
        self._snake_one_body.fill("Green")

        self._snake_two_head = pygame.image.load("images/snake_head_two.png")
        self._snake_two_body = pygame.Surface((50, 50))
        self._snake_two_body.fill("Red")

        self._apple = pygame.image.load("images/apple.png")

    def _snake_head_direction(self, snake_head, direction):
        """_summary_"""

        head_directions = {
            "UP": pygame.transform.rotate(snake_head, 180),
            "DOWN": pygame.transform.rotate(snake_head, 0),
            "RIGHT": pygame.transform.rotate(snake_head, 90),
            "LEFT": pygame.transform.rotate(snake_head, -90),
        }
        return head_directions[direction]

    def _draw_snake(self, snake, snake_body, snake_head):
        """_summary_

        Args:
            snake (Snake)
            snake_body (_type_): _description_
            snake_head (_type_): _description_
        """

        for index, location in enumerate(snake.locations):
            # Convert the index for the square in the grade into the
            # pixel location on the screen
            x = location[1] * 50
            y = location[0] * 50 + self._shift
            direction = snake.directions[0]
            if index == 0:
                self._screen.blit(
                    self._snake_head_direction(snake_head, direction), (x, y)
                )
                continue
            self._screen.blit(snake_body, (x, y))

    def _draw_start_screen(self):
        """_summary_"""
        self._screen.blit(self._start_screen, (0, 0))

    def _draw_running_game(self):
        """_summary_"""
        self._screen.blit(self._snake_map, (0, self._shift))

        # Draw the snakes
        self._draw_snake(
            self._model.snake_one, self._snake_one_body, self._snake_one_head
        )
        self._draw_snake(
            self._model.snake_two, self._snake_two_body, self._snake_two_head
        )

        # Draw the apple
        for apple in self._model.apples:
            self._screen.blit(
                self._apple, (apple[1] * 50, apple[0] * 50 + self._shift)
            )

    def _draw_end_screen(self):
        """_summary_"""
        if self._model.collision()[0] and self._model.collision()[1]:
            self._screen.blit(self._tie, (0, 0))
        elif self._model.collision()[1]:
            self._screen.blit(self._snake_one_wins, (0, 0))
        else:
            self._screen.blit(self._snake_two_wins, (0, 0))

    def draw(self, frame_rate):
        """summary"""

        if self._model.game_state == 1:
            self._draw_start_screen()
        elif self._model.game_state == 2:
            self._draw_running_game()
        else:
            self._draw_end_screen()

        # Update the display
        pygame.display.update()

        # Set the frames per second for the game
        self._clock.tick(frame_rate)
