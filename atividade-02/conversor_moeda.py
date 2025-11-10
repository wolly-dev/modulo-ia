# Crie um programa que converte um valor em reais para dólares e euros
# Use os seguintes dados:

# * Valor em reais: R$100.00
# * Taxa do dólar: R$5.20
# * Taxa do euro: R$6.15

#O programa deve calcular e exibir os valores convertidos,
# Arredondando para duas casas decimais

#valorReal = 100.00
#dolarTaxa = 5.20
#euroTaxa = 6.15
#print(f"""Valor em reais: R${valorReal:.2f}.
#Convertido para dólar: ${valorReal/dolarTaxa:.2f}.
#Convertido para Euro: ${valorReal/euroTaxa:.2f}.

#""")

valorReal = float(input("Digite o valor em reais a ser convertido: "))
dolarTaxa = 5.20
euroTaxa = 6.15

print(f"""O valor digitado foi: R${valorReal:.2f}.
Convertido para dólar: ${valorReal/dolarTaxa:.2f}.
Convertido para euro: ${valorReal/euroTaxa:.2f}.
""")