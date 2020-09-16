def selected_sort(numbers):
    for k in range(len(numbers)-1) :
        m = min(numbers[k:])
        if numbers[k] != m:
            idx = numbers[k:].index(m) + k
            tmp = numbers[k]
            # swap
            numbers[k],  numbers[idx] = m, tmp
    return numbers

print([3,1,2,4,5,6,7,3,3,8])
print(selected_sort([3,1,2,4,5,6,7,3,3,8]))
