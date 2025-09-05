a, b = input().split()

newa = ""
newb = ""

for i in range(-1, -len(a) - 1, -1):
    newa += a[i]
for i in range(-1, -len(b) - 1, -1):
    newb += b[i]

print(max(int(newa), int(newb)))
