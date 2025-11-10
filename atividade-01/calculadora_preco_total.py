# Desenvolva um programa que calcula o preço total de uma compra.
# Use as seguintes informações:

# * Nome do produto: "Cadeira infantil"
# * Preço unitário: R$ 12.40
# * Quantidade: 3
# O programa deve calcular o preço total e exibir
# todas as informações, incluindo o resultado final.

produto = "Cadeira infantil"
produtoPreco = 12.40
produtoQtd = 3
print(f"""Nome do produto: {produto}.
Preço do produto: R${produtoPreco:.2f}.
Quantidade: {produtoQtd}.
Total do preço: R${produtoPreco*produtoQtd:.2f}

""")