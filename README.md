# Huffman Coding Text Compressor

Text compression tool implementing **Huffman Coding** built for the **"Synthesis and Analysis of Algorithms"** (SAA) course at TU-Sofia.

Combines binary trees, custom sorting, recursion, and frequency analysis for lossless compression.

---

## 🛠️ Key Components

- **Node Class:** Binary tree node holding character, frequency, left, and right pointers.
- **Custom Merge Sort:** Descending-order sort algorithm to easily extract (`pop()`) lowest-frequency nodes.
- **Tree Construction:** Iteratively merges the two lowest-frequency nodes into a parent node until only the root remains.
- **Recursive Encoding (DFS):** Traverses the tree (`left` = `'0'`, `right` = `'1'`) to assign binary codes to leaf nodes.
- **Edge Case Handling:** Safely handles single-character inputs (e.g., `"aaaaa"`).

---

## ⏱️ Complexity Analysis

Let `N` be the total text length and `K` be the number of unique characters.

### Time Complexity

| Step | Operation | Time Complexity |
| :--- | :--- | :--- |
| **1. Frequency Count** | Count character frequencies | `O(N)` |
| **2. Initial Sort** | Sort `K` nodes with Merge Sort | `O(K log K)` |
| **3. Tree Building** | Merge `K` nodes with re-sorting | `O(K^2 log K)` |
| **4. Code Generation** | DFS tree traversal | `O(K)` |
| **5. Compression** | Translate text to binary | `O(N)` |
| **Total Time Complexity** | **`O(N + K^2 log K)`** | |

> **Academic Note:** Using `Min-Heap` yields `O(K log K)`. Custom `Merge Sort` is used here to meet SAA coursework requirements for analyzing dynamic sorting. Since `K <= 256` for ASCII, `K` acts as a constant in practice.

### Space Complexity
- **Dictionaries & Tree Storage:** `O(K)`
- **Compressed Output:** `O(N)`
- **Total Space Complexity:** **`O(N + K)`**

---

## 🚀 How to Run

1. Run the script via terminal:
   ```bash
   python huffman.py
