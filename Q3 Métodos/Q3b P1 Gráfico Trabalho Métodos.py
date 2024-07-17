import numpy as np
import matplotlib.pyplot as plt

# Definir a expressão do polinômio de Taylor de primeiro grau
def P1(t):
    return 2.52e-10*t + 5.096e-8

# Gerar valores de t de -250 a 1000 Graus Celsius
t_values = np.linspace(-250, 1000, 400)

# Calcular os valores correspondentes de P1(t)
P1_values = P1(t_values)

# Plotar o gráfico
plt.figure(figsize=(0, 1000))
plt.plot(t_values, P1_values, label='P1(t)')
plt.xlabel('t (°C)')
plt.ylabel('P1(t)')
plt.title('Gráfico de P1(t)')
plt.legend()
plt.grid(True)
plt.show()