# attempt no 2 at task 6 


def newtonSqrt(n, base):
    approx_root = 0.5 * n
    for i in range(base):
        betterapprox = 0.5 * (approx_root + n/approx_root)
        approx_root = betterapprox
    return betterapprox

print("the square root of 100 :",newtonSqrt(100, 10))
