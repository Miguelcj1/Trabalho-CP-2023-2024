import matplotlib.pyplot as plt
import numpy as np
import re
import os

##> Script Python que lê os ficheiros da pasta "core_outputs" e constroi automaticamente um gráfico de speedup com os resultados
##! Apenas funciona em máquinas locais, pois não dá para usar matplotlib no cluster.

# Constants
SEQ_TIME = 23.1639

def speedup(time):
    return SEQ_TIME / time

def get_seconds_from(filename):
    with open(filename, 'r') as f:
        for line in f:
            match = re.search(r'(\d+\,\d+) seconds time elapsed', line)
            if match:
                return float(match.group(1).replace(',', '.'))
    print("Ocorreu um problema!!!")
    return 0


def read_core_outputs(directory="core_outputs"):
    """
    Returns a list of times in seconds from the core outputs, ordered by the number of cores crescently

    Parameters:
    - directory (str): directory where the core outputs are stored

    Returns:
    times (list): list of times in seconds
    """
    times = []
    files = os.listdir(directory)
    files = sorted(files, key=lambda x: int(x.split("_")[1]))
    print(files)

    for f in files:
        time = get_seconds_from(directory + "/" + f)
        times.append(time)
    print(times)
    return times




x_values = list(np.arange(4, 41, 4)) #(start, end, step)
y_values = read_core_outputs("core_outputs")
"""
y_values = [
    11.83711492, # 4 cores
    7.79823345,  # 8 cores
    4.429618154, # 12 cores
    3.329742445, # 16 cores
    3.264248948, # 20 cores
    3.094146565, # 24 cores
    2.894629863, # 28 cores
    2.486358823, # 32 cores
    2.227191343, # 36 cores
    2.093691082, # 40 cores
]
"""

ideal_values = [4, 8, 12, 16, 20, 20, 20, 20, 20, 20]

speedup_values = []
for y in y_values:
    speedup_values.append(speedup(y))

plt.plot(x_values, speedup_values, linestyle='--', color='blue', marker='o', markersize=5, label='Speed Up')

plt.plot(x_values, ideal_values, linestyle=':', color='black', marker = 'o', markersize=5, label='Ideal Speed Up')

plt.xlabel('CORES')
plt.ylabel('Speed Up')

plt.title('CP')

plt.grid(True, linestyle='-', linewidth=0.9, color='gray', alpha=0.8, axis='both', which='major')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.8, axis='both', which='minor')

plt.xticks(x_values)
plt.gca().set_xticks([0] + x_values, minor=True)  # Minor ticks

plt.yticks(np.arange(0, max(ideal_values) + 2, 2))
plt.gca().set_yticks(np.arange(0, max(ideal_values) + 2, 0.4), minor=True)  # Minor ticks


# Show the plot
plt.legend()
plt.show()
