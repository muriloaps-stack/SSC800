linha = input().rstrip("\n")
lista = linha.split()

# conta em casefold para agrupar "Lucas" e "lucas"
from collections import Counter
freq = Counter([nome.casefold() for nome in lista])

# percorre mantendo a forma original, mas verifica por casefold
repetidos = [nome.capitalize() for nome in lista if freq[nome.casefold()] > 1]

print(repetidos)
