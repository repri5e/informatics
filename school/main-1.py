def ReduceFraction(n, m):
    src1, src2 = n, m
    while m != n:
        if n > m:
            n = n - m
        else:
            m = m - n
    gcd = m
    p = src1 / gcd
    q = src2 / gcd
    return(p, q)
a = int(input())
b = int(input())
print(*(map(int, ReduceFraction(a, b))))