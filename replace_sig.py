import os
import argparse

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

def main():
    parser = argparse.ArgumentParser(description='Replace empty space in a binary file with a signature.')
    parser.add_argument('-b', '--binary', help='Path to the binary file', required=True)
    parser.add_argument('-s', '--signature', help='Path to the signature file', required=True)

    args = parser.parse_args()

    replace_empty_space(args.binary, args.signature)

if __name__ == '__main__':
    main()
