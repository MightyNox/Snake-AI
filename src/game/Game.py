import pygame
from game.window.Window import Window
from game.snake.Snake import Snake
from game.point.Point import Point


class Game:
    __window = None
    __done = None
    __snake = None
    __point = None
    __clock = None
    __time = None

    def __init__(self):
        self.__window = Window()
        self.__done = False
        self.__snake = Snake()
        self.__point = []
        self.__clock = pygame.time.Clock()
        self.__time = 0

    def start(self):
        while not self.__done:
            self.__calc_time()

            if not self.__point:
                self.__point.append(Point())

            if self.__time >= 200:
                try:
                    self.__snake.move(self.__point)
                except:
                    return False
                self.__time = 0

            self.__handle_event()
            self.__window.display_elements(self.__snake, self.__point)

    def __handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__done = True

        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.__snake.move_right()
        elif keys[pygame.K_LEFT]:
            self.__snake.move_left()
        elif keys[pygame.K_UP]:
            self.__snake.move_up()
        elif keys[pygame.K_DOWN]:
            self.__snake.move_down()

    def __calc_time(self):
        self.__time += self.__clock.get_time()
        self.__clock.tick()
