from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

import random
import time
import csv
import os


def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]


def generate_sorted_list(size):
    return list(range(size))


def generate_reverse_sorted_list(size):
    return list(range(size, 0, -1))


def generate_almost_sorted_list(size):
    arr = list(range(size))

    if size > 1:
        swaps = max(1, size // 50)

        for _ in range(swaps):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]

    return arr


def measure_time(sort_function, data):
    start = time.perf_counter()
    sort_function(data.copy())
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":

    sizes = [20, 50, 100, 500, 1000]

    algorithms = [
        ("Selection", selection_sort),
        ("Insertion", insertion_sort),
        ("Merge", merge_sort),
        ("Quick", quick_sort)
    ]

    structures = [
        ("Random", generate_random_list),
        ("Sorted", generate_sorted_list),
        ("Reverse Sorted", generate_reverse_sorted_list),
        ("Almost Sorted", generate_almost_sorted_list)
    ]

    os.makedirs("../data", exist_ok=True)

    with open("../data/results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Algorithm", "Size", "Structure", "Time"])

        for size in sizes:
            print("\n==============================")
            print("Testing size:", size)

            for structure_name, structure_function in structures:
                test_list = structure_function(size)

                print("\nStructure:", structure_name)

                for algorithm_name, algorithm_function in algorithms:
                    try:
                        result = measure_time(algorithm_function, test_list)
                        print(algorithm_name, "Sort:", result)
                        writer.writerow([algorithm_name, size, structure_name, result])

                    except Exception as e:
                        print(algorithm_name, "Sort: ERROR")
                        writer.writerow([algorithm_name, size, structure_name, "ERROR"])



                      
