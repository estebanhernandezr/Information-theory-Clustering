import matplotlib.pyplot as plt
import sys

sys.path.insert(0, 'python/transmitters/huffman/functions')
sys.path.insert(1, 'python/transmitters/huffman/encoder')

from auxiliar_classes import node
from auxiliar_functions import combine_dependence, print_tree
from auxiliar_functions import combine_independence
from auxiliar_functions import mean_codeword_lenght
from Encoder import Encoder


def simulation(lim, p):
    A_sim = [node('W', p, "", []), node('B', 1-p, "", [])]
    B_sim = [node('0', 0.49, "", []), node('1', 0.21, "", [])]
    mean_codeword_lenghts = []
    for i in range(1, lim):
        A_sim_local = combine_independence(node(symbol="", probability=1, code="", children=[]), A_sim, i)
        codificador = Encoder(A_sim)
        arbol_sim = codificador.huffman_code(A_sim_local)
        mean_lenght = mean_codeword_lenght(arbol_sim)
        #print("longitud(",i,"):", mean_lenght)
        mean_codeword_lenghts.append(mean_lenght)
    #print(mean_codeword_lenghts)
    return (mean_codeword_lenghts)

def simulation_dependence(lim, p):
    #matrix = {"W": {"W": 0.6, "B": 0.8, " ": p}, "B": {"W": 0.4, "B": 0.2, " ": 1-p}, " ": {"A": p, "B":1-p}}
    matrix = {"W": {"W": 0.9, "B": 0.4, " ": p}, "B": {"W": 0.1, "B": 0.6, " ": 1-p}, " ": {"A": p, "B":1-p}}
    A_sim = [node('W', p, "", []), node('B', 1-p, "", [])]
    B_sim = [node('0', 0.49, "", []), node('1', 0.21, "", [])]
    mean_codeword_lenghts = []
    for i in range(1, lim):
        A_sim_local = combine_dependence(matrix, node(symbol=" ", probability=1, code="", children=[]), A_sim, i)
        codificador = Encoder(A_sim)
        arbol_sim = codificador.huffman_code(A_sim_local)
        mean_lenght = mean_codeword_lenght(arbol_sim)
        mean_codeword_lenghts.append(mean_lenght)
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

reps = 10
prob = 0.5
Sms_indep = simulation(reps, prob)
Sms_dep = simulation_dependence(reps, prob) #simulation(10)
print(Sms_indep)
print(Sms_dep)

plt.plot([i for i in range(1, len(Sms_indep)+1)], Sms_indep, marker = 'x', markersize = 10)
plt.plot([i for i in range(1, len(Sms_dep)+1)], Sms_dep, marker = 'x', markersize = 10)
plt.plot([i for i in range(1, len(Sms_dep)+1)], [i for i in range(1, len(Sms_dep)+1)], marker = '.', markersize = 5)
plt.legend(['indep','dep','worst'])
plt.ylim([0, len(Sms_dep)+1])
plt.show()