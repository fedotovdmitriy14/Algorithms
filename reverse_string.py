# переворот строки

def reverse_string(string):
    reversed_string = []
    index = len(string)

    while index:
        index -= 1
        reversed_string.append(string[index])

    return "".join(reversed_string)


print(reverse_string("Hello there!"))