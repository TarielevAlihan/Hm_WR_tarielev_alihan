def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Последние i элементов уже отсортированы,
        # поэтому мы можем игнорировать их
        for j in range(0, n-i-1):
            # Переставляем элементы, если текущий больше следующего
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)




def binary_search(sorted_list, val):
    first = 0
    last = len(sorted_list)-1
    position = None
    while first <= last:
        middle = (first + last) // 2
        if val == sorted_list[middle]:
            position = middle
            break
        elif val > sorted_list[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if position is not None:
        return f'{val} существует в позиции {position}'
    else:
        return f'{val} не существует'




print(binary_search(sorted_list, 2))
print(binary_search(sorted_list,6 ))
print(binary_search(sorted_list, 9))





