import random
from snake import Snake


class SnakeGameModel:
    """
    Class to store and track the state of a snake game
    """

    _board_width = 9
    _board_height = 10
    _snake_starting_length = 3
    _starting_direction = "RIGHT"
    _num_apples = 1

    def __init__(self):
        """
        Creates an instance of the SnakeGameState class
        """
        self._snake_one = Snake(
            self._board_height // 2, (self._board_width // 2) - 2, "RIGHT", 3
        )
        self._snake_two = Snake(
            self._board_height // 2, (self._board_width // 2) + 2, "LEFT", 3
        )

        self._apples = []
        for i in range(1, self._num_apples + 1):
            self._apples.append(
                [
                    i * (self._board_height // (self._num_apples + 1)),
                    self.board_width - 2,
                ]
            )

    def move_snakes(self, snake_one_direction, snake_two_direction):
        """
        Advance the snake in the indicated direction

        Attributes:
            direction: String which direction for head to move in

        Returns:
            Boolean representing if valid move
        """
        self._snake_one.move(snake_one_direction)
        self._snake_two.move(snake_two_direction)

        self._check_and_eat()

    def _snake_collision(self):
        """
        Checks if either snake has collided with itself or

        Returns:
            Integer representing which snake collided or 0 for niether
        """
        # Check that the head hasn't collided with body
        for i in range(1, len(self._snake)):
            if self._snake[0] == self._snake[i]:
                return True

        # Check that head still in x bounds
        if self._snake[0][1] < 0 or self._snake[0][1] >= self.board_width:
            return True

        # Check that head still in y bounds
        if self._snake[0][0] < 0 or self._snake[0][0] >= self.board_height:
            return True

        return False

    def _check_and_eat(self):
        """
        Checks if the snake is eating and if so grows and generates new apple
        """
        # Check and grow snake one
        apple_index = -1
        for i, apple in enumerate(self._apples):
            if self._snake[0] == apple:
                apple_index = i

        if apple_index != -1:
            self._new_apple(apple_index)
            self._grow_snake()

    def _new_apple(self, old_index):
        """
        Change apple location at index to new location
        """
        empty_spaces = []
        for row in range(self._board_height):
            for col in range(self._board_width):
                if [row, col] not in self._snake and [
                    row,
                    col,
                ] not in self._apples:
                    empty_spaces.append([row, col])

        self._apples[old_index] = random.choice(empty_spaces)

    @property
    def snake_directions(self):
        """
        Returns the current game model
        """
        return self._snake_directions

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
    def snake(self):
        """
        Returns the current game model
        """
        return self._snake

    @property
    def apples(self):
        """
        Returns the current game model
        """
        return self._apples
