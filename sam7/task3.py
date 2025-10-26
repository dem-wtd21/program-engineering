with open('center mass.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')
num_lines = len(lines)

words = text.split()
num_words = len(words)

letters = 0
for char in text:
    if char.isalpha():
        letters += 1

print("center mass file contains:")
print(f"{letters} letters")
print(f"{num_words} words")
print(f"{num_lines} lines")