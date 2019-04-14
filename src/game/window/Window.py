import pygame


class Window:

    def __init__(self):
        pygame.init()
        self._font = pygame.font.SysFont("monospace", 15)
        pygame.display.set_caption('Ssssnake')
        self._screen = pygame.display.set_mode((620, 610))
        surface = pygame.image.load('../img/snake.png')
        pygame.display.set_icon(surface)

    def display_elements(self, snake, point):
        self._refresh()
        self._print_border()
        self._display_snake(snake)
        self._display_point(point)
        self._display_score(snake[0].size)

        pygame.display.flip()

    def _display_snake(self, snake):
        for i in range(snake[0].size):
            pygame.draw.rect(self._screen, (0, 128, 255), pygame.Rect(snake[0].x[i], snake[0].y[i], 20, 20))

    def _display_point(self, point):
        if point:
            pygame.draw.rect(self._screen, (0, 255, 0), pygame.Rect(point[0].x, point[0].y, 20, 20))

    def _display_score(self, score):
        label = self._font.render("Score: {}".format(score-2), 1, (255, 255, 0))
        self._screen.blit(label, (100, 560))

    def _print_border(self):
        pygame.draw.rect(self._screen, (255, 255, 255), pygame.Rect(5, 5, 610, 510), 2)

    def _refresh(self):
        self._screen.fill((0, 0, 0))
