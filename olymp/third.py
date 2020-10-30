n = int(input())
coords = n*[0]

for y in range(n):
    x = int(input())
    coords[x-1] = n + 1 - y

for i in coords:
    print(i-1)
    
    
