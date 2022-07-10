import sys
sys.path.insert(0, 'python/clusterers/clusterer_hierarchical/functions')
sys.path.insert(1, 'python/clusterers/clusterer_hierarchical')

from dendogram_visualization import visualize_dendogram
from phylogenetic_tree_visualization import visualize_phylogenetic_tree

class Clusterer:

    def __init__(self):
        self.clusters = None

    def clust(self, labels, distance_matrix):
        visualize_dendogram(labels, distance_matrix)