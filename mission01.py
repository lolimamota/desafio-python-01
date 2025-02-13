# Missão 1: criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

# nota = float(input("Digite a nota: "))

# if nota >= 6:
#     print("Este aluno está Aprovado! :D")
#     float(input("Digite a nota: "))
# else:
#     print("Este aluno está reprovado! :(")
#     float(input("Digite a nota: "))

while True:
    nota = float(input("Digite a nota: "))
    if nota >= 6:
        print("Este aluno está Aprovado! :D")
    else:
        print("Este aluno está reprovado! :(")
        break