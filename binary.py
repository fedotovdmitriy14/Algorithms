
numbers = [2, 6, 7, 8, 2, 8, 15, 0, 1, 77]



def binary_search(arr, search):
    arr.sort()
    index = None
    lowest = 0
    highest = len(numbers)

    while (lowest <= highest) and index is None:
        middle = (lowest + highest) // 2

        if numbers[middle] == search:
            index = middle
        else:
            if search < numbers[middle]:
                highest = middle - 1
            else:
                lowest = middle +1

    return f"Индекс равен {index}"

print(binary_search(numbers, 77))

