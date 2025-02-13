# Missão 02: Criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

while True:
    idade = int(input("Digite sua idade: "))

    if idade >= 16:
        print("Pode votar!")
    else:
        print("Não pode votar ainda!")
        break