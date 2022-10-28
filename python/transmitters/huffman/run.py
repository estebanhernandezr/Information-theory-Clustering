import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
import scipy.interpolate as interp
from mpl_toolkits.mplot3d import Axes3D

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
        codificador = Encoder(B_sim)
        arbol_sim = codificador.huffman_code(A_sim_local)
        mean_lenght = mean_codeword_lenght(arbol_sim)
        #print("longitud(",i,"):", mean_lenght)
        mean_codeword_lenghts.append(mean_lenght)
    #print(mean_codeword_lenghts)
    return (mean_codeword_lenghts)

def simulation_dependence(lim, p):
    #matrix = {"W": {"W": 0.6, "B": 0.8, " ": p}, "B": {"W": 0.4, "B": 0.2, " ": 1-p}, " ": {"A": p, "B":1-p}}
    #matrix = {"W": {"W": 0.9, "B": 0.4, " ": p}, "B": {"W": 0.1, "B": 0.6, " ": 1-p}, " ": {"A": p, "B":1-p}}
    matrix = {"W": {"W": 0.5, "B": 0.5, " ": p}, "B": {"W": 0.5, "B": 0.5, " ": 1-p}}
    A_sim = [node('W', p, "", []), node('B', 1-p, "", [])]
    B_sim = [node('0', 0.49, "", []), node('1', 0.21, "", [])]
    mean_codeword_lenghts = []
    for i in range(1, lim):
        A_sim_local = combine_dependence(matrix, node(symbol=" ", probability=1, code="", children=[]), A_sim, i)
        codificador = Encoder(B_sim)
        arbol_sim = codificador.huffman_code(A_sim_local)
        mean_lenght = mean_codeword_lenght(arbol_sim)
        mean_codeword_lenghts.append(mean_lenght)
    return (mean_codeword_lenghts)

def probability_vs_meanlength():
    probas = []
    deltas = []
    ps = np.linspace(0, 1, 100)
    for p in ps:
        A_sim = [node('W', p, "", []), node('B', 1-p, "", [])]
        B_sim = [node('0', 0.49, "", []), node('1', 0.21, "", [])]
        A_sim_local9 = combine_independence(node(symbol="", probability=1, code="", children=[]), A_sim, 8)
        codificador = Encoder(B_sim)
        arbol_sim9 = codificador.huffman_code(A_sim_local9)
        mean_lenght9 = mean_codeword_lenght(arbol_sim9)

        A_sim_local10 = combine_independence(node(symbol="", probability=1, code="", children=[]), A_sim, 9)
        codificador = Encoder(B_sim)
        arbol_sim10 = codificador.huffman_code(A_sim_local10)
        mean_lenght10 = mean_codeword_lenght(arbol_sim10)
        deltas.append(mean_lenght10-mean_lenght9)
        probas.append(p)

    plt.plot(probas, deltas, marker = 'x', markersize = 10)
    plt.show()
    return deltas

def probability_vs_meanlength_dependence():
    probas1 = []
    probas2 = []
    deltas = []
    ps = np.linspace(0.1, 1, 20)
    for pAB in ps:
        for pBA in ps:
            p = pAB/(pBA+pAB)
            A_sim = [node('W', p, "", []), node('B', 1-p, "", [])]
            B_sim = [node('0', 0.49, "", []), node('1', 0.21, "", [])]
            matrix = {"W": {"W": pBA, "B": pAB, " ": p}, "B": {"W": 1-pBA, "B": 1-pAB, " ": 1-p}}
            A_sim_local9 = combine_dependence(matrix, node(symbol=" ", probability=1, code="", children=[]), A_sim, 8)
            codificador = Encoder(B_sim)
            arbol_sim9 = codificador.huffman_code(A_sim_local9)
            mean_lenght9 = mean_codeword_lenght(arbol_sim9)

            A_sim_local10 = combine_dependence(matrix, node(symbol=" ", probability=1, code="", children=[]), A_sim, 9)
            codificador = Encoder(B_sim)
            arbol_sim10 = codificador.huffman_code(A_sim_local10)
            mean_lenght10 = mean_codeword_lenght(arbol_sim10)
            deltas.append(mean_lenght10-mean_lenght9)
            probas1.append(pAB)
            probas2.append(pBA)

    X = probas1
    Y = probas2
    Z = deltas

    plotx,ploty, = np.meshgrid(np.linspace(np.min(X),np.max(X),10),\
                            np.linspace(np.min(Y),np.max(Y),10))
    plotz = interp.griddata((X,Y),Z,(plotx,ploty),method='linear')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(plotx,ploty,plotz,cstride=1,rstride=1,cmap='viridis')  # or 'hot'
    plt.xlabel("p(A|B)")
    plt.ylabel("p(B|A)")
    plt.show()
    return deltas

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

"""
reps = 10
prob = 0.99
Sms_indep = simulation(reps, prob)
Sms_dep = simulation_dependence(reps, prob) #simulation(10)
print(Sms_indep)
print(Sms_dep)

plt.plot([i for i in range(1, len(Sms_indep)+1)], Sms_indep, marker = 'x', markersize = 10)
plt.plot([i for i in range(1, len(Sms_dep)+1)], Sms_dep, marker = 'x', markersize = 10)
plt.plot([i for i in range(1, len(Sms_dep)+1)], [i for i in range(1, len(Sms_dep)+1)], marker = '.', markersize = 5)
plt.legend(['indep','dep','worst'])
plt.ylabel("longitud promedio")
plt.xlabel("Longitud del bloque")
plt.ylim([0, len(Sms_dep)+1])
plt.show()
"""

probability_vs_meanlength_dependence()