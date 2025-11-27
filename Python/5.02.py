nota = float(input())

X = 0
Y = 0
Z = 0

while nota >= 0:
    if nota < 5:
        X = X + 1
        Z = nota + Z
    elif nota >= 5:
        Y = Y+1
        Z = nota + Z
    
    nota = float(input())

P = int((Y / (X + Y)) * 100)

print(f"Baixas: {X}")
print(f"Altas: {Y}")
print(f"Media: {Z / (X + Y):.2f}")
print(f"Percentual: {P}%")


