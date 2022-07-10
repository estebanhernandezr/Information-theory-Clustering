import sys
sys.path.insert(0, 'python/clusterers/clusterer_dimensional/functions')
sys.path.insert(1, 'python/clusterers/clusterer_dimensional')

import numpy as np

from distance_matrix2coordinates import visualize_flat_clustering

class Clusterer:

    def __init__(self):
        self.clusters = None

    def clust(self, labels, distance_matrix):
        visualize_flat_clustering(labels, np.array(distance_matrix))