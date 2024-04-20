import random


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
        self._snake = []
        for i in range(self._snake_starting_length):
            self._snake.append(
                [self._board_height // 2, 1 + self._snake_starting_length - i]
            )

        self._snake_directions = [
            "RIGHT" for _ in range(self._snake_starting_length)
        ]

        self._apples = []
        for i in range(1, self._num_apples + 1):
            self._apples.append(
                [
                    i * (self._board_height // (self._num_apples + 1)),
                    self.board_width - 2,
                ]
            )

    def move_snake(self, direction):
        """
        Advance the snake in the indicated direction

        Attributes:
            direction: String which direction for head to move in

        Returns:
            Boolean representing if valid move
        """

        backwards_dict = {
            "UP": "DOWN",
            "DOWN": "UP",
            "RIGHT": "LEFT",
            "LEFT": "RIGHT",
        }
        move_dict = {
            "UP": [-1, 0],
            "DOWN": [1, 0],
            "RIGHT": [0, 1],
            "LEFT": [0, -1],
        }

        if backwards_dict[direction] == self._snake_directions[0]:
            direction = self._snake_directions[0]

        self._snake.pop()

        next_head_row = self._snake[0][0] + move_dict[direction][0]
        next_head_col = self._snake[0][1] + move_dict[direction][1]
        self._snake.insert(0, [next_head_row, next_head_col])

        self._snake_directions.pop()
        self._snake_directions.insert(0, direction)
        self._check_and_eat()

        return self._snake_collision()

    def _grow_snake(self):
        """
        Grow the snake by 1 length
        """
        backwards_dict = {
            "UP": "DOWN",
            "DOWN": "UP",
            "RIGHT": "LEFT",
            "LEFT": "RIGHT",
        }
        move_dict = {
            "UP": [-1, 0],
            "DOWN": [1, 0],
            "RIGHT": [0, 1],
            "LEFT": [0, -1],
        }
        tail_direction = self._snake_directions[-1]
        new_row = (
            self._snake[-1][0] + move_dict[backwards_dict[tail_direction]][0]
        )
        new_col = (
            self._snake[-1][1] + move_dict[backwards_dict[tail_direction]][1]
        )

        self._snake.append([new_row, new_col])
        self._snake_directions.append(tail_direction)

    def _snake_collision(self):
        """
        Checks if the snakes position is valid

        Returns:
            Boolean for if snake has collided with something
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
        Checks if the snake is eating and if so grows and gnerates new apple
        """
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
