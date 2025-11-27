cpf = input().strip()

# Remove pontos e hífen → deixa só os dígitos
nums = []
for c in cpf:
    if c.isdigit():
        nums.append(int(c))

# Agora nums contém 11 números: D1..D11
D1, D2, D3, D4, D5, D6, D7, D8, D9, D10_input, D11_input = nums

# ----- Cálculo do primeiro dígito verificador -----
S1 = (10*D1 + 9*D2 + 8*D3 + 7*D4 + 6*D5 +
      5*D6 + 4*D7 + 3*D8 + 2*D9)

if S1 % 11 < 2:
    D10 = 0
else:
    D10 = 11 - (S1 % 11)

# ----- Cálculo do segundo dígito verificador -----
S2 = (11*D1 + 10*D2 + 9*D3 + 8*D4 + 7*D5 + 
      6*D6 + 5*D7 + 4*D8 + 3*D9 + 2*D10)

if S2 % 11 < 2:
    D11 = 0
else:
    D11 = 11 - (S2 % 11)

# ----- Validação -----
if D10 == D10_input and D11 == D11_input:
    print("CPF valido")
else:
    print("CPF invalido")
