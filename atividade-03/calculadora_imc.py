# Desenvolva um programa que calcule o índice de Massa Corpotal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) du usuário,
# Calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC:

# * < 18.5: classificacao = "Abaixo do peso"
# * < 25: classificacao = "Peso normal"
# * < 30: classificacao = "Sobrepeso"
# * Para os demais cenários: classificacao = "Obeso"
# peso/(altura x altura)

peso = float(input("Digite seu peso em kgs: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é de: {imc:.2f}. Classificação:")

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Normal.")
elif imc < 30:
    print("Sobrepeso.")
else:
    print("Obeso.")