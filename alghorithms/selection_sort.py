
def find_smallest(arr):
    smallest_index = 0
    smallest = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


test_arr = [5, 3, 6, 2, 10]
print(f'before: {test_arr}')
print(f'after : {selection_sort(test_arr)}')
