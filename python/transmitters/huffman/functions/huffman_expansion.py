import sys
sys.path.insert(0, 'python/transmitters/huffman/functions')
sys.path.insert(1, 'python/transmitters/huffman/functions')

def expand(root, B):
    for i, child in enumerate(root.children):
        child.code = root.code + B[i].symbol
        expand(child, B)
    return(root)