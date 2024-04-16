class Snake:
    """
    Class to represent a snake

    Attributes:
        locations: Location of all snake segments as a list of lists
        directions: Direction of all snake segments as a list of strings
    """

    _directions_dict = {
        "UP": [-1, 0],
        "DOWN": [1, 0],
        "RIGHT": [0, 1],
        "LEFT": [0, -1],
    }
    _backwards_direction_dict = {
        "UP": "DOWN",
        "DOWN": "UP",
        "RIGHT": "LEFT",
        "LEFT": "RIGHT",
    }

    def __init__(self, head_row, head_col, direction, length):
        """
        Initializes a snake at a location and facing a direction

        Attributes:
            head_row: Integer representing the row location of snake head
            head_col: Integer representing the col location of snake head
            direction: String representing direction the snake is facing
            length: Integer representing the length of the snake
        """
        self._locations = [[head_row, head_col]]
        for i in range(1, length):
            segment_row = (
                self._directions_dict[
                    self._backwards_direction_dict[direction]
                ][0]
                + self._locations[i - 1][0]
            )
            segment_col = (
                self._directions_dict[
                    self._backwards_direction_dict[direction]
                ][1]
                + self._locations[i - 1][1]
            )
            self._locations.append([segment_row, segment_col])

        self._directions = [direction for _ in range(length)]

    def move(self, direction):
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

        if backwards_dict[direction] == self._directions[0]:
            direction = self._directions[0]

        self._locations.pop()

        next_head_row = (
            self._locations[0][0] + self._directions_dict[direction][0]
        )
        next_head_col = (
            self._locations[0][1] + self._directions_dict[direction][1]
        )
        self._locations.insert(0, [next_head_row, next_head_col])

        self._directions.pop()
        self._directions.insert(0, direction)

    def grow(self):
        """
        Grow the snake by 1 length
        """
        backwards_dict = {
            "UP": "DOWN",
            "DOWN": "UP",
            "RIGHT": "LEFT",
            "LEFT": "RIGHT",
        }

        tail_direction = self._directions[-1]
        new_row = (
            self._locations[-1][0]
            + self._directions_dict[backwards_dict[tail_direction]][0]
        )
        new_col = (
            self._locations[-1][1]
            + self._directions_dict[backwards_dict[tail_direction]][1]
        )

        self._locations.append([new_row, new_col])
        self._directions.append(tail_direction)

    @property
    def directions(self):
        """
        Returns the directions of all snake segments as a list of lists
        """
        return self._directions

    @property
    def locations(self):
        """
        Returns the locations of all snake segments as a list of strings
        """
        return self._locations
