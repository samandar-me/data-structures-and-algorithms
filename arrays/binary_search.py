def binary_search(items, target):
    low = 0
    high = len(items) - 1
    target = target.lower()

    while low <= high:
        mid = (low + high) // 2
        guess = items[mid].lower()

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None

# if __name__ == '__main__':
#     my_list1 = [3, 1, 8, 7, 2]
#     my_list2 = ["google", "apple", "meta", "bloomberg", "amazon"]
#
#   #  print(binary_search(my_list1, 8))
#
#     print(binary_search(my_list2, "Google"))