import random
import pygame
from typing import List
from .constants import WIDTH, HEIGHT, TEAM_SIZE, BLUE, RED, ROBOT_SIZE, ATTACK_RANGE, GROUPING_DISTANCE
from .entities import Robot
from .utils.vector import Vector2D
from .ai.unsupervised_learning import UnsupervisedAI

class GameState:
    """Класс, представляющий состояние игры."""

    def __init__(self):
        self.blue_team = self._create_team(BLUE, 0, WIDTH // 2)
        self.red_team = self._create_team(RED, WIDTH // 2, WIDTH)
        self.unsupervised_ai = UnsupervisedAI()
        self.game_over = False
        self.winner = None

    def _create_team(self, color: tuple, min_x: int, max_x: int) -> List[Robot]:
        return [self._create_robot(color, min_x, max_x) for _ in range(TEAM_SIZE)]

    def _create_robot(self, color: tuple, min_x: int, max_x: int) -> Robot:
        return Robot(
            Vector2D(random.randint(min_x, max_x), random.randint(0, HEIGHT)),
            color,
            color
        )

    def update(self):
        """Обновляет состояние игры."""
        if self.game_over:
            return

        all_robots = self.blue_team + self.red_team

        # Применяем кластеризацию к роботам
        self.unsupervised_ai.cluster_robots(all_robots)

        # Получаем центры кластеров
        cluster_centers = self.unsupervised_ai.get_cluster_centers()

        for robot in all_robots:
            if robot.is_alive():
                enemies = self.red_team if robot.team == BLUE else self.blue_team
                live_enemies = [enemy for enemy in enemies if enemy.is_alive()]

                if live_enemies:
                    nearest_enemy = min(live_enemies, key=lambda e: (e.position - robot.position).length())
                    distance_to_enemy = (nearest_enemy.position - robot.position).length()

                    if robot.should_retreat():
                        retreat_direction = robot.position - nearest_enemy.position
                        robot.move(retreat_direction)
                    elif distance_to_enemy <= ATTACK_RANGE:
                        robot.attack(nearest_enemy)
                    else:
                        # Группировка с союзниками
                        allies = [ally for ally in all_robots if ally.team == robot.team and ally != robot]
                        nearby_allies = [ally for ally in allies if (ally.position - robot.position).length() <= GROUPING_DISTANCE]

                        if nearby_allies:
                            group_center = sum((ally.position for ally in nearby_allies), robot.position)
                            group_center = group_center / (len(nearby_allies) + 1)
                            move_direction = nearest_enemy.position - group_center
                            robot.move(move_direction)
                        else:
                            robot.move(nearest_enemy.position - robot.position)
                else:
                    center = Vector2D(cluster_centers[robot.cluster][0], cluster_centers[robot.cluster][1])
                    robot.move(center - robot.position)

        self.blue_team = [robot for robot in self.blue_team if robot.is_alive()]
        self.red_team = [robot for robot in self.red_team if robot.is_alive()]

        # Проверка на окончание игры
        if not self.blue_team:
            self.game_over = True
            self.winner = "Красная команда"
        elif not self.red_team:
            self.game_over = True
            self.winner = "Синяя команда"

    def check_collision(self, robot1, robot2):
        distance = (robot1.position - robot2.position).length()
        return distance < ROBOT_SIZE * 2  # Предполагаем, что столкновение происходит, когда роботы касаются друг друга

    def get_all_robots(self):
        """Возвращает список всех роботов."""
        return self.blue_team + self.red_team

    def get_winner_message(self):
        """Возвращает сообщение о победителе."""
        if self.game_over and self.winner:
            return f"Игра окончена! Победила {self.winner}!"
        return ""
