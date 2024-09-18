import numpy as np
from sklearn.cluster import KMeans
from typing import List
from .entities import Robot

class AI:
    """Класс для реализации искусственного интеллекта."""

    def __init__(self):
        self.kmeans = KMeans(n_clusters=2)

    def cluster_robots(self, robots: List[Robot]):
        """Кластеризует роботов с помощью алгоритма K-means."""
        positions = np.array([[robot.position.x, robot.position.y] for robot in robots])
        self.kmeans.fit(positions)
        # Здесь можно добавить логику использования результатов кластеризации
