import numpy as np
import matplotlib.pyplot as plt

# Definir as funções
def rho_exact(t, rho20, alpha):
    return rho20 * np.exp(alpha * (t - 20))

def rho_linear(t, rho20, alpha):
    return rho20 * (1 + alpha * (t - 20))

# Definir os parâmetros
rho20 = 1.68e-8
alpha = 0.0039

# Gerar valores de t
t_values = np.linspace(0, 80, 400)

# Calcular valores exatos e aproximados
rho_exact_values = rho_exact(t_values, rho20, alpha)
rho_linear_values = rho_linear(t_values, rho20, alpha)

# Calcular o erro relativo
relative_error = np.abs((rho_exact_values - rho_linear_values) / rho_exact_values)

# Encontrar intervalo onde o erro é menor ou igual a 1%
within_1_percent = np.where(relative_error <= 0.01)[0]
t_min = t_values[within_1_percent[0]]
t_max = t_values[within_1_percent[-1]]

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t_values, rho_exact_values, label='ρ(t) Exato', color='blue')
plt.plot(t_values, rho_linear_values, label='ρ(t) Linear', color='orange', linestyle='--')
plt.fill_between(t_values, rho_linear_values, rho_exact_values, 
                 where=(relative_error <= 0.01), color='green', alpha=0.3, label='Faixa de 1%')
plt.axvline(t_min, color='red', linestyle=':', label=f'Limite inferior: {t_min:.1f}°C')
plt.axvline(t_max, color='purple', linestyle=':', label=f'Limite superior: {t_max:.1f}°C')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistividade (Ω·m)')
plt.title('Comparação entre a Resistividade Exata e a Aproximação Linear')
plt.legend()
plt.grid(True)
plt.show()

print(f"Intervalo de valores de t onde a aproximação linear fica dentro de uma faixa de 1% do valor exato: {t_min:.1f}°C a {t_max:.1f}°C")
