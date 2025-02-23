#!/usr/bin/env python3 


encodingScheme = {
    'A': '0001', 
    'B': '0010', 
    'C': '0011', 
    'D': '0100',
    'E': '0101', 
    'F': '0110', 
    'G': '0111', 
    'H': '1000',
    'I': '1001', 
    'J': '1010', 
    'K': '1011', 
    'L': '1100',
    'M': '1101', 
    'N': '1110', 
    'O': '1111', 
    ' ': '0000'  # Space
}

inpFilename = "input.txt"
outFilename = "binary.txt"


''' MAIN '''
try:
    with open(inpFilename, "r") as file:
        text = file.read().strip().upper()  # Convert to uppercase for consistency

    ''' Convert text into 4-bit binary '''
    binaryOutput = []
    for char in text:
        if char in encodingScheme:
            binaryOutput.append(encodingScheme[char])
        else:
            print(f"[!] Character '{char}' is not in the encoding scheme and will be skipped...")

    ''' joining binary values into a string '''
    binaryStr = ' '.join(binaryOutput)

    # Write to binary.txt
    with open(outFilename, "w") as binary_file:
        binary_file.write(binaryStr)

    # Print the binary output
    print("Encoded Binary Output:")
    print(binaryStr)

except FileNotFoundError:
    print("Error: input.txt file not found.")

