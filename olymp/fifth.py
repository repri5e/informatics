n = int(input())
min_sizes = []
max_sizes = []
results = []

for i in range(n):
    min_size = int(input())
    min_sizes.append(min_size)

for i in range(len(min_sizes)):
    max_size = min_sizes[i]
    for j in range(len(min_sizes)):
        if max_size > min_sizes[j]:
            max_size += min_sizes[j]
    for j in range(len(min_sizes)):
        if max_size > min_sizes[j]:
            max_size += min_sizes[j]
    if max_size >= max(min_sizes):
        results.append(1)
    else:
        results.append(0)
        
for res in results:
    print(res)
