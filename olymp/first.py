k = int(input())
dist = int(input())

last = dist // k
lastd = dist - last*k
if lastd >= k/2:
    print(k-lastd)
else:
    print(lastd)
