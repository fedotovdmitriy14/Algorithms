# алгоритм Евклида

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
            print(a)
        else:
            b = b % a
            print(b)

    return a+b

print(gcd(30, 18))
# print(gcd(77, 0))