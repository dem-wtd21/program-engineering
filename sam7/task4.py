with open('zapreshyonka.txt', 'r') as f:
    bad_words = f.read().split()

text = input("Введите предложение: ")

result = text
for word in bad_words:
    result = result.replace(word, '*' * len(word))
    result = result.replace(word.upper(), '*' * len(word))
    result = result.replace(word.capitalize(), '*' * len(word))

print(result)