class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


# Sorts in descending order by frequency
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].freq >= right[j].freq:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Recursive code generation
def encode(root, current_code, huffman_codes):
    if root is None:
        return

    # If leaf node
    if root.char is not None:
        huffman_codes[root.char] = current_code

    encode(root.left, current_code + "0", huffman_codes)
    encode(root.right, current_code + "1", huffman_codes)


def huffman_encoding(text):
    # 1. Frequency analysis
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1

    # 2. Create list of nodes
    nodes = [Node(char, freq) for char, freq in freq_map.items()]

    # Edge case: user enters only a single repeated character (e.g. "aaaaa")
    if len(nodes) == 1:
        huffman_codes = {nodes[0].char: "0"}
        print("--- CODE DICTIONARY ---")
        print(f"'{nodes[0].char}': 0")
        print("\n--- RESULT ---")
        print(f"Original text: {text}")
        print(f"Compressed text: {'0' * len(text)}")
        return "0" * len(text), huffman_codes

    # 3. Build the tree
    nodes = merge_sort(nodes)
    while len(nodes) > 1:
        # Extract two lowest frequency nodes (from the back)
        right_node = nodes.pop()
        left_node = nodes.pop()

        # Merge them
        parent = Node(None, left_node.freq + right_node.freq)
        parent.left = left_node
        parent.right = right_node

        nodes.append(parent)
        nodes = merge_sort(nodes)
    root = nodes[0]

    # 4. Generate result
    huffman_codes = {}
    encode(root, "", huffman_codes)

    compressed_text = "".join(huffman_codes[char] for char in text)

    print("\n--- CODE DICTIONARY ---")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")

    print("\n--- RESULT ---")
    print(f"Original text: {text}")
    print(f"Compressed text: {compressed_text}")

    original_size = len(text) * 8
    compressed_size = len(compressed_text)
    compression_ratio = 100 - ((compressed_size / original_size) * 100)

    print("\n--- ANALYSIS ---")
    print(f"Original size: {original_size} bits")
    print(f"Compressed size: {compressed_size} bits")
    print(f"Space saved: {compression_ratio:.2f}%\n")
    return compressed_text, huffman_codes


def huffman_decoding(compressed_text, huffman_codes):
    reversed_codes = {code: char for char, code in huffman_codes.items()}
    decoded_text = []
    current_code = ""

    for bit in compressed_text:
        if bit not in ("0", "1"):
            raise ValueError("Compressed text must contain only 0 and 1.")

        current_code += bit
        if current_code in reversed_codes:
            decoded_text.append(reversed_codes[current_code])
            current_code = ""

    if current_code:
        raise ValueError("Compressed text ends with an incomplete code.")

    return "".join(decoded_text)


if __name__ == "__main__":
    # Dynamic user input
    user_input = input("Enter text to compress: ")
    if user_input:
        compressed_text, huffman_codes = huffman_encoding(user_input)
        decoded_text = huffman_decoding(compressed_text, huffman_codes)
        print(f"Decoded text: {decoded_text}")
    else:
        print("You entered an empty string! Please restart the program and enter valid text.")