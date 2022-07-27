import matplotlib.pyplot as plt
import numpy as np
import math
import sympy
import numpy as np
from sklearn.manifold import MDS
from matplotlib import pyplot as plt
import sklearn.datasets as dt
import numpy as np
from sklearn.metrics.pairwise import manhattan_distances, euclidean_distances
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def give_coords(distances):
    """give coordinates of points for which distances given

    coordinates are given relatively. 1st point on origin, 2nd on x-axis, 3rd 
    x-y plane and so on. Maximum n-1 dimentions for which n is the number
    of points

     Args:
        distanes (list): is a n x n, 2d array where distances[i][j] gives the distance 
            from i to j assumed distances[i][j] == distances[j][i]

     Returns:
        numpy.ndarray: cordinates in list form n dim

     Examples:
        >>> a = sympy.sqrt(2)
        >>> distances = [[0,1,1,1,1,1],
                         [1,0,a,a,a,a],
                         [1,a,0,a,a,a],
                         [1,a,a,0,a,a],
                         [1,a,a,a,0,a],
                         [1,a,a,a,a,0]]
        >>> give_coords(distances)
        array([[0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1]], dtype=object)

        >>> give_coords([[0, 3, 4], [3, 0, 5], [4, 5, 0]])
        array([[0, 0],
        [3, 0],
        [0, 4]], dtype=object)        

    """
    distances = np.array(distances)

    n = len(distances)
    X = sympy.symarray('x', (n, n - 1))

    for row in range(n):
        X[row, row:] = [0] * (n - 1 - row)

    for point2 in range(1, n):

        expressions = []

        for point1 in range(point2):
            expression = np.sum((X[point1] - X[point2]) ** 2) 
            expression -= distances[point1,point2] ** 2
            expressions.append(expression)

        X[point2,:point2] = sympy.solve(expressions, list(X[point2,:point2]))[1]

    return X

def visualize_flat_clustering(labels, D):
    X = give_coords(D)
    mds = MDS(random_state=0)
    X_transform = mds.fit_transform(X)
    stress = mds.stress_
    print(X_transform)
    print(stress)
    x, y = X_transform.T

    fig, ax = plt.subplots()
    ax.scatter(x,y)

    for i, txt in enumerate(labels):
        ax.annotate(txt, (x[i], y[i]))

    plt.show()