import random


class Point:

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __init__(self, snake):
        while True:
            outside_of_snake = True

            self._x = random.randint(1, 30) * 20 - 10
            self._y = random.randint(1, 25) * 20 - 10

            for i in range(snake.size-1, 0, -1):
                if self._x == snake.x[i] and self._y == snake.y[i]:
                    outside_of_snake = False
                    break

            if outside_of_snake:
                break
