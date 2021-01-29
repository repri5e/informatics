ans = 1000
line = [int(i) for i in input().split()]
for i in range(len(line)):
    if 0 < line[i] < ans:
        ans = line[i]
print(ans)
