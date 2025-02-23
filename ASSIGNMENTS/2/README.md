# Tent Map and Shannon Entropy Analysis

This Python script generates and analyzes sequences based on the Tent Map, a well-known chaotic map. The script performs the following tasks:

1. **Generate sequences using the Tent Map for different values of the growth rate parameter (`r`)**:
   The Tent Map equation is defined as:

   ```math
   x_{n+1} = \begin{cases} 
   r \cdot x_n & \text{if } x_n < 0.5 \\
   r \cdot (1 - x_n) & \text{if } x_n \geq 0.5
   \end{cases}
   ```

   Where:
   - *xn* is the value of the sequence at step *n*.
   - *r* is the growth rate parameter and it controls the dynamics of the sequence.

1. **Convert the sequences into binary sequences based on a dynamic threshold (mean of the sequence)**:
   The conversion uses the mean *μ* of the sequence as the threshold:

   ```math
   \mu = \frac{1}{N} \sum_{i=1}^{N} x_i
   ```

   Then the sequence is converted to binary as follows:

   ```math
   b_i = \begin{cases} 
   1 & \text{if } x_i > \mu \\
   0 & \text{if } x_i \leq \mu
   \end{cases}
   ```

2. **Calculate the Shannon Entropy of the binary sequences**:
   Shannon Entropy is a measure of the unpredictability or disorder in a sequence. It is calculated using the formula:

   ```math
   H(X) = - \sum_{i=1}^{k} p_i \cdot \log_2(p_i)
   ```

   Where:
   - *pi* is the probability of occurrence of the *i*-th value in the binary sequence.
   - *k* is the number of distinct values in the sequence (in this case, 2: 0 and 1).

3. **Plots**:
   - **Bifurcation Diagram**: This plot visualizes the behavior of the Tent Map for different values of *r*, showing the stable points, periodic cycles, and chaotic behavior.
   - **Shannon Entropy vs r**: This plot shows how the entropy varies with the growth rate *r*, indicating the level of chaos in the system for different parameter values.
