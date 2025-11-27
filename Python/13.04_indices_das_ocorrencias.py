texto = input().rstrip("\n")
palavra = input().rstrip("\n")

indices = []
i = 0

while True:
    pos = texto.find(palavra, i)
    if pos == -1:
        break
    indices.append(pos)
    i = pos + len(palavra)

for x in indices:
    print(x)
