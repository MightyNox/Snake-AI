class Direction:

    @property
    def current_direction(self):
        return self._current_direction

    @property
    def previous_direction(self):
        return self._previous_direction

    @current_direction.setter
    def current_direction(self, direction):
        self._current_direction = direction

    @previous_direction.setter
    def previous_direction(self, direction):
        self._previous_direction = direction

    def __init__(self):
        self._current_direction = 0
        self._previous_direction = 0

    def turn_right(self):
        if self._previous_direction != 1:
            self._current_direction = 0

    def turn_left(self):
        if self._previous_direction != 0:
            self._current_direction = 1

    def turn_up(self):
        if self._previous_direction != 3:
            self._current_direction = 2

    def turn_down(self):
        if self._previous_direction != 2:
            self._current_direction = 3
