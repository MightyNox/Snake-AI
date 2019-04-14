from game.point.Point import Point
from game.direction.Direction import Direction
from game.exception import SnakeCollisionException, WinException


class Snake:

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def size(self):
        return self._size

    @property
    def step(self):
        return self._step

    @property
    def direction(self):
        return self._direction

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @size.setter
    def size(self, size):
        self._size = size

    @step.setter
    def step(self, step):
        self._step = step

    def __init__(self):
        self._x = [10, 30]
        self._y = [10, 10]
        self._size = 2
        self._step = 20
        self._direction = Direction()

    def move(self, point):
        self._direction.previous_direction = self._direction.current_direction

        for i in range(self.size - 1, 0, -1):
            self._x[i] = self._x[i - 1]
            self._y[i] = self._y[i - 1]

        if self._direction.current_direction == 0:
            self._x[0] = self._x[0] + self._step
        if self._direction.current_direction == 1:
            self._x[0] = self._x[0] - self._step
        if self._direction.current_direction == 2:
            self._y[0] = self._y[0] - self._step
        if self._direction.current_direction == 3:
            self._y[0] = self._y[0] + self._step

        self._x[0] = self._x[0] % 600
        self._y[0] = self._y[0] % 500

        if self.snake_collision():
            raise SnakeCollisionException("Snake is eating himself!")

        self._point_collision(point)

    def _point_collision(self, point):
        if len(point) == 0:
            return

        if self._x[0] == point[0].x and self._y[0] == point[0].y:
            self._x.append(self.x[0])
            self._y.append(self.y[0])
            self._size += 1

            if self._size == 750:
                raise WinException("Snake is sooo loooong!")
            else:
                point[0] = Point(snake=self)

    def snake_collision(self):
        for i in range(self._size - 1, 0, -1):
            if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                return True

        return False
