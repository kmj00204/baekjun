a = int(input())
b = input()
n = -1

while n > (len(b) * -1) - 1:
    print(a * int(b[n]))
    n -= 1
print(a * int(b))
