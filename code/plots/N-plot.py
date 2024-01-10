import matplotlib.pyplot as plt
import numpy as np

# plt.plot(x_values, speedup_values, linestyle='--', color='blue', marker='o', markersize=5, label='Execution Time(seconds)')

# plt.plot(x_values, ideal_values, linestyle='--', color='black', marker = 'o', markersize=5, label='Ideal Speed Up')

threadsBlock = [1000, 3000, 5000, 7000, 9000, 11000]
times = [
    2.751,
    4.325,
    6.535,
    9.636,
    14.482,
    20.138,
]

plt.xlabel('Value of N')
plt.ylabel('Execution Time (seconds)')

plt.title('Weak Scalability analysis')

plt.grid(True, linestyle='-', linewidth=0.9, color='gray', alpha=0.8, axis='both', which='major')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.8, axis='both', which='minor')

# plt.xticks(threadsBlock)
plt.plot(threadsBlock, times, linestyle='--', color='blue', marker = 'o', markersize=5, label='Exec. Time')

# plt.xticks(threadsBlock)
# plt.xscale('log', base=2)
plt.xticks(threadsBlock)

plt.yticks(np.arange(0, 21, 2))
plt.gca().set_yticks(np.arange(0, 21, 0.5), minor=True)  # Minor ticks


# Show the plot
plt.show()