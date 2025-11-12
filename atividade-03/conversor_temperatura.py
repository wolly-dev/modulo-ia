# Crie um programa que converta temperaturas entre:
# * Celsius
# * Fahrenheit
# * kelvin
# O usuário deve informar a temperatura, a unidade de origem e a unidade
# Para a qual deseja converter.
# %%
escalaOrigem = int(input("""Para que escala de temperatura deseja fazer a conversão?
1- Celsius
2- Fahrenheit
3- Kelvin
"""))

temperatura = float(input("Digite a temperatura: "))
match escalaOrigem:
    case 1:
        print("Você escolheu Celsius como origem.")

        escalaDestino = int(input("""Digite para que escala deseja converter:
        1- Fahrenheit
        2- Kelvin
        """))
        match escalaDestino:
            case 1:
                celsius_fahrenheit = (temperatura * 9/5) + 32
                print("Escolheu Fahrenheit como destino.")
                print(f"{temperatura:.2f}°C convertido para Fahrenheit é {celsius_fahrenheit:.2f}°F!")

            case 2:
                celsius_kelvin = temperatura + 273.15
                print("Escolheu Kelvin como destino.")
                print(f"{temperatura:.2f}°C convertido para Kelvin é {celsius_kelvin:.2f}K!")
# Daqui pra trás está correto!
    case 2:
        print("Você escolheu Fahrenheit como origem.")

        escalaDestino = int(input("""Digite para que escala deseja converter:
        1- Celsius
        2- Kelvin
        """))
        match escalaDestino:
            case 1:
                fahrenheit_celsius = (temperatura - 32) * 5/9
                print("Escolheu Celsius como destino.")
                print(f"{temperatura:.2f}°F convertido para Celsius é {fahrenheit_celsius:.2f}°C!")

            case 2:
                fahrenheit_kelvin = (temperatura - 32) * 5/9 + 273.15
                print("Escolheu kelvin como destino.")
                print(f"{temperatura:.2f}°C convertido para Kelvin é {fahrenheit_kelvin:.2f}K!")
    case 3:
        print("Você escolheu Kelvin como origem.")

        escalaDestino = int(input("""Digite para que escala deseja converter:
        1- Celsius
        2- Fahrenheit
        """))
        match escalaDestino:
            case 1:
                kelvin_celsius = temperatura - 273.15
                print("Escolheu Celsius como destino.")
                print(f"{temperatura:.2f}K convertido para Celsius é {kelvin_celsius:.2f}°C!")

            case 2:
                kelvin_fahrenheit = (temperatura - 273.15) * 9/5 + 32
                print("Escolheu Fahrenheit como destino.")
                print(f"{temperatura:.2f}K convertido para Kelvin é {kelvin_fahrenheit:.2f}°F!")


# %%
