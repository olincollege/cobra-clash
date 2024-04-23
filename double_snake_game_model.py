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

    """

    _board_width = 19
    _board_height = 19
    _snake_starting_length = 4
    _num_apples = 1

    def __init__(self):
        """
        Creates an instance of the SnakeGameState class
        """
        self._setup()

    def reset(self):
        """
        Resets the attributes to the intial state
        """
        self._setup()

    def _setup(self):
        """
        Sets the attributes of the game to inital state
        """
        self._snake_one = Snake(
            self._board_height // 2,
            (self._board_width // 2) - 4,
            "RIGHT",
            self._snake_starting_length,
        )
        self._snake_two = Snake(
            self._board_height // 2,
            (self._board_width // 2) + 4,
            "LEFT",
            self._snake_starting_length,
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

        Attributes:
            direction: String which direction for head to move in

        """
        self._snake_one.move(snake_one_direction)
        self._snake_two.move(snake_two_direction)

        self._check_and_eat()

    def collision(self):
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

    @property
    def board_width(self):
        """
        Returns the current game model
        """
        return self._board_width

    @property
    def board_height(self):
        """
        Returns the current game model
        """
        return self._board_height

    @property
    def snake_starting_length(self):
        """
        Returns the current game model
        """
        return self._snake_starting_length

    @property
    def snake_one(self):
        """
        Returns the current game model
        """
        return self._snake_one

    @property
    def snake_two(self):
        """
        Returns the current game model
        """
        return self._snake_two

    @property
    def apples(self):
        """
        Returns the current game model
        """
        return self._apples
