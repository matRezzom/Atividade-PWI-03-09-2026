# 8

nome = input("Digite seu nome:")
peso = float(input("Peso (kg):"))
altura = float(input("Altura (m):"))

if not (0 < peso < 400 and 0 < altura <3):
    print("Dados fora da faixa esperada.")
else:
    imc = peso / (altura ** 2)
    print (f"{nome} seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidade") 