# Spelling Checker (Python)
This Python program takes a word as input and calculates its edit distance from each word present in the 'book.txt' file. The Levenshtein Edit Distance Algorithm will be used to suggest a new word instead of a word that is not found in the dictionary or is misspelled. If the word's distance from all the words is more than 3, the program does not provide any suggestions and prints "NONE". Otherwise, it finds the word with the smallest distance from the given word and calculates the steps required to reach the correct word. The program then prints the output on the console and saves it inside the 'testout.txt' file.

## Features
- Calculates the edit distance between a given word and words in the 'book.txt' file.
- Provides suggestions for the correct word if the edit distance is within a certain threshold(3).
- Prints the output on the console and saves it to the 'testout.txt' file.

## Requirements
To run this program, you need:
- Python 3.x

## Usage
1. Clone the repository or download the source code.
2. Ensure that the 'book.txt' file is present in the same directory as the program.
3. Open a terminal or command prompt and navigate to the program's directory.
5. Enter a word when prompted.
6. The program will calculate the edit distance from each word in 'book.txt' and provide suggestions if applicable.
7. The output will be displayed on the console, and it will be saved in the 'testout.txt' file.

## License
This program is released under the [MIT License](https://raw.githubusercontent.com/SahilDShaw/spelling-checker-python/main/LICENSE). Feel free to modify and distribute it as per the terms of the license.

## Disclaimer
This program calculates the edit distance between a given word and words in 'book.txt' to provide suggestions. The suggestions are based on the edit distance and may not always be accurate. The correctness of the suggestions depends on the quality and relevance of the words in the 'book.txt' file. The author and contributors of this program are not responsible for any consequences arising from the use of this program.
