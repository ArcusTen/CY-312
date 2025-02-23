# Tent Map and Shannon Entropy Analysis

This Python script generates and analyzes sequences based on the Tent Map, a well-known chaotic map. The script performs the following tasks:

1. Generates sequences using the Tent Map for different values of the growth rate parameter (`r`).

2. Converts the sequences into binary sequences based on a dynamic threshold (mean of the sequence).

3. Calculates the Shannon Entropy of the binary sequences to measure the unpredictability.

4. Plots two diagrams:
   - A **Bifurcation Diagram** to visualize the behavior of the Tent Map for different `r` values.
    - A plot of **Shannon Entropy vs r** to show how entropy varies with the growth rate.