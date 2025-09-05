t = int(input())

for _ in range(t):
    s, r = input().split()
    s = int(s)
    string = ""
    for i in range(len(r)):
        string += r[i] * s
    print(string)
