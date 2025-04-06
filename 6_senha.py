# Validação de Senha

# O algoritmo deve verificar se a senha fornecida pelo usuário atende aos critérios:

# •	Deve ter no mínimo 8 caracteres.
# •	Deve conter pelo menos uma letra maiúscula.
# •	Deve conter pelo menos um número.
# •	Não pode ter espaços. 
# Desafio: Utilize várias condições e variáveis para armazenar as informações,
# além de uma estrutura de repetição para garantir que a senha esteja correta.

print("-"*46)
print("Verificação de Senha:")
print("Deve ter no mínimo 8 caracteres.")
print("Deve conter pelo menos uma letra maiúscula.")
print("Deve conter pelo menos um número.")
print("Não pode ter espaços. ")
print("-"*46)

senha = input("Digite sua senha: ")

#Enquanto for verdade que as condições são falsas, ele realiza os testes
while True:
    #Inicia assumindo que todas as condições são falsas
    caracters = False
    maiuscula = False
    numero = False
    espaco = True #Menos essa, pq só funcionou assim (???)

    if len(senha) >= 8: #Testa a quantidade de caracteres 
        caracters = True

    #Laço para percorrer cada caracter da senha
    for caracter in senha:

        if caracter >= 'A' and caracter <= 'Z': #Testa se tem letra maiuscula 
            maiuscula = True
    
        if caracter >= '0' and caracter <= '9': #Testa se tem número
            numero = True
    
        if caracter == ' ': #Testa se tem espaço
            espaco = False

    # Se todas as condições forem satisfeitas, sai do laço
    if caracters and maiuscula and numero and espaco:
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Senha inválida! Tente novamente.")
        print(" ")
        senha = input("Digite sua senha: ")
    

