# 10

COTACAO_DOLAR = 5.40

print("1 - Real para Dólar")
print("2 - Dólar para Real")
opcao = int(input("Escolha a opção: "))

if opcao != 1 and opcao != 2:
    print("Opção inválida.")
else:
    valor = float(input("Digite o valor a ser convertido: "))
    if opcao == 1:
        resultado = valor / COTACAO_DOLAR
        print(f"Resultado: US$ {resultado:.2f}")
    else:
        resultado = valor * COTACAO_DOLAR
        print(f"Resultado: R$ {resultado:.2f}")