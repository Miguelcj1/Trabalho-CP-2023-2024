import matplotlib.pyplot as plt
import numpy as np
import re
import os

##> Script Python que lê os ficheiros da pasta "core_outputs" e constroi automaticamente um gráfico de tempos
##! Apenas funciona em máquinas locais, pois não dá para usar matplotlib no cluster.

OUTPUTS_DIR = "/home/pedro/MEI/CP/core_outputs"

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


def read_core_outputs(directory, func = get_time):
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
mylabel = 'Time elapsed (s)'
y_values = read_core_outputs(OUTPUTS_DIR, get_time) #* 2º argumento configurável

# plt.title('Memory analysis')
# plt.ylabel('Arithmetic intensity (#I/#LCC)')

# plt.title('Instructions analysis')
# plt.ylabel('Instructions (#I)')

# plt.title('LCC analysis')
# plt.ylabel('#LCC') 

plt.title('Execution time analysis')
plt.ylabel('Execution time (s)') 

##>

plt.plot(x_values, y_values, linestyle='--', color='blue', marker='o', markersize=5, label=mylabel)

plt.grid(True, linestyle='-', linewidth=0.9, color='gray', alpha=0.8, axis='both', which='major')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.8, axis='both', which='minor')

plt.xticks(x_values)
plt.gca().set_xticks([0] + x_values, minor=True)

plt.yticks(np.arange(0, 15, 2))
plt.gca().set_yticks(np.arange(0, 15, 1), minor=True)


# Show the plot
plt.legend()
plt.show()
