def inserted_sort(numbers):
    for i in range(1, len(numbers)):
        j = i - 1
        tmp = numbers[i]
        print(tmp)
        print(numbers[j])
        while numbers[j] > tmp and j>=0:
            numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
            j = j-1
            print(numbers)
    return numbers



# print([3,1,2,4,5,6,7,3,3,8])
print(inserted_sort([3,1,2,4,5,7,5,5,3,1,1,6,7,3,3,8]))
# print(inserted_sort([3,8,2,5,4,6,7,1]))
