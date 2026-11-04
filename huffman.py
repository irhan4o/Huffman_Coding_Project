class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


# Сортира низходящо по честота
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

    # Добавяне на останалите елементи
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Рекурсивно генериране на кодовете
def encode(root, current_code, huffman_codes):
    if root is None:
        return

    # Ако е листо
    if root.char is not None:
        huffman_codes[root.char] = current_code

    encode(root.left, current_code + "0", huffman_codes)
    encode(root.right, current_code + "1", huffman_codes)


def huffman_encoding(text):
    # 1. Честотен анализ
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1

    #2 Създаване на списък от възли
    nodes = [Node(char, freq) for char, freq in freq_map.items()]

    # Справяне с граничен случай: ако потребителят въведе само един повтарящ се символ (напр. "aaaaa")
    if len(nodes) == 1:
        print("--- РЕЧНИК НА КОДОВЕТЕ ---")
        print(f"'{nodes[0].char}': 0")
        print("\n--- РЕЗУЛТАТ ---")
        print(f"Оригинален текст: {text}")
        print(f"Компресиран текст: {'0' * len(text)}")
        return

    # 3. Изграждане на дървото
    nodes = merge_sort(nodes)
    while len(nodes) > 1:
        # Взимаме двата възела с най-малката честота (най-отзад)
        right_node = nodes.pop()
        left_node = nodes.pop()

        # Сливаме ги
        parent = Node(None, left_node.freq + right_node.freq)
        parent.left = left_node
        parent.right = right_node

        nodes.append(parent)
        nodes = merge_sort(nodes)
    root = nodes[0]

    # 4. Генериране на резултата
    huffman_codes = {}
    encode(root, "", huffman_codes)

    compressed_text = "".join(huffman_codes[char] for char in text)

    print("\n--- РЕЧНИК НА КОДОВЕТЕ ---")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")

    print("\n--- РЕЗУЛТАТ ---")
    print(f"Оригинален текст: {text}")
    print(f"Компресиран текст: {compressed_text}")

    original_size = len(text) * 8
    compressed_size = len(compressed_text)
    compression_ratio = 100 - ((compressed_size / original_size) * 100)

    print("\n--- АНАЛИЗ ---")
    print(f"Оригинален размер: {original_size} бита")
    print(f"Компресиран размер: {compressed_size} бита")
    print(f"Спестено пространство: {compression_ratio:.2f}%\n")

if __name__ == "__main__":
    # Динамично въвеждане на текст от потребителя
    user_input = input("Въведете текст за компресиране: ")
    if user_input:
        huffman_encoding(user_input)
    else:
        print("Въведохте празен низ! Моля, стартирайте програмата отново и въведете текст.")



        