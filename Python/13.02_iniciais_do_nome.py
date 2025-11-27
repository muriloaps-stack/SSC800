nome = input().rstrip("\n")

palavras = nome.split()

iniciais = [p[0] for p in palavras]

print(iniciais)
