J = 0.009
y_0 = 11000
saldo = 1000000
n_meses = 30 * 12

# Função para calcular o valor mensal necessário
def calculate_u(y_0, saldo, J, n_meses):
    y = y_0
    for _ in range(n_meses):
        u_t = (saldo - y * (1 + J)**n_meses) / sum((1 + J)**i for i in range(n_meses))
    return u_t

u_t = calculate_u(y_0, saldo, J, n_meses)
print("Deve ser investido mensalmente R$",u_t)
