import sys
sys.path.insert(0, 'python/transmitters/huffman/functions')
sys.path.insert(1, 'python/transmitters/huffman/functions')

def expand(root, B):
    beta = len(B)
    if root.children != []:
        for i in range(0, beta):
            child = root.children[i]
            child.code = root.code + B[i].symbol
            expand(child, B)
    return(root)