import pygame
import random
import copy
from game.exception import SnakeCollisionException


class Control:

    def __init__(self, mode, snake, point):
        self._mode = mode
        self._snake = snake
        self._point = point

    def manage(self):
        if self._mode == "user":
            self._user_control()
        elif self._mode == "bot":
            self._data_control()

    def _user_control(self):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self._snake[0].direction.turn_right()
        elif keys[pygame.K_LEFT]:
            self._snake[0].direction.turn_left()
        elif keys[pygame.K_UP]:
            self._snake[0].direction.turn_up()
        elif keys[pygame.K_DOWN]:
            self._snake[0].direction.turn_down()

    def _data_control(self):
        """ look for point """
        direction = 0
        if self._snake[0].x[0] < self._point[0].x:
            direction = 0
        elif self._snake[0].x[0] > self._point[0].x:
            direction = 1
        elif self._snake[0].y[0] < self._point[0].y:
            direction = 3
        elif self._snake[0].y[0] > self._point[0].y:
            direction = 2

        """ one step in the future """
        snake_copy = copy.deepcopy(self._snake[0])
        snake_copy.direction.current_direction = direction
        new_direction = 0
        if direction == 0:
            snake_copy.direction.turn_right()
            new_direction = random.randint(2, 3)
        elif direction == 1:
            snake_copy.direction.turn_left()
            new_direction = random.randint(2, 3)
        elif direction == 2:
            snake_copy.direction.turn_up()
            new_direction = random.randint(0, 1)
        elif direction == 3:
            snake_copy.direction.turn_down()
            new_direction = random.randint(0, 1)

        try:
            snake_copy.move([])
        except SnakeCollisionException:
            direction = new_direction

        if direction == 0:
            self._snake[0].direction.turn_right()
        elif direction == 1:
            self._snake[0].direction.turn_left()
        elif direction == 2:
            self._snake[0].direction.turn_up()
        elif direction == 3:
            self._snake[0].direction.turn_down()
