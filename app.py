print("Olá, mundo!")

a = 10
b = 5

print(a+b) #soma
print(a-b) #subtração
print(a*b) #multiplicação
print(a/b) #divisão
print(a//b) #divisão inteira
print(a%b) #resto da divisão
print(2**b) # potenciação

# operações de comparação

print (a==b) # false -> a é igual a b?
print (a!=b) #true -> a é diferente de b?
print (a > b) #true -> a é maior que b?
print (a < b) #true -> a é menor que b?
print (a >= b) #false -> a é maior que b?

# operadores lógicos

print (True and False) #false - > o and exige que os dois sejam verdadeiros
print (True or False) #true - > o or exige que apenas um seja verdadeiro
print (not True ) #false - > inverte o valor 

tem_carteira = True
idade = 17
print(tem_carteira and idade >= 18) # false 

#convertendo texto em número

# valor vai sair como se fosse um string 
valor = input("Digite um número")
print (valor, type(valor))
print (valor + valor)

# int() converte para inteiro
# float() converte para decimal
# str() converte para texto

#forma "correta"

valor = int(input("Digite um número"))
print (valor, type(valor))
print (valor + valor)

# F-string, meio que uma concatenação

nome = "ana"
nota = 8.5434234

print(f"O aluno {nome} passou de ano com nota {nota}")
print(f"O aluno {nome} passou de ano com nota {nota:.2f}")
print(f"O aluno {nome} passou de ano com nota {nota * 2}")

# estrutura IF - condicional 

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação") 
else:
    print("Reprovação, vergonha, desgraça")


peso = float(input("Peso (kg):"))
altura = float(input("Altura (m):"))

if not (0 < peso < 400 and 0 < altura <3):
    print("Dados fora da faixa esperada.")