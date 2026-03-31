def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    numbers = [8, 4, 6, 2, 7, 1]

    print("Original:", numbers)

    sorted_numbers = selection_sort(numbers)

    print("Sorted:", sorted_numbers)