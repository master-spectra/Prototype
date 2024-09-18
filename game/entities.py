from .utils.vector import Vector2D
from .constants import MAX_HEALTH, DAMAGE, MOVEMENT_SPEED, RETREAT_HEALTH

class Robot:
    """Класс, представляющий робота в игре."""

    def __init__(self, position: Vector2D, color: tuple, team):
        self.position = position
        self.color = color
        self.team = team
        self.health = MAX_HEALTH
        self.damage = DAMAGE
        self.target = None
        self.cluster = None  # Добавляем атрибут для хранения метки кластера

    def move(self, direction: Vector2D):
        """Перемещает робота в направлении цели."""
        if direction.length() > 0:
            self.position += direction.normalize() * MOVEMENT_SPEED

    def attack(self, target: 'Robot'):
        """Атакует цель."""
        target.take_damage(self.damage)

    def take_damage(self, amount):
        """Метод для получения урона."""
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            # Здесь можно добавить логику уничтожения робота

    def is_alive(self) -> bool:
        """Проверяет, жив ли робот."""
        return self.health > 0

    def should_retreat(self) -> bool:
        """Проверяет, следует ли роботу отступать."""
        return self.health <= RETREAT_HEALTH
