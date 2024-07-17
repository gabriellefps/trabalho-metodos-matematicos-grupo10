import numpy as np
import matplotlib.pyplot as plt

# Definir a expressão do polinômio de Taylor de segundo grau
def P2(t):
    return 2.52e-10 * t + 5.67e-13 * (t - 10)**2 + 5.086e-8

# Gerar valores de t de -250 a 1000 Graus Celsius
t_values = np.linspace(-250, 1000, 400)

# Calcular os valores correspondentes de P2(t)
P2_values = P2(t_values)

# Plotar o gráfico
plt.figure(figsize=(0, 1000))
plt.plot(t_values, P2_values, label='P2(t)')
plt.xlabel('t (°C)')
plt.ylabel('P2(t)')
plt.title('Gráfico de P2(t)')
plt.legend()
plt.grid(True)
plt.show()


