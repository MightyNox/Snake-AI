class Snake:
    __direction = None
    __prev_direction = None
    __speed = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def size(self):
        return self.__size

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @size.setter
    def size(self, size):
        self.__size = size

    def __init__(self):
        self.x = [10, 30]
        self.y = [10, 10]
        self.size = 2
        self.__speed = 20
        self.__direction = 0
        self.__prev_direction = 0

    def move(self, point):
        self.__prev_direction = self.__direction

        for i in range(self.size - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.__direction == 0:
            self.x[0] = self.x[0] + self.__speed
        if self.__direction == 1:
            self.x[0] = self.x[0] - self.__speed
        if self.__direction == 2:
            self.y[0] = self.y[0] - self.__speed
        if self.__direction == 3:
            self.y[0] = self.y[0] + self.__speed

        self.x[0] = self.x[0] % 600
        self.y[0] = self.y[0] % 500

        self.__snake_collision()
        self.__point_collision(point)

    def move_right(self):
        if self.__prev_direction != 1:
            self.__direction = 0

    def move_left(self):
        if self.__prev_direction != 0:
            self.__direction = 1

    def move_up(self):
        if self.__prev_direction != 3:
            self.__direction = 2

    def move_down(self):
        if self.__prev_direction != 2:
            self.__direction = 3

    def __point_collision(self, point):
        if self.x[0] == point[0].x and self.y[0] == point[0].y:
            self.x.append(self.x[0])
            self.y.append(self.y[0])
            self.size += 1
            del point[0]

    def __snake_collision(self):
        for i in range(self.size - 1, 0, -1):
            if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                raise Exception("Snake is eating himself!")
