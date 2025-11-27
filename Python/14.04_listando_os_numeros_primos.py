def eh_primo(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

# Programa principal
N = int(input())

for num in range(2, N + 1):
    if eh_primo(num) == 1:
        print(num)
