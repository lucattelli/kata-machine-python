def bubble_sort(arr: list[int]) -> None:
    high = len(arr)

    while high > 1:
        for index in range(1, high):
            previous = index - 1
            current = index

            if arr[previous] > arr[current]:
                new_previous = arr[current]
                arr[current] = arr[previous]
                arr[previous] = new_previous

        high -= 1
