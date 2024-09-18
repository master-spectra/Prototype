import math

class Vector2D:
    """Класс для работы с двумерными векторами."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def length(self) -> float:
        """Возвращает длину вектора."""
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> 'Vector2D':
        """Возвращает нормализованный вектор."""
        length = self.length()
        if length > 0:
            return Vector2D(self.x / length, self.y / length)
        return Vector2D(0, 0)

    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Vector2D':
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> 'Vector2D':
        if scalar != 0:
            return Vector2D(self.x / scalar, self.y / scalar)
        raise ValueError("Division by zero")

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"
