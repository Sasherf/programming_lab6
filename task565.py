counts = {}
n = int(input())

for i in range(n):
    line = input().split()
    for word in line:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

best_word = None
max_count = 0

for word in sorted(counts):
    if counts[word] > max_count:
        max_count = counts[word]
        best_word = word

print(best_word)