# Conversão de Número Decimal para Binário

# Crie um algoritmo que converta um número decimal fornecido pelo usuário para o sistema binário. 
# Desafio: O algoritmo deve fazer a conversão usando divisões sucessivas por 2, armazenando os 
# restos e, ao final, invertendo a sequência dos restos para formar o número binário.

print("-- Cálculadora de Número Decimal para Binário --")
n = int(input("Informe um número inteiro positivo qualquer: "))
binario = ""  

while n > 0:
    resto = n % 2
    binario = str(resto) + binario  
    n = n // 2

print(f"Número em binário: {binario}")


