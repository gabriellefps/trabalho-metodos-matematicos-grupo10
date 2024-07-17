import sympy as sp

# Definir a variável simbólica
t = sp.symbols('t')

# Definir os parâmetros simbólicos
rho20, alpha = sp.symbols('rho20 alpha')

# Definir a função rho(t)
rho = rho20 * sp.exp(alpha * (t - 20))
print(f"rho(t): {rho}\n")

# Calcular a derivada de rho(t) em relação a t
rho_prime = sp.diff(rho, t)
print(f"Derivada simbólica de rho(t): {rho_prime}\n")

# Definir os valores para rho20 e alpha
rho20_value = 5.6e-8  # Resistividade em ohm-metros, por exemplo, para o cobre
alpha_value = 0.0045   # Coeficiente de temperatura, por exemplo, para o cobre

# Avaliar a derivada simbólica em t = 20
rho_prime_at_20 = rho_prime.subs({t: 20, rho20: rho20_value, alpha: alpha_value})
print(f"Derivada de rho(t) em t=20: {rho_prime_at_20}\n")

# Valor de P1
P1_t = rho20_value + rho_prime_at_20*(t-20)
print(f"Valor de P1(t): {P1_t}\n")

#Avaliar a derivada segunda simbólica em relação a t
rho_prime2 = sp.diff(rho, t, t)
print(f"Derivada segunda simbólica de rho(t): {rho_prime}\n")

# Avaliar a derivada segunda simbólica em t = 20
rho_prime2_at_20 = rho_prime2.subs({t: 20, rho20: rho20_value, alpha: alpha_value})
print(f"Derivada segunda de rho(t) em t=20: {rho_prime2_at_20}\n")

# Valor de P2
P2_t = rho20_value + rho_prime_at_20*(t-20) + (rho_prime2_at_20/2)*((t-20)**2)
print(f"Valor de P2(t): {P2_t}\n")