texto = input().rstrip("\n")
palavra = input().rstrip("\n")

# separa o texto em palavras usando espaço
lista_palavras = texto.split()

# conta ocorrências exatas
contador = 0
for p in lista_palavras:
    if p == palavra:
        contador += 1

print(contador)
