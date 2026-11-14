# Huffman Coding Text Compressor

A Python implementation of **Huffman coding** for lossless text compression and decompression. The project was created for the **Synthesis and Analysis of Algorithms (SAA)** course at TU-Sofia.

The implementation demonstrates frequency analysis, binary-tree construction, custom merge sort, recursive depth-first traversal, and decoding from generated Huffman codes.

## Features

- Counts the frequency of every character in the input.
- Builds a Huffman tree from the frequency table.
- Generates a binary code for each character.
- Compresses text into a string of `0` and `1` bits.
- Decodes compressed text back to the original text.
- Handles the single-character case, such as `aaaaa`.
- Reports the original size, compressed size, and percentage of saved space.
- Validates compressed input during decoding.

## Requirements

- Python 3.8 or newer
- No external dependencies

## Running the program

Clone the repository and run:

```bash
python huffman.py
```

Enter a non-empty text when prompted. The program prints:

1. The generated character-to-code dictionary.
2. The compressed representation.
3. Compression statistics.
4. The decoded text.

Example:

```text
Enter text to compress: hello huffman

--- CODE DICTIONARY ---
' ': ...
'h': ...

--- RESULT ---
Original text: hello huffman
Compressed text: ...

--- ANALYSIS ---
Original size: 104 bits
Compressed size: ... bits
Space saved: ...%

Decoded text: hello huffman
```

The exact codes depend on the character frequencies in the input.

## Using the functions

The main functions can also be imported into another Python program:

```python
from huffman import huffman_encoding, huffman_decoding

text = "hello huffman"
compressed_text, huffman_codes = huffman_encoding(text)
decoded_text = huffman_decoding(compressed_text, huffman_codes)

assert decoded_text == text
```

### `huffman_encoding(text)`

Returns:

- `compressed_text`: the encoded text as a string of `0` and `1`;
- `huffman_codes`: a dictionary mapping each character to its Huffman code.

### `huffman_decoding(compressed_text, huffman_codes)`

Returns the original text by reversing the generated codes. It raises `ValueError` when the compressed input contains characters other than `0` or `1`, or ends with an incomplete code.

## Algorithm and complexity

Let:

- `N` be the length of the input text;
- `K` be the number of unique characters.

The project intentionally uses merge sort instead of a min-heap to meet the algorithm-analysis requirements of the course.

| Operation | Complexity |
| --- | --- |
| Frequency analysis | `O(N)` |
| Initial merge sort | `O(K log K)` |
| Tree construction with repeated sorting | `O(K^2 log K)` |
| Code generation | `O(K)` |
| Encoding | `O(N)` |
| Decoding | `O(N)` |
| **Total encoding complexity** | **`O(N + K^2 log K)`** |

The tree, code dictionary, and frequency data use `O(K)` space. The encoded and decoded text require additional `O(N)` space.

In a production implementation, replacing repeated sorting with a min-heap would reduce tree construction to `O(K log K)`.

## Project structure

```text
.
├── huffman.py   # Huffman tree, encoding, decoding, and command-line interface
└── README.md    # Project documentation
```

## Limitations

- The compressed result is displayed as a string of text bits, not packed into a binary file.
- The code dictionary must be preserved in order to decode the compressed text.
- The command-line program expects a non-empty input string.
