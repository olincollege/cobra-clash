"""
Class to represent the model of a two player game of snake
"""

import random
from snake import Snake


class SnakeGameModel:
    """
    Class to store and track the state of a snake game

    Attributes:
        board_width: int representing width of game board
        board_height: int representing height of game board
        snake_starting_length: int representing how long snakes start as
        num_apples: int representing how many apples on board
        snake_one: instance of snake object
        snake_two: instance of snake object
        apples: list of lists with integer coords of apples
        game_state: integer representing phase of game (starting screen,
        playing game, ending screen)
    """

    _board_width = 19
    _board_height = 19
    _snake_starting_length = 4
    _num_apples = 1

    def __init__(
        self,
        snake_one_locations=None,
        snake_one_directions=None,
        snake_two_locations=None,
        snake_two_directions=None,
    ):
        """
        Creates an instance of the SnakeGameState class

        Parameters:
            snake_one_locations: list of lists containing initial integer
            coords for snake one segments
            snake_one_directions: list of strings with initial directions for
            snake one segments
            snake_two_locations: list of lists containing initial integer
            coords for snake two segments
            snake_two_directions: list of strings with initial directions for
            snake two segments
        """
        self._setup(
            snake_one_locations=snake_one_locations,
            snake_one_directions=snake_one_directions,
            snake_two_locations=snake_two_locations,
            snake_two_directions=snake_two_directions,
        )
        self._game_state = 1

    def reset(self):
        """
        Resets the attributes to the default state
        """
        self._setup()

    def _setup(
        self,
        snake_one_locations=None,
        snake_one_directions=None,
        snake_two_locations=None,
        snake_two_directions=None,
    ):
        """
        Sets the attributes of the game to initial state

        Parameters:
            snake_one_locations: list of lists containing initial integer
            coords for snake one segments
            snake_one_directions: list of strings with initial directions for
            snake one segments
            snake_two_locations: list of lists containing initial integer
            coords for snake two segments
            snake_two_directions: list of strings with initial directions for
            snake two segments
        """
        if snake_one_locations is None or snake_one_directions is None:
            self._snake_one = Snake(
                [self._board_height // 2 - 1, (self._board_width // 2) - 5],
                "RIGHT",
                self._snake_starting_length,
            )
        else:
            self._snake_one = Snake(
                None,
                None,
                None,
                locations_and_directions=[
                    snake_one_locations,
                    snake_one_directions,
                ],
            )
        if snake_two_locations is None or snake_two_directions is None:
            self._snake_two = Snake(
                [self._board_height // 2 + 1, self._board_width // 2 + 5],
                "LEFT",
                self._snake_starting_length,
            )
        else:
            self._snake_two = Snake(
                None,
                None,
                None,
                locations_and_directions=[
                    snake_two_locations,
                    snake_two_directions,
                ],
            )

        self._apples = []
        for i in range(1, self._num_apples + 1):
            self._apples.append(
                [
                    i * (self._board_height // (self._num_apples + 1)),
                    self.board_width // 2,
                ]
            )

    def move_snakes(self, snake_one_direction, snake_two_direction):
        """
        Advance the snake in the indicated direction and return if either
        has died

        Parameters:
            snake_one_direction: String of direction for snake one to move in
            snake_two_direction: String of direction for snake two to move in
        """
        self._snake_one.move(snake_one_direction)
        self._snake_two.move(snake_two_direction)

        self._check_and_eat()

    def snake_won(self):
        """
        Checks whether a player has won or not

        Returns:
            bool: whether snake one has won
            bool: whether snake two has won
        """

        snake_one_won = False
        snake_two_won = False

        if self._collision()[0] and self._collision()[1]:
            snake_one_won = True
            snake_two_won = True
        elif self._collision()[1] or self._snake_one.apples_eaten == 10:
            snake_one_won = True
        elif self._collision()[0] or self._snake_two.apples_eaten == 10:
            snake_two_won = True

        return snake_one_won, snake_two_won

    def _collision(self):
        """
        Checks if either snake has collided with itself, each other, or wall

        Returns:
            bool: whether snake one has died
            bool: whether snake two has died
        """
        collision_one = False
        collision_two = False
        wall_collision_one, wall_collision_two = self._wall_collision()
        snake_collision_one, snake_collision_two = self._snake_collision()

        if wall_collision_one or snake_collision_one:
            collision_one = True
        if wall_collision_two or snake_collision_two:
            collision_two = True

        if collision_one or collision_two:
            self._game_state = 3

        return collision_one, collision_two

    def _wall_collision(self):
        """
        Checks if either snake has collided with itself or each other

        Returns:
            bool: whether snake one has collided
            bool: whether snake two has collided
        """
        snake_one = False
        snake_two = False

        # Check that snake one head still in x bounds
        if (
            self._snake_one.locations[0][1] < 0
            or self._snake_one.locations[0][1] >= self.board_width
        ):
            snake_one = True

        # Check that snake one head still in y bounds
        if (
            self._snake_one.locations[0][0] < 0
            or self._snake_one.locations[0][0] >= self.board_height
        ):
            snake_one = True

        # Check that snake two head still in x bounds
        if (
            self._snake_two.locations[0][1] < 0
            or self._snake_two.locations[0][1] >= self.board_width
        ):
            snake_two = True

        # Check that snake two head still in y bounds
        if (
            self._snake_two.locations[0][0] < 0
            or self._snake_two.locations[0][0] >= self.board_height
        ):
            snake_two = True

        return snake_one, snake_two

    def _snake_collision(self):
        """
        Checks if either snake has collided with itself or each other

        Returns:
            bool: whether snake one has collided
            bool: whether snake two has collided
        """
        snake_one = False
        snake_two = False

        # Check that snake one head hasn't collided with self
        for i in range(1, len(self._snake_one.locations)):
            if self._snake_one.locations[0] == self._snake_one.locations[i]:
                snake_one = True

        # Check that snake one hasn't collided with snake two
        for coord in self._snake_two.locations:
            if self._snake_one.locations[0] == coord:
                snake_one = True

        # Check that snake two head hasn't collided with self
        for i in range(1, len(self._snake_two.locations)):
            if self._snake_two.locations[0] == self._snake_two.locations[i]:
                snake_two = True

        # Check that snake two hasn't collided with snake one
        for coord in self._snake_one.locations:
            if self._snake_two.locations[0] == coord:
                snake_two = True

        return snake_one, snake_two

    def _check_and_eat(self):
        """
        Checks if the snake is eating and if so grows and generates new apple
        """
        # Check and grow snake one
        eaten_indexes = []
        for i, apple in enumerate(self._apples):
            if self._snake_one.locations[0] == apple:
                eaten_indexes.append(i)
                self._snake_one.grow()
            if self._snake_two.locations[0] == apple:
                eaten_indexes.append(i)
                self._snake_two.grow()

        for index in eaten_indexes:
            self._new_apple(index)

    def _new_apple(self, old_index):
        """
        Change apple location at index to new location

        Parameters:
            old_index: Integer representing the index of the apple to update
        """
        empty_spaces = []
        for row in range(self._board_height):
            for col in range(self._board_width):
                if (
                    [row, col] not in self._snake_one.locations
                    and [row, col] not in self._snake_two.locations
                    and [row, col] not in self._apples
                ):
                    empty_spaces.append([row, col])

        self._apples[old_index] = random.choice(empty_spaces)

    def set_game_state(self, new_state):
        """
        Sets the game state to new game state

        Parameters:
            new_state: Integer representing the new state
        """
        self._game_state = new_state

    def __repr__(self):
        """
        Defines how the map would be printed
        """
        empty_space = " "
        snake_one_body = "■"
        snake_two_body = "□"
        snake_one_heads = {"UP": "▲", "DOWN": "▼", "LEFT": "◀", "RIGHT": "▶"}
        snake_two_heads = {"UP": "△", "DOWN": "▽", "LEFT": "◁", "RIGHT": "▷"}
        apple = "◈"
        wall = "▩"

        output = ""
        for row in range(self.board_height + 2):
            line = ""
            for col in range(self.board_width + 2):
                if row in (0, self.board_height + 1) or col in (
                    0,
                    self.board_width + 1,
                ):
                    line += wall
                else:
                    board_row, board_col = row - 1, col - 1
                    board_pos = [board_row, board_col]

                    if board_pos in self.snake_one.locations:
                        line += (
                            snake_one_heads[self.snake_one.directions[0]]
                            if board_pos == self.snake_one.locations[0]
                            else snake_one_body
                        )
                    elif board_pos in self.snake_two.locations:
                        line += (
                            snake_two_heads[self.snake_two.directions[0]]
                            if board_pos == self.snake_two.locations[0]
                            else snake_two_body
                        )
                    elif board_pos in self.apples:
                        line += apple
                    else:
                        line += empty_space
            output += line + "\n"
        return output

    @property
    def game_state(self):
        """
        Returns the current game state as int
        """
        return self._game_state

    @property
    def board_width(self):
        """
        Returns the board width as an int
        """
        return self._board_width

    @property
    def board_height(self):
        """
        Returns the board height as an int
        """
        return self._board_height

    @property
    def snake_starting_length(self):
        """
        Returns the snake starting length as an int
        """
        return self._snake_starting_length

    @property
    def snake_one(self):
        """
        Gets snake one

        Returns:
            Snake: instance of snake class
        """
        return self._snake_one

    @property
    def snake_two(self):
        """
        Gets snake two

        Returns:
            Snake: instance of snake class
        """
        return self._snake_two

    @property
    def apples(self):
        """
        Returns the location of the apples as a list of list of coordinates
        """
        return self._apples
