#сортировка выборкой

nums = [5, 7, 6, 9, 8, 2, 4, 3, 1]

print("Было", nums)

for i in range(len(nums)):
    lowest = i

    for j in range(i+1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j

    nums[i], nums[lowest] = nums[lowest], nums[i]
    print(nums)

print("Стало", nums)