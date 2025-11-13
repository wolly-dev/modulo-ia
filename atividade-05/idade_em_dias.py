# %%
import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano = int(input("Em que ano você nasceu? "))
idade_em_dias = calcular_idade_em_dias(ano)
print(f"Voce nasceu há aproximadamente {idade_em_dias} dias!")
# %%
