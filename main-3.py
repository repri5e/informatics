def iter():
    a = int(input())
    b = int(input())
    print(a // b)
    print(a - b*(a // b))

try:
    while True:
        iter()
        print('='*15)
except KeyboardInterrupt:
    print('terminating...')
