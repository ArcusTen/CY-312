# 4-bit Encoder Python Script

This Python script converts text from an input file (input.txt) into its 4-bit binary equivalent based on a predefined encoding scheme and outputs the result into a file (binary.txt). The encoding scheme maps characters from 'A' to 'O' (including a space) to their corresponding 4-bit binary values.

The encoding scheme is as follows:

```bash
'A' → 0001
'B' → 0010
'C' → 0011
'D' → 0100
'E' → 0101
'F' → 0110
'G' → 0111
'H' → 1000
'I' → 1001
'J' → 1010
'K' → 1011
'L' → 1100
'M' → 1101
'N' → 1110
'O' → 1111
Space (' ') → 0000
```

## Usage

1. Ensure you have Python 3 installed on your system.
Place your input text in a file named input.txt in the same directory as this script.
2. The script will output the encoded 4-bit binary text to a file named binary.txt in the same directory.

3. If any character in the input file is not in the encoding scheme, the script will notify you and skip the character.

## Disadvantages of Using a 4-Bit Encoder

### Limited Character Set:

A 4-bit encoding scheme can only represent 16 unique values (0 to 15) which severely limits the characters that can be encoded. In this case, only uppercase letters from 'A' to 'O' and a space character are supported. This means any text with characters outside this set (e.g., lowercase letters, punctuation, numbers) would be ignored or cause an error.
