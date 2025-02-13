# Missão 03: Criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

while True:
    nota = float(input("Digite a sua nota: "))

    if 90 <= nota <= 100:
        print("Parabéns, você tirou um A")
    elif 80 <= nota <= 89:
        print("Muito bem, você tirou um B")
    elif 70 <= nota <= 79:
        print("Bom trabalho, você tirou um C")
    elif 60 <= nota <= 69:
        print("Fique atento, você tirou um D")
    else:
        print("Estude um pouco mais, você tirou um F")