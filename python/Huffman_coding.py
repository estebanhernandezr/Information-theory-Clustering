# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 12:17:15 2022

@author: crai-portatil
"""

def print_tree(root, level):
    if root != None:
        print(root.symbol, " | ", root.code)
        for i in range(0, len(root.children)):
            print_tree(root.children[i], level+1)
                        

class node:
    def __init__(self, symbol, code, children):
        self.symbol = symbol
        self.code = code
        self.children = children

class supersymbol:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability

def sort_supersymbols(supersymbols):    
    n = len(supersymbols)
    for i in range(0, n):
        k = i
        j = i-1
        while k > 0 and supersymbols[k].probability > supersymbols[j].probability:
            c = supersymbols[k]
            supersymbols[k] = supersymbols[j]
            supersymbols[j] = c
            k -= 1
            j = k-1
    for a in supersymbols:
        print(a.symbol, ": ", a.probability, end=' | ')
    print()
    return supersymbols

class Huffman_tree:
    A = [supersymbol('A', 0.15), supersymbol('T', 0.15), supersymbol('G', 0.10), supersymbol('U', 0.20), supersymbol('Y', 0.05), supersymbol('X', 0.20), supersymbol('W', 0.15)]
    B = [supersymbol('0', 0.25), supersymbol('1', 0.25), supersymbol('2', 0.25)]
    alpha = len(A)
    beta = len(B)

    def __init__(self):
        self.root = None
        self.Build_Huffman_tree(self.A)

    def Build_Huffman_tree(self, P):
        beta = self.beta
        if len(P) > 1:
            P = sort_supersymbols(P)
            P_ = P[: -beta] + [supersymbol(symbol='super', probability=sum([x.probability for x in P[-beta:]]))]
            root = self.Build_Huffman_tree(P_)
            idx = 0
            for i in range(0, beta):
                root.children.append(
                                        node(
                                            symbol=P[-beta+i].symbol,
                                            code=root.code+self.B[i].symbol,
                                            children=[]
                                            )
                                    )
                if P[-beta+i].symbol == "super":
                    idx = i
            return(root.children[idx])
        else:
            self.root = node(symbol=(P[0].symbol), code="", children=[])
            return(self.root)

raiz = Huffman_tree()
print_tree(raiz.root, 0)
