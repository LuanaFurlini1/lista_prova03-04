# Cálculo de Raízes de uma Equação Quadrática

# O algoritmo deve calcular as raízes de uma equação quadrática do tipo ax² + bx + c = 0.
# O discriminante (Δ) é dado por Δ = b² - 4ac.

# •	Se Δ > 0, existem duas raízes reais distintas.
# •	Se Δ = 0, existe uma raiz real (múltipla).
# •	Se Δ < 0, não existem raízes reais. 
# Desafio: O algoritmo deve usar uma estrutura de decisão para verificar o valor de Δ
# e calcular as raízes.


a = float(input("Insira o A da sua equação: "))
b = float(input("Insira o B da sua equação: "))
c = float(input("Insira o C da sua equação: "))

delta = b * b - 4 * a * c
delta = round(delta, 2)


if delta > 0:
    b1 = (-b + delta ** 0.5) / (2 * a)
    b1 = round(b1, 2)
    b2 = (-b - delta ** 0.5) / (2 * a)
    b2 = round(b2, 2)
    print(f"Raízes da equação: {b1} e {b2}")

elif delta == 0:
    b3 = (-b) / (2 * a)
    print(f"Raíz da equação: {b3}")

else:
    print("Não existem raizes reais!")