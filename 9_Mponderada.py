# Calculadora de Média Ponderada

# O algoritmo deve calcular a média ponderada de um aluno, dado:
# •	Nota 1 com peso 3
# •	Nota 2 com peso 2
# •	Nota 3 com peso 5 

# Após calcular a média, classifique o aluno:
# •	Se a média for maior ou igual a 7, o aluno está aprovado.
# •	Se a média for menor que 7, o aluno está reprovado.
# Desafio: Use variáveis para armazenar as notas e os pesos e calcule a média ponderada. 

n1 = float(input("Informe sua primeira nota: "))
n2 = float(input("Informe sua segunda nota: "))
n3 = float(input("Informe sua terceira nota: "))

#pesos
p1 = 3
p2 = 2
p3 = 5

#multiplicando notas pelos pesos
m1 = n1 * p1
m2 = n2 * p2
m3 = n3 * p3

soma_pesos = p1 + p2 + p3

media = (m1 + m2 + m3) / soma_pesos
media = round(media,2)

if media >= 7:
    print(f"Parabéns, você foi aprovado! Sua média foi: {media}")

else:
    print(f"Aluno reprovado! Média: {media}")