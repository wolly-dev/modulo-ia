# Crie um programa que calcula a média escolar de um aluno.
# O programa deve calcular a média, exibir todas as notas,
# E o resultado final:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

print(f"""As seguintes notas:
{nota1}
{nota2}
{nota3}
Têm como média final: {media:.2f}""")