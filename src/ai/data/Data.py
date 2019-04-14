import pandas
import numpy


class Data:

    def __init__(self, snake):
        self._data = numpy.array([[0, 0, 0]])
        self._snake = snake

    def collect(self):
        score = self._snake[0].size - 2
        direction = self._snake[0].direction.current_direction

        if score > 50:
            reward = 200
        elif score > 20:
            reward = 100
        elif score > 10:
            reward = 1
        else:
            reward = 0

        self._data = numpy.append(self._data, [[direction, reward, score]], axis=0)

    def save(self):
        if len(self._data) > 0:
            self._data = numpy.delete(self._data, 0, 0)
            data = pandas.DataFrame(self._data, columns=["direction", "reward", "score"])
            data.to_csv('ai/data_set/initial_data.csv', index=False, sep=' ')
