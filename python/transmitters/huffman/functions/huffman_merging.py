import sys
sys.path.insert(0, 'python/transmitters/huffman/functions')

from auxiliar_functions import print_tree
from auxiliar_functions import sort_nodes
from auxiliar_classes import node

def merge(P, B):
    beta = len(B)
    if len(P) > 1:
        P  = sort_nodes(P)
        merge_node = node(symbol="super", probability=sum([x.probability for x in P[-beta:]]), code="", children=[])
        for i in range(0, beta):
            merge_node.children.append(P[-beta+i])
        P_ = P[: -beta] + [merge_node]
        return(merge(P_, B))
    else:
        root = P[-1]
        return(root)