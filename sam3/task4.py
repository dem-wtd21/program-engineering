vowels = "aeiou"

while True:
    s = input("Введите предложение (или 'stop' для выхода): ")

    if s.lower() == "stop":
        break

    print(f"Длина: {len(s)}")

    s_lower = s.lower()
    print(f"Нижний регистр: {s_lower}")

    vowel_count = sum(1 for char in s_lower if char in vowels)
    print(f"Гласных: {vowel_count}")

    s_replaced = s.replace("ugly", "beauty").replace("Ugly", "Beauty")
    print(f"Замена: {s_replaced}")

    starts = s.startswith("The")
    ends = s.endswith("end")
    print(f"Начинается с 'The': {starts}")
    print(f"Заканчивается на 'end': {ends}")