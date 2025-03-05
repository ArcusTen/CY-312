import textwrap
import permutations
# import helperfunc

def text_to_64bit_binary(text):
    # Convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    
    if len(binary_text) > 64:
        print("Input text is too long to fit in 64 bits. Please shorten the input.")
        exit(1)
    
    # padding to 64 bits (if needed)
    binary_text = binary_text.zfill(64)
    return binary_text

def process_block(block):
    ''' Apply initial permutation '''
    block = permutations.permutation(block, "initial")
    
    # splitting into 32-bit chunks '
    lpt, rpt = block[:32], block[32:]
    
    ''' applying expansion permutation to the right part '''
    rpt = permutations.permutation(rpt, "expansion")

    # applying S-boxes
    rpt = permutations.sBox_permutation(rpt)
    # combining the left & right parts
    result = lpt + rpt
    return result

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        text = file.readline().strip()
    print(f"[!] INPUT TEXT: {text}")
    
    try:
        binary_text = text_to_64bit_binary(text)
    except ValueError as e:
        print(e)
        exit(1)
    
    processed_text = process_block(binary_text)
    print(f"[!] PROCESSED TEXT: {processed_text}")
    
    with open('output.txt', 'w') as file:
        file.write(processed_text)
    
    print(f"[!] OUTPUT TEXT: {processed_text}")