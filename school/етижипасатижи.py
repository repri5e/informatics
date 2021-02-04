src = 6
results = [0]*32

def one(num):
    return num+1
def two(num):
    return 2*num

for i in range(32):
    operator = 1
    binary = str(bin(i))[2:]
    binary += '0'*(5-len(binary))
    binary = list(binary)
    for j in range(5):
        turn = binary[0]
        binary = binary[1:]
        if turn == '0':
            opeator = one(operator)
        elif turn == '1':
            operator = two(operator)
    results[i] = operator

while True:
    print(results)
    if results.count(str(src)) == 0:
        print(src)
        break
    else:
        src += 1
