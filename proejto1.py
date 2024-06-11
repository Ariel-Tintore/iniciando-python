# Banco de dados de usuários e senhas
usuarios = []
senhas = []

def criar_conta():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha desejada: ")

    # Armazenando o usuário e senha na lista
    usuarios.append(usuario)
    senhas.append(senha)
    print("Conta criada com sucesso!")

def login():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    # Verificando se o usuário e senha correspondem
    if usuario in usuarios and senha == senhas[usuarios.index(usuario)]:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

# Programa principal
while True:
    print("\nSelecione a opção desejada:")
    print("1 - Criar conta")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        criar_conta()
    elif opcao == "2":
        login()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Programa encerrado.")