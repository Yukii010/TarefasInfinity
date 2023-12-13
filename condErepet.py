senha_cadastrada = "123456"
email_cadastrado = "usuario@exemplo.com"

senha_digitada = input("Digite sua senha: ")
email_digitado = input("Digite seu email: ")

while senha_digitada != senha_cadastrada or email_digitado != email_cadastrado:
    print("Senha ou email inválidos.")
    senha_digitada = input("Digite sua senha novamente: ")
    email_digitado = input("Digite seu email novamente: ")

print("Login efetuado com sucesso!")
