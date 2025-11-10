# Desenvolva um programa que calcule o desconto em uma loja.
# Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$50.00
# * Porcentagem doe desconto: 20%

# O programa deve calcular o valor do desconto e o preço final,
# Exibindo todos os detalhes.

produto = "Camiseta"
precoProduto = 50.00
desconto = 20/100

produtoDesconto = precoProduto - (desconto*precoProduto)

print(f"O produto {produto} que custa R${precoProduto:.2f}, com um desconto de 20%, passa a custar: R${produtoDesconto:.2f}")