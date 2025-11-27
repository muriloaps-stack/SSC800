def area(base,altura):
    area = (base * altura) / 2
    return area


input_base = float(input())
input_altura = float(input())       

resultado = area(input_base, input_altura)
print(resultado)