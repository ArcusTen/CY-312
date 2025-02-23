import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math

def tent_map(r, x0, n):
    """
    Generate sequence using the tent map.
    
    Args:
        r (float): Growth rate parameter
        x0 (float): Initial value
        n (int): Number of iterations
    
    Returns:
        list: Sequence of values (transient removed)
    """
    x = [x0]
    for i in range(n - 1):
        if x[-1] < 0.5:
            x.append(r * x[-1])
        else:
            x.append(r * (1 - x[-1]))
    return x

def toBinary(sequence):
    """
    Convert sequence to binary based on dynamic threshold.
    
    Args:
        sequence (list): Input sequence
    
    Returns:
        list: Binary sequence
    """
    threshold = np.mean(sequence)  # Dynamic threshold based on data
    return [1 if x > threshold else 0 for x in sequence]

def shannon_entropy(binary_sequence):
    """
    Calculate Shannon entropy of binary sequence.
    
    Args:
        binary_sequence (list): Binary sequence
    
    Returns:
        float: Shannon entropy value
    """
    counter = Counter(binary_sequence)
    length = len(binary_sequence)
    probabilities = [count / length for count in counter.values()]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

# Parameters
r_values = np.linspace(1, 2.0, 1000)  # Tent map r ranges from 0 to 2
x0 = 0.7
n_iterations = 2000

# diagram
plt.style.use('default')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Tent Map Analysis')

# Plot bifurcation diagram
for r in r_values:
    sequence = tent_map(r, x0, n_iterations)
    ax1.plot([r] * len(sequence), sequence, ',k', alpha=0.1, markersize=0.1)

ax1.set_xlabel('r parameter')
ax1.set_ylabel('Values')
ax1.set_title('Bifurcation Diagram')

# Plot entropy vs r parameter
entropy_values = []
for r in r_values:
    sequence = tent_map(r, x0, n_iterations)
    binary_sequence = toBinary(sequence[-300:])  # Using last 300 points
    entropy = shannon_entropy(binary_sequence)
    entropy_values.append(entropy)

ax2.plot(r_values, entropy_values, 'b-', linewidth=1)
ax2.set_xlabel('r parameter')
ax2.set_ylabel('Shannon Entropy')
ax2.set_title('Shannon Entropy vs r Parameter')

plt.tight_layout()
plt.savefig('tent_map_analysis.png')
plt.show()