# 1. Calculadora de Imposto de Renda Progressivo
# Descrição: O imposto de renda no Brasil é progressivo. 
# Crie um algoritmo que calcule o valor do imposto de renda 
# de uma pessoa com base na sua faixa de rendimento. As faixas 
# e alíquotas são as seguintes:

# •	Até R$ 1.903,98: isento
# •	De R$ 1.903,99 a R$ 2.826,65: 7,5%
# •	De R$ 2.826,66 a R$ 3.751,05: 15%
# •	De R$ 3.751,06 a R$ 4.664,68: 22,5%
# •	Acima de R$ 4.664,68: 27,5%
# Desafio: Utilize variáveis para armazenar os rendimentos 
# e a alíquota aplicada, além de usar constantes para as faixas.

rendimento = float(input("Informe seu salário: "))

a = rendimento * 0.075
b = rendimento * 0.15
c = rendimento * 0.225
d = rendimento * 0.275

if rendimento <= 1903.98:
    print("Isento")

elif rendimento >= 1903.99 and rendimento <= 2826.65:
    print(f"Imposto de Renda com 7,5%: {round(a, 2)}")

elif rendimento >= 2826.66 and rendimento <= 3751.05:
    print(f"Imposto de Renda com 15%: {round(b, 2)}")

elif rendimento >= 3751.06 and rendimento <= 4664.68:
    print(f"Imposto de Renda com 22,5%: {round(c, 2)}")

else:
    print(f"Imposto de Renda com 27,5%: {round(d, 2)}")
