Exp = int(input().strip())

# Subida: 1 .. Exp
for k in range(1, Exp + 1):
    print('\t'.join('*' for _ in range(k)))

# Descida: Exp-1 .. 1
for k in range(Exp - 1, 0, -1):
    print('\t'.join('*' for _ in range(k)))
