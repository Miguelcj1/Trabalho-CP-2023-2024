import matplotlib.pyplot as plt
import numpy as np
import re
import os

##> Script Python que lê os ficheiros da pasta "core_outputs" e constroi automaticamente um gráfico relativamente a um certo valor do ficheiro de output.
##! Apenas funciona em máquinas locais, pois não dá para usar matplotlib no cluster.

# OUTPUTS_DIR = "/home/pedro/MEI/CP/Trabalho-CP-2023-2024/code/core_outputs"
OUTPUTS_DIR = "/home/pedro/MEI/CP/core_outputs"

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

def get_time(filename):
    """
    Retorna o tempo em segundos do ficheiro passado como argumento
    """
    with open(filename, 'r') as f:
        for line in f:
            match = re.search(r'(\d+(?:\,|\.)\d+) seconds time elapsed', line)
            if match:
                return float(match.group(1).replace(',', '.'))
    print("Ocorreu um problema!!!")
    return 0

def get_cpi(filename):
    """
    Retorna a intensidade aritmetica obtida através de #I/#LCC do ficheiro passado como argumento
    """
    instructions = 0
    cycles = 0
    with open(filename, 'r') as f:
        for line in f:
            matchi = re.search(r'(\d+)\s+instructions', line)
            matchCycles = re.search(r'(\d+)\s+cycles', line)
            if matchi:
                instructions = int(matchi.group(1))
            elif matchCycles:
                cycles = int(matchCycles.group(1))
    print("Ficheiro:", filename, "->", instructions, "instructions,", cycles, "cycles")
    cpi = cycles / instructions
    cpi = round(cpi, 3)
    print("CPI:", cpi, "\n")
    return cpi


def read_core_outputs(directory, func):
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


#! MAIN

# Number of cores
x_values = list(np.arange(4, 41, 4)) #(start, end, step)
plt.xlabel('CORES')


#> Configuravéis
y_values = read_core_outputs(OUTPUTS_DIR, get_cpi) #> 2º argumento configurável

# plt.title('Memory analysis')
# plt.ylabel('Arithmetic intensity (#I/#LCC)')

# plt.title('Instructions analysis')
# plt.ylabel('Instructions (#I)')

# plt.title('LCC analysis')
# plt.ylabel('#LCC') 

# plt.title('Time elapsed')
# plt.ylabel('Execution time (s)') 

plt.title('CPI analysis')
plt.ylabel('CPI') 

##>

plt.plot(x_values, y_values, linestyle='--', color='blue', marker='o', markersize=5)

plt.grid(True, linestyle='-', linewidth=0.9, color='gray', alpha=0.8, axis='both', which='major')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.8, axis='both', which='minor')

plt.xticks(x_values)
plt.gca().set_xticks([0] + x_values, minor=True)


# Show the plot
# plt.legend()
plt.show()
