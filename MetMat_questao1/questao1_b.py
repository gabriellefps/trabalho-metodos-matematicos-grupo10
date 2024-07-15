# Dados fornecidos
J = 0.009
u = -11000
n_meses = 13 * 12

# Encontrar o saldo inicial necessário
y = 0  # saldo final é zero após 13 anos
for saldo in range(n_meses):
    y = (y - u) / (1 + J)

print("O valor mínimo necessário é: R$",y)  # saldo inicial necessário