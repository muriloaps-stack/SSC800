valores = []

for i in range(5):
    numero = int(input(f"Digite um {i+1} valor inteiro: "))
    valores.append(numero)

inverso = []

for i in range(len(valores)-1, -1, -1):
    inverso.append(valores[i])

print("Valores na ordem inversa:", inverso)
print("lista original:", valores)