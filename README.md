# César Cipher Project in Python

[FR](README.fr.md) | [EN](README.md)

## Description

This project is a Python script that implements the César cipher. It can be executed from the command line to encrypt or decrypt text.  
The script works only on letters of the alphabet (after converting them to lowercase) and ignores all other characters (spaces, numbers, punctuation, etc.).

------------

### Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Improvement Suggestions](#improvement-suggestions)
- [License](#license)
- [Author](#author)

------------

## Features

**Encryption/Decryption**  
- Allows you to encrypt or decrypt text by applying a defined shift to each letter of the alphabet.  
- Letters are converted to lowercase, and only the letters A to Z are processed.

**Processing Modes**

- **Text Mode:** The text to be processed is passed as an argument in the command line.
- **File Mode:** The script can read text from a file, process it, and overwrite the same file or write the output to a specified file.

**Command Line Options**

- The script uses the `argparse` module to provide detailed help and verify the validity of the provided arguments.

## Prerequisites

Python 3.x must be installed on your machine.

## Installation

Clone the repository (or download the script):

```bash
git clone https://github.com/Foufou-exe/py-cryptographie-cesar.git
cd py-cryptographie-cesar
```
Make the script executable (optional):

```bash
chmod +x main.py
```

Run the script from the command line with the following syntax:

```bash
python main.py [-c SHIFT | -d SHIFT] [-f FILE] [-o OUTPUT_FILE] [TEXT]

```

**Encrypting Text Passed as an Argument**

To encrypt the text "abc" with a shift of 2:

```bash
python main.py -c 2 "abc"
```

Expected output:

```bash
cde
```
Decrypting Text Passed as an Argument

To decrypt the text "cde" with a shift of 2:

```bash
python main.py -d 2 "cde"
```

Expected output:

```bash
abc
```

**Encrypting a File**

If the file fichier.txt contains, for example, "Abc, XYZ! 123", the script will process only the letters (after converting them to lowercase) and ignore non-alphabetic characters:

Displayed output:

```bash
abcya
```

**Specifying an Output File**

To write the output to a different file without overwriting the original:

```bash
python main.py -c 27 -f fichier.txt -o resultat.txt
```

The result will be written to resultat.txt and also displayed in the console.

## How It Works

The César cipher implemented in this script works as follows:

### Conversion to Lowercase:

All letters are transformed to lowercase.

### Processing Letters Only:

Only the letters of the alphabet (A to Z) are encrypted/decrypted. Other characters are ignored in the final output.

### Cyclical Shift:

The shift operation is performed modulo 26, which allows using shifts greater than 26.

**Available Options**

- -c SHIFT : Encrypt the text with the specified shift.

- -d SHIFT : Decrypt the text with the specified shift.

- -f, --file FILE : Specifies the file to process.

- -o, --output OUTPUT_FILE : (Optional) Specifies the output file. By default, the input file is overwritten.

- -h, --help : Displays the help message for the script.

## Improvement Suggestions

- [ ] Interactive Mode: Add a command line interface that guides the user step-by-step.

- [ ] Batch Processing: Allow encryption/decryption of multiple files.

- [ ] Adding Other Algorithms: Integrate additional encryption methods (e.g., the Vigenère cipher).

- [ ] Unit Testing: Implement a test suite to ensure the code's robustness.

- [ ] Graphical User Interface: Develop a user interface using Tkinter or another library.

## License

Under the MIT License. You are free to use, modify, and distribute this code as long as you retain the author's attribution and the license.

## Author

[@Foufou-exe](https://github.com/Foufou-exe)




