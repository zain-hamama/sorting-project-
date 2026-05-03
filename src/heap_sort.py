def heapify(arr, n, i):
    """
    Make the subtree rooted at index i a max-heap,
    assuming subtrees below i are already max-heaps.
    n = size of the heap (we may have shrunk it during sorting).
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Find the largest among root, left child, right child
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying down
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Phase 1: build a max-heap
    # Start from the last non-leaf node and heapify each upward
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to the end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    numbers = [8, 4, 6, 2, 7, 1]
    print("Original:", numbers)
    sorted_numbers = heap_sort(numbers)
    print("Sorted:", sorted_numbers)


    