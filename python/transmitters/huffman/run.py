import matplotlib.pyplot as plt
import sys

sys.path.insert(0, 'python/transmitters/huffman/functions')
sys.path.insert(1, 'python/transmitters/huffman/encoder')

from auxiliar_classes import node
from auxiliar_functions import print_tree
from auxiliar_functions import combine
from auxiliar_functions import mean_codeword_lenght
from Encoder import Encoder


def simulation(lim):
    p = 0.7
    A_sim = [node('W', p, "", []), node('B', 1-p, "", [])]
    B_sim = [node('0', 0.49, "", []), node('1', 0.21, "", [])]
    mean_codeword_lenghts = []
    for i in range(1, lim):
        A_sim_local = combine(node(symbol="", probability=1, code="", children=[]), A_sim, i)
        codificador = Encoder(A_sim)
        arbol_sim = codificador.huffman_code(A_sim_local)
        mean_lenght = mean_codeword_lenght(arbol_sim)
        #print("longitud(",i,"):", mean_lenght)
        mean_codeword_lenghts.append(mean_lenght)
    #print(mean_codeword_lenghts)
    return (mean_codeword_lenghts)

#A = [node('WW', 0.49, "", []), node('WB', 0.21, "", []), node('BW', 0.21, "", []), node('BB', 0.09, "", [])]
A = [node('-', 0.05, "", []), node('C', 0.05, "", []), node('I', 0.05, "", []), node('M', 0.05, "", []), node('N', 0.05, "", []), node('P', 0.05, "", []), node('R', 0.05, "", []), node('E', 0.10, "", []), node('L', 0.10, "", []), node('O', 0.15, "", []), node('S', 0.30, "", [])]
#A = [node('WW', 0.25, "", []), node('WB', 0.25, "", []), node('BW', 0.25, "", []), node('BB', 0.25, "", [])]
#A = [node('WW', 1, "", []), node('WB', 0, "", []), node('BW', 0, "", []), node('BB', 0, "", [])]
#A = [node('WWW', 0.343, "", []), node('WWB', 0.147, "", []), node('WBW', 0.147, "", []), node('BWW', 0.147, "", []), node('WBB', 0.063, "", []), node('BWB', 0.063, "", []), node('BBW', 0.063, "", []), node('BBB', 0.027, "", [])]
#A = [node('W', 0.50, "", []), node('B', 0.50, "", [])]

B = [node('0', 0.5, "", []), node('1', 0.5, "", []), node('2', 0.5, "", []), node('3', 0.5, "", [])]

alpha = len(A)
print("alpha:", alpha)
beta = len(B)

codificador = Encoder(B)
arbol = codificador.huffman_code(A)
print_tree(arbol, 0)

#Sms = simulation(10)
#print(Sms)

#plt.plot([i for i in range(1, len(Sms)+1)], Sms, marker = 'x', markersize = 10)
#plt.plot([i for i in range(1, len(Sms)+1)], [i for i in range(1, len(Sms)+1)], marker = '.', markersize = 5)
#plt.ylim([0, len(Sms)+1])
#plt.show()