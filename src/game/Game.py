import pygame
from game.window.Window import Window
from game.snake.Snake import Snake
from game.point.Point import Point
from game.control.Control import Control
from ai.data import Data


class Game:

    def __init__(self, mode, speed):
        self._window = Window()
        self._snake = [Snake()]
        self._data = Data(self._snake)
        self._point = [Point(snake=self._snake[0])]
        self._control = Control(mode=mode, snake=self._snake, point=self._point)
        self._clock = pygame.time.Clock()
        self._mode = mode
        self._speed = speed
        self._time = 0
        self._done = False

    def start(self):

        while not self._done:
            try:
                self._game_body()
            except Exception as exception:
                if self._mode == "user":
                    print(exception)
                    self._done = True
                elif self._mode == "bot":
                    print("score={}".format(self._snake[0].size))
                    self._snake[0] = Snake()

        self._data.save()

    def _game_body(self):
        self._calc_time()

        if self._time >= self._speed:
            self._data.collect()
            self._snake[0].move(self._point)
            self._time = 0

        self._handle_event()
        self._window.display_elements(self._snake, self._point)

    def _handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._done = True

        self._control.manage()

    def _calc_time(self):
        self._time += self._clock.get_time()
        self._clock.tick()
