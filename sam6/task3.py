def find_top_3_counts(number_string):
    all_counts = {}
    for char in number_string:
        digit = int(char)
        all_counts[digit] = all_counts.get(digit, 0) + 1

    sorted_items = sorted(
        all_counts.items(),
        key=lambda item: (item[1], -item[0]),
        reverse=True
    )
    top_3_items = sorted_items[:3]
    final_dict = dict(sorted(top_3_items, key=lambda item: item[0]))

    return final_dict

# Пример использования
random_numbers = "9112223333444445555556666667777777"
result_dict = find_top_3_counts(random_numbers)

print(result_dict)