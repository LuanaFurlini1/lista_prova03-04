# Determinação de Salário Líquido

# O algoritmo deve calcular o salário líquido de um funcionário, considerando:
# •	Desconto de INSS (8% do salário bruto)
# •	Desconto de IR (5% para salários até R$ 2.000, 10% para salários maiores) 

# Desafio: O algoritmo deve calcular o desconto do INSS e o imposto de renda, subtrair
#  esses valores do salário bruto e exibir o salário líquido.

salarioB = float(input("Informe seu salário bruto: "))

inss = salarioB * 0.08

if salarioB <= 2000:
    ir = salarioB * 0.05

else:
    ir = salarioB * 0.1

salarioL = salarioB - inss - ir

print(f"Seu salário líquido é de: {salarioL}")