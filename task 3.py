import random
import time

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == x:
            return middle
        elif arr[middle] < x:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def generate_sorted_array(size, lower_bound=1, upper_bound=10000):
    array = [random.randint(lower_bound, upper_bound) for _ in range(size)]
    return sorted(array)

def measure_time():
    sizes = [50000, 100000, 500000, 1000000]
    x = 500

    for size in sizes:
        array = generate_sorted_array(size)
        start_time = time.perf_counter()
        linear_search(array, x)
        linear_time = time.perf_counter() - start_time
        start_time = time.perf_counter()
        binary_search(array, x)
        binary_time = time.perf_counter() - start_time
        print(f"Розмір масиву: {size}")
        print(f"Час лінійного пошуку: {linear_time:.6f} секунд")
        print(f"Час бінарного пошуку: {binary_time:.6f} секунд")

measure_time()
