# Logistic Map and Shannon Entropy Analysis

This Python script generates and analyzes sequences based on the **Logistic Map**, a popular mathematical model used to describe population dynamics and chaotic systems. The script performs the following tasks:

1. Generates sequences using the Logistic Map for different values of the growth rate parameter (`r`).
2. Converts the sequences into binary sequences based on a dynamic threshold (mean of the sequence).
3. Calculates the Shannon Entropy of the binary sequences to measure the unpredictability.
4. Plots two diagrams:
   - A Bifurcation Diagram to visualize the behavior of the Logistic Map for different r values.
   - A plot of Shannon Entropy vs r to show how entropy varies with the growth rate.

## Formulae

### Logistic Map Formula:

```math
x_{n+1} = r \cdot x_n \cdot (1 - x_n)
```

Where:

- 𝑥𝑛 is the value of the sequence at iteration 𝑛,
- 𝑟 is the growth rate parameter (ranging typically between 1 and 4),
- 𝑥0 is the initial value (often chosen between 0 and 1).

### Shannon Entropy Formula:

Shannon Entropy is used to measure the unpredictability or randomness of a binary sequence. Given by:

```math
H(X) = - \sum_{i} p_i \cdot \log_2(p_i)
```

Where:

- 𝑝𝑖 is the probability of the 𝑖-th distinct value in the binary sequence (0 or 1),
- 𝐻(𝑋) is the entropy of the sequence.

The entropy value provides a measure of how random or unpredictable the sequence is. A high entropy indicates a highly unpredictable sequence, while a low entropy indicates more regularity.
