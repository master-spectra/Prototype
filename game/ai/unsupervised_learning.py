import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class UnsupervisedAI:
    def __init__(self, n_clusters=3):
        self.kmeans = KMeans(n_clusters=n_clusters)
        self.scaler = StandardScaler()

    def cluster_robots(self, robots):
        features = np.array([[r.position.x, r.position.y, r.health] for r in robots])
        scaled_features = self.scaler.fit_transform(features)
        labels = self.kmeans.fit_predict(scaled_features)

        for robot, label in zip(robots, labels):
            robot.cluster = label

    def get_cluster_centers(self):
        return self.scaler.inverse_transform(self.kmeans.cluster_centers_)
