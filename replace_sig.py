import os

def find_signature_size(signature_file):
    with open(signature_file, 'rb') as f:
        signature = f.read()
    return len(signature)

def find_empty_space(binary_file, size):
    with open(binary_file, 'rb') as f:
        binary = f.read()
    
    for i in range(len(binary) - size):
        if binary[i:i+size] == b'\x00' * size:
            return i
    
    return -1

def replace_empty_space(binary_file, signature_file):
    signature_size = find_signature_size(signature_file)
    empty_space_offset = find_empty_space(binary_file, signature_size)
    
    if empty_space_offset == -1:
        print("No empty space of required size found in the binary file.")
        return
    
    with open(signature_file, 'rb') as f:
        signature = f.read()
    
    with open(binary_file, 'r+b') as f:
        f.seek(empty_space_offset)
        f.write(signature)

    print("Signature successfully replaced in the binary file.")

# eplace variables
binary_file_path = 'path/to/binary_file'
signature_file_path = 'path/to/signature_file'
replace_empty_space(binary_file_path, signature_file_path)
