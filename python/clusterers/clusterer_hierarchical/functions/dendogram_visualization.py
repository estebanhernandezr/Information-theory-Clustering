from math import dist
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import numpy as np

"""
    GRAPH VISUALIZATION
"""
def visualize_dendogram(names, distM):
    dists = np.array(distM)
    #dists = squareform(distM)
    print(names)
    print(dists)
    linkage_matrix = linkage(dists, 'complete', optimal_ordering=True)
    dendrogram(linkage_matrix, labels=names, orientation='top', leaf_rotation=90, color_threshold=None)
    plt.title("dendogram")
    plt.tight_layout()
    plt.show()