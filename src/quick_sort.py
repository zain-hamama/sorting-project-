def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for x in arr[:-1]:

        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":

    numbers = [8,4,6,2,7,1]

    print("Original:", numbers)

    sorted_numbers = quick_sort(numbers)

    print("Sorted:", sorted_numbers)

    sizes = [20, 50, 100, 500, 1000]