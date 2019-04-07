import random


class Point:

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __init__(self):
        self.__x = random.randint(1, 30) * 20 - 10
        self.__y = random.randint(1, 25) * 20 - 10
