def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


if __name__ == '__main__':
    n = 200
    fib_gen = fib(n)

    with open('fib.txt', 'w', encoding='utf-8') as file:
        for num in fib_gen:
            file.write(str(num) + '\n')

    fib_gen = fib(n)
    result = None
    for num in fib_gen:
        result = num
    print(result)