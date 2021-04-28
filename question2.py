def search (str, lst, size):
    result = 0
    for i in range(size):
        if lst[i] == str:
            result = i + 1
    if result != 0:
        return result
    else:
        return -1

str = "hello"
lst = ["abc", "dab", "abba"]
size = 3
print(search(str, lst, size))
