import matplotlib.pyplot as plt
import numpy as np
import re
import os

##> Script Python que lê os ficheiros da pasta "core_outputs" e constroi automaticamente um gráfico relativamente a um certo valor do ficheiro de output.
##! Apenas funciona em máquinas locais, pois não dá para usar matplotlib no cluster.


def get_i_lcc(filename):
    """
    Retorna a intensidade aritmetica obtida através de #I/#LCC do ficheiro passado como argumento
    """
    instructions = 0
    lcc = 0
    with open(filename, 'r') as f:
        for line in f:
            matchi = re.search(r'(\d+)\s+instructions', line)
            matchlcc = re.search(r'(\d+)\s+LLC-loads', line)
            if matchi:
                instructions = int(matchi.group(1))
            elif matchlcc:
                lcc = int(matchlcc.group(1))
    print("Ficheiro:", filename, "->", instructions, "instructions,", lcc, "LLC-loads")
    intensity = instructions / lcc
    intensity = round(intensity, 2)
    print("Intensidade aritmética:", intensity, "\n")
    return intensity

def get_i(filename):
    """
    Retorna o #I do ficheiro passado como argumento
    """
    instructions = 0
    with open(filename, 'r') as f:
        for line in f:
            matchi = re.search(r'(\d+)\s+instructions', line)
            if matchi:
                instructions = int(matchi.group(1))
    print("Ficheiro:", filename, "->", instructions, "instructions\n")
    return instructions

def get_lcc(filename):
    """
    Retorna o #LCC do ficheiro passado como argumento
    """

    lcc = 0
    with open(filename, 'r') as f:
        for line in f:
            matchlcc = re.search(r'(\d+)\s+LLC-loads', line)
            if matchlcc:
                lcc = int(matchlcc.group(1))
    print("Ficheiro:", filename, "->", lcc, "LLC-loads\n")
    return lcc




def read_core_outputs(directory="core_outputs", func = get_i_lcc):
    """
    Returns a list of values that "func" returns, from the core outputs, ordered by the number of cores crescently

    Parameters:
    - directory (str): directory where the core outputs are stored
    - func (function): function to apply on the core_output file that receives a filename and returns a value

    Returns:
    values (list): list of values returned by "func"
    """
    values = []
    files = os.listdir(directory)
    files = sorted(files, key=lambda x: int(x.split("_")[1]))

    for f in files:
        v = func(directory + "/" + f)
        values.append(v)
    return values



#> MAIN

# Number of cores
x_values = list(np.arange(4, 41, 4)) #(start, end, step)
plt.xlabel('CORES')

#* Configuravéis
y_values = read_core_outputs("core_outputs", get_lcc) #* 2º argumento configurável

# plt.title('Memory analysis')
# plt.ylabel('Arithmetic intensity (#I/#LCC)')

# plt.title('Instructions analysis')
# plt.ylabel('Instructions (#I)')

plt.title('LCC analysis')
plt.ylabel('#LCC') 

mylabel = '#LCC'
##*

plt.plot(x_values, y_values, linestyle='--', color='blue', marker='o', markersize=5, label=mylabel)

plt.grid(True, linestyle='-', linewidth=0.9, color='gray', alpha=0.8, axis='both', which='major')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.8, axis='both', which='minor')

plt.xticks(x_values)
plt.gca().set_xticks([0] + x_values, minor=True)


# Show the plot
plt.legend()
plt.show()
