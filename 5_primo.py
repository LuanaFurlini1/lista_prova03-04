# Número Primo

# Crie um algoritmo que verifique se um número fornecido pelo usuário é primo ou não.
# Um número é primo se ele for maior que 1 e divisível apenas por 1 e por ele mesmo. 
# Desafio: O algoritmo deve realizar o cálculo da divisibilidade e usar uma estrutura de 
# repetição para verificar todos os números até a raiz quadrada do número.

n = int(input("Digite um numero inteiro positivo qualquer: "))

if n <= 1:
    print(f"{n} não é um número primo!")

else:
    raiz = n ** 0.5
    primo = True
    
for i in range(2, int(raiz) + 1):
    if n % i == 0:
        primo = False
        break

if primo:
        print(f"{n} é um número primo!")

else:
    print(f"{n} não é um número primo!")