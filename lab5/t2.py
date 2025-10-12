print("Set():")
a = set('abcdefg')
print(a)

for i in range(1, 5):
    a.add(i)
    print(a)

print("\nFrozenset():")
b = frozenset('abcdefg')
print(b)

try:
    for i in range(1, 5):
        b.add(i)
        print(b)
except AttributeError as e:
    print(f"Ошибка: {e}")