import time

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    # print(f' item: {item} - high: {high} - low: {low}')
    while low <= high:
        mid = (low + high) // 2
        # print(f' - low: {low}  high: {high}  mid: {mid}')
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        # time.sleep(1)
    return None


my_list = [1, 3, 5, 7, 9]


print(binary_search(my_list, 7))
print(binary_search(my_list, -1))