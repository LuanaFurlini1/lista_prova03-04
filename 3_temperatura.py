# Conversor de Temperaturas

# Crie um algoritmo que converta uma temperatura em graus Celsius para Fahrenheit e Kelvin.

# Fórmulas:
# • Fahrenheit = (Celsius * 9/5) + 32
# • Kelvin = Celsius + 273.15 
# Desafio: O algoritmo deve fazer a conversão a partir de uma temperatura 
# fornecida pelo usuário e apresentar os dois resultados.

temp = float(input("Insira uma temperatura em graus Celsius: "))

f = (temp * 1.8) + 32
f = round(f, 2)

k = temp + 273.15
k = round(k, 2)

print(f"Temperatura em Fahrenheit: {f}")
print(f"Temperatura em Kelvin: {k}")

