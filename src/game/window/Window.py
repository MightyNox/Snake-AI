import pygame


class Window:
    __screen = None
    __font = None

    def __init__(self):
        self.__init_pygame()

    def display_elements(self, snake, point):
        self.__refresh()
        self.__print_border()
        self.__display_snake(snake)
        self.__display_point(point)
        self.__display_score(snake.size)

        pygame.display.flip()

    def __display_snake(self, snake):
        for i in range(snake.size):
            pygame.draw.rect(self.__screen, (0, 128, 255), pygame.Rect(snake.x[i], snake.y[i], 20, 20))

    def __display_point(self, point):
        if point:
            pygame.draw.rect(self.__screen, (0, 255, 0), pygame.Rect(point[0].x, point[0].y, 20, 20))

    def __display_score(self, score):
        label = self.__font.render("Score: {}".format(score-2), 1, (255, 255, 0))
        self.__screen.blit(label, (100, 560))

    def __init_pygame(self):
        pygame.init()
        self.__font = pygame.font.SysFont("monospace", 15)
        pygame.display.set_caption('Ssssnake')
        self.__screen = pygame.display.set_mode((620, 610))
        surface = pygame.image.load('../img/snake.png')
        pygame.display.set_icon(surface)

    def __print_border(self):
        pygame.draw.rect(self.__screen, (255, 255, 255), pygame.Rect(5, 5, 610, 510), 2)

    def __refresh(self):
        self.__screen.fill((0, 0, 0))
