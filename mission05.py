# Missão 05: Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

senha_correta = "Python123"

while True:
    senha = input("Digite a senha: ")
    if senha_correta == senha:
        print("Acesso liberado!")
        break
    else:
        print("Senha incorreta. Tente novamente.")