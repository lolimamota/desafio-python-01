# Missão 9: Criar uma função que receba um número e retorne o dobro do seu valor.

# ➡️ Exemplo: dobro(5)
# ➡️ Saída: "O dobro de 5 é 10"

number = int(input("Insira um número para descobrir o dobro: "))

def double(number):
    result = number * 2
    print(f"O dobro de {number} é : {result}")

double(number)