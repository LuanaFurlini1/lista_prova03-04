# Calculadora de Área de Figuras Geométricas

# Crie um algoritmo que calcule a área de diferentes figuras geométricas, como:
# •	Quadrado: lado²
# •	Retângulo: base * altura
# •	Triângulo: (base * altura) / 2
# •	Círculo: π * raio² 
# Desafio: O usuário deve escolher qual figura deseja calcular e o algoritmo deve 
# solicitar as variáveis necessárias (como lado, base, altura ou raio).

print("-"*45) 
print("Calculadora de Área de Figuras Geométricas:")
print("1 - Quadrado")
print("2 - Retângulo")
print("3 - Triângulo")
print("4 - Círculo")
print("-"*45)

figura = int(input("Selecione o número correspondente a figura escolhida: "))


while figura >= 1 or figura <= 4:

    if figura == 1:
        print(" ")
        l = float(input("Informe a medida do lado do quadrado: "))
        area = l**2
        area = round(area, 2)
        print(f"Área do Quadrado: {area}")
        break

    elif figura == 2:
        print(" ")
        b = float(input("Informe a medida da base do retângulo: "))
        a = float(input("Informe a medida da altura do retângulo: "))
        area = b * a
        area = round(area, 2)
        print(f"Área do Retângulo: {area}")
        break

    elif figura == 3:
        print(" ")
        b = float(input("Informe a medida da base do triângulo: "))
        a = float(input("Informe a medida da altura do triângulo: "))
        area = (b * a)/2
        area = round(area, 2)
        print(f"Área do Triângulo: {area}")
        break

    elif figura == 4:
        print(" ")
        r = float(input("Informe a medida do raio da circunferência: "))
        area = 3.14 * r**2
        area = round(area, 2)
        print(f"Área do círculo: {area}")
        break

    else:
        figura = int(input("Selecione um número válido: "))
        