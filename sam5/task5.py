def create_special_set(numbers):
    result_set = set()
    from collections import Counter
    counts = Counter(numbers)

    for num, count in counts.items():
        result_set.add(num)
        for i in range(2, count + 1):
            result_set.add(str(num) * i)

    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

set_1 = create_special_set(list_1)
set_2 = create_special_set(list_2)
set_3 = create_special_set(list_3)

print(f"Множество 1: {set_1}")
print(f"Множество 2: {set_2}")
print(f"Множество 3: {set_3}")