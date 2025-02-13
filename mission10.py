# Missão 10: Crie uma função que receba um nome e diga quantas letras esse nome tem.

quantidade_aluno = int(input("Qual a quantidade de alunos?"))

alunos_registrados = ([])

controle = 0


while controle < quantidade_aluno:
    aluno = input("Digite o primeiro nome do aluno: ")
    print(len(aluno))
    alunos_registrados.append(aluno)
    controle += 1
    print(alunos_registrados)
