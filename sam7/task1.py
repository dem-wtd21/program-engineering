from collections import Counter


def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.lower().split()
    words = [word.strip('.,!?;:"()[]') for word in words if word.strip('.,!?;:"()[]')]

    total_words = len(words)

    word_counts = Counter(words)
    most_common_word, most_common_count = word_counts.most_common(1)[0]

    print(f"Общее количество слов в тексте: {total_words}")
    print(f"Самое частое слово: '{most_common_word}'")
    print(f"Количество повторений: {most_common_count}")

analyze_text('article.txt')