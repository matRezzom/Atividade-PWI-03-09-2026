# 7

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

if (nota1 + nota2 + nota3)/ 3 >= 7:
    print("Você passou, parabéns, Aprovado")
elif (nota1 + nota2 + nota3) / 3 <= 6.9 and (nota1 + nota2 + nota3) / 3 >= 4:
    print("Recuperação parça")
else:
    print("Reprovado")
