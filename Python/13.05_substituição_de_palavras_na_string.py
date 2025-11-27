texto = input().rstrip("\n")
pal1 = input().rstrip("\n")
pal2 = input().rstrip("\n")

palavras = texto.split()

resultado = []
for p in palavras:
    if p == pal1:
        resultado.append(pal2)
    else:
        resultado.append(p)

print(" ".join(resultado))
