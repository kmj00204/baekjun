n = int(input())

letters = set()
for _ in range(n):
    letters.add(input())

sorted_letters = sorted(letters, key=lambda x: (len(x), x))

for letter in sorted_letters:
    print(letter)
