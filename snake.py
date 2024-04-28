"""
Class to represent and control a snake for the game snake
"""


class Snake:
    """
    Class to represent a snake

    Attributes:
        locations: Location of all snake segments as a list of lists of ints
        directions: Direction of all snake segments as a list of strings
        apples_eaten: Number of apples eaten as an integer
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

    def __init__(
        self,
        head_location,
        direction,
        length,
        locations_and_directions=None,
    ):
        """
        Initializes a snake with head location and direction or with coords

        If directions and locations are specified it will initialize only
        using those specific coordinates and directions. If they are None,
        it will initialize based on the location of the head and direction
        the snake is facing.

        Parameters:
            head_location: list of two integers for row and col of head
            direction: String representing direction the snake is facing
            length: Integer greater than 0 representing the length of the snake
            locations_and_directions: List of lists with the first list being a
              list of lists of int with coordinates of segments and the second
                a list of strings of directions of segments
        """
        self._apples_eaten = 0
        if locations_and_directions is None:
            locations = None
            directions = None
        else:
            locations = locations_and_directions[0]
            directions = locations_and_directions[1]
        if directions is None and locations is None:
            self._locations = [[head_location[0], head_location[1]]]
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

        else:
            self._locations = []
            self._directions = []
            for loc in locations:
                self._locations.append(loc)
            for direct in directions:
                self._directions.append(direct)

    def move(self, direction):
        """
        Advance the snake in the indicated direction

        Attributes:
            direction: String which direction for head to move in
        """

        if self._backwards_direction_dict[direction] == self._directions[0]:
            direction = self._directions[0]

        next_head_row = (
            self._locations[0][0] + self._directions_dict[direction][0]
        )
        next_head_col = (
            self._locations[0][1] + self._directions_dict[direction][1]
        )
        self._locations.insert(0, [next_head_row, next_head_col])
        self._locations.pop()
        self._directions.insert(0, direction)
        self._directions.pop()

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
        self._apples_eaten += 1

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

    @property
    def apples_eaten(self):
        """
        Returns the number of apples eaten by the snake as an integer
        """
        return self._apples_eaten
