# Desenvolva um programa que calcula o ocnsume médio de combustível de um veículo
# Use os seguintes dados:

# * Distancia percorrida: 300km
# * Combustivel gasto: 25 litros

# O programa deve calcular o consumo médio (km/l) e exibir
# Todos os dados da viagem, incluindo o resultado final
# Arredondado para duas casas decimais:

kmPercorrido = 300
combustivelGasto = 25
gastoPorKm = kmPercorrido / combustivelGasto
print(f"""Em uma viagem de {kmPercorrido}km onde foram gastos {combustivelGasto}l de combustível,
Foi percorrido {gastoPorKm}km por litro de combustível na viagem.""")