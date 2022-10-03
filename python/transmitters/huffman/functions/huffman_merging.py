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
        liminf = max(0, (len(P)-beta))
        limsup = min(beta, len(P))
        for i in range(0, limsup):
            merge_node.children.append(P[liminf+i])
        P_ = P[: -beta] + [merge_node]
        return(merge(P_, B))
    else:
        root = P[-1]
        return(root)