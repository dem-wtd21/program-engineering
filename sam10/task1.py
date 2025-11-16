import time

def timer(func):
    def wrapper():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print(f"\nВремя выполнения: {end_time - start_time:.6f} секунд")
    return wrapper

@timer
def fibonacci():
    fib1 = 0
    fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end='')

if __name__ == '__main__':
    fibonacci()