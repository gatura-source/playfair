# **Playfair Cipher Implementation in Python**

This project implements the Playfair cipher, a classical encryption technique, in Python. The code includes helper functions and a `Playfair` class to encrypt plaintext using a keyword.

---

## **Features**
1. **Key Features**:
   - Removes spaces in the plaintext.
   - Handles repeated letters by inserting a filler (`X`).
   - Constructs a 5x5 Playfair matrix using the keyword.
   - Encrypts plaintext based on the Playfair cipher rules.

2. **Helper Functions**:
   - `create_diagraph(inp)`: Splits the input into digraphs (pairs of characters).
   - `checkduplicate(string)`: Ensures no duplicate characters appear consecutively in the plaintext.

---

## **Class Details**
### **Playfair Class**
The main class encapsulates the Playfair cipher functionality.

### **Methods**:
- **`__init__(self, keyword, plaintext)`**:
  Initializes the object with a keyword and plaintext.

- **`rm_spaces(self)`**:
  Removes spaces from the plaintext.

- **`create_table(self)`**:
  Generates a 5x5 Playfair matrix using the keyword.

- **`search_matrix(self, matrix, element)`**:
  Finds the coordinates of a character in the matrix.

- **`row_Rule(self, matrix, x1, y1, x2, y2)`**:
  Handles encryption when two characters are in the same row.

- **`col_Rule(self, matrix, x1, y1, x2, y2)`**:
  Handles encryption when two characters are in the same column.

- **`other_Rule(self, matrix, x1, y1, x2, y2)`**:
  Handles encryption when two characters form a rectangle.

- **`encrypt(self)`**:
  Encrypts the plaintext using the Playfair cipher rules.

---


## **Sample Output**
```plaintext
+++++++++++++++++++++
 The Encrypted text is GATLMZCLRQTX
+++++++++++++++++++++
```

---

## **How the Cipher Works**
1. **Generate the Matrix**:
   - The keyword is used to create a unique matrix of letters (excluding `J` and replacing it with `I`).
   - Remaining letters of the alphabet are appended to fill the 5x5 grid.

2. **Prepare the Plaintext**:
   - Spaces are removed, and repeated characters in pairs are separated by `X`.
   - If the plaintext has an odd length, a filler (`Z`) is added.

3. **Encrypt the Digraphs**:
   - **Same Row:** Replace each character with the one to its right (wrapping around to the start).
   - **Same Column:** Replace each character with the one below it (wrapping to the top).
   - **Rectangle Rule:** Replace the characters with the ones in the same row but opposite corners.

---

## **Notes**
- Ensure the keyword is unique and meaningful for better encryption.
- The plaintext should be a string without numbers or special characters.

Feel free to modify and extend the script for additional functionality or decryption.
