import pygame
from .constants import WIDTH, HEIGHT, ROBOT_SIZE

class Renderer:
    """Класс для отрисовки игры."""

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def draw(self, game_state):  # Убрали аннотацию типа
        """Отрисовывает текущее состояние игры."""
        self.screen.fill((255, 255, 255))  # Заполняем экран белым цветом

        # Отрисовка роботов
        for robot in game_state.get_all_robots():
            pygame.draw.circle(self.screen, robot.color,
                               (int(robot.position.x), int(robot.position.y)),
                               ROBOT_SIZE)

            # Отрисовка полоски здоровья
            health_bar_width = 30
            health_bar_height = 5
            health_percentage = robot.health / 100
            pygame.draw.rect(self.screen, (255, 0, 0),  # Красный цвет для фона полоски здоровья
                             (int(robot.position.x - health_bar_width/2),
                              int(robot.position.y - ROBOT_SIZE - 10),
                              health_bar_width, health_bar_height))
            pygame.draw.rect(self.screen, (0, 255, 0),  # Зеленый цвет для заполнения полоски здоровья
                             (int(robot.position.x - health_bar_width/2),
                              int(robot.position.y - ROBOT_SIZE - 10),
                              int(health_bar_width * health_percentage), health_bar_height))

        # Здесь можно добавить отрисовку других элементов игры, например, баз

        pygame.display.flip()
