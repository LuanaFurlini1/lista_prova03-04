# Calculadora de Desconto de Produtos

# Crie um algoritmo que calcule o preço final de um produto 
# após aplicar um desconto baseado no preço inicial:

# • Se o preço for maior que R$ 1.000, o desconto será de 15%.
# • Se o preço for entre R$ 500 e R$ 1.000, o desconto será de 10%.
# • Se o preço for menor que R$ 500, o desconto será de 5%.
# Desafio: Use estruturas de decisão e constantes para o valor do desconto.

preco = float(input("Insira o valor do produto escolhido: "))

a = preco * 0.15
b = preco * 0.10
c = preco * 0.05

if preco > 1000:
    print(f"Preço com desconto de 15%: {preco - a}")

elif preco >= 500 and preco <= 1000:
    print(f"Preço com desconto de 10%: {preco - b}")

elif preco < 500 and preco >= 1:
    print(f"Preço do produto com desconto de 5%: {preco - c}")

else:
    print("Insira um preço válido!")