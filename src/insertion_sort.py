def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    numbers = [8, 4, 6, 2, 7, 1]

    print("Original:", numbers)
    sorted_numbers = insertion_sort(numbers)
    print("Sorted:", sorted_numbers)
    