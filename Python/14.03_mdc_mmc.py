def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mdc3(a, b, c):
    return mdc(mdc(a, b), c)

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

def mmc3(a, b, c):
    return mmc(mmc(a, b), c)

# Programa principal
n1 = int(input())
n2 = int(input())
n3 = int(input())

resultado_mdc = mdc3(n1, n2, n3)
resultado_mmc = mmc3(n1, n2, n3)

print(f"MDC: {resultado_mdc}")
print(f"MMC: {resultado_mmc}")
