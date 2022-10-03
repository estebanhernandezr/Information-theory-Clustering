import sys
sys.path.insert(0, 'python/transmitters/huffman/functions')

from auxiliar_classes import node

def print_tree(root, lvl):
    string = "----"*lvl+">"
    print(root.code, string, root.symbol)
    if root.children != []:
        for i in range(0, len(root.children)):
            child = root.children[i]
            print_tree(child, lvl+1)

def sort_nodes(nodes):    
    n = len(nodes)
    for i in range(0, n):
        k = i
        j = i-1
        while k > 0 and nodes[k].probability > nodes[j].probability:
            c = nodes[k]
            nodes[k] = nodes[j]
            nodes[j] = c
            k -= 1
            j = k-1
    return nodes

def get_pairs(root):
    if root.children == []:
        return([(root.code, root.probability)])
    else:
        pairs = []
        for child in root.children:
            pairs += get_pairs(child)
        return pairs

def combine(combination, conjunto, longitud):
    if longitud == 0:
        return ([combination])
    else:
        combinaciones = []
        for i in conjunto:
            nodo = node(symbol=combination.symbol+i.symbol, probability=combination.probability*i.probability, code="", children=[])
            combinaciones += combine(nodo, conjunto, longitud-1)
        return(combinaciones)

def mean_codeword_lenght(code_tree):
    pairs = get_pairs(code_tree)
    mean_lenght = 0
    for pair in pairs:
        mean_lenght += (len(pair[0])*pair[1])
    return(mean_lenght)