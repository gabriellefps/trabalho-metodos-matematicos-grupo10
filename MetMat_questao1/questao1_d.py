J = 0.009
y_f = 1000000
y_i = 11000
n_meses = 30 * 12

def calculate(y_i, y_f, J, n_meses):
  for _ in range(n_meses):
    u_t = (y_f - y_i * (1 - J)**n_meses) / sum((1 + J)**i for i in range(n_meses))
  return u_t

u_t = calculate(y_i, y_f, J, n_meses)
print("O valor necessário é: R$",u_t)