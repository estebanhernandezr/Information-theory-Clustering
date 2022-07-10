from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt

"""
    GRAPH VISUALIZATION
"""
def visualize_dendogram(names, distM):
    dists = distM
    #dists = squareform(distM)
    linkage_matrix = linkage(dists, 'complete', optimal_ordering=True)
    dendrogram(linkage_matrix, labels=names, orientation='top', leaf_rotation=90, color_threshold=None)
    plt.title("dendogram")
    plt.tight_layout()
    plt.show()