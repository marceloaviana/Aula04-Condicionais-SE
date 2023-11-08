# Exercicio 5

idade = int(input("Digite a sua idade: "))

if idade < 18:
  print("Você é menor de idade")
elif idade >= 18 and idade < 65:
  print("Você é um adulto")
elif idade >= 65 and idade < 100:
  print("Você é um idoso")
else:
  print("Fazendo hora extra")


# Exercicio 6

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda noita: "))

media = (n1 + n2) / 2
print("Média: ", media)

if media >=6:
  print("Aluno aprovado!")
else:
  print("Aluno reprovado!")


# Exercicio 7

print("Digite a nota 1: ")
n1 = float(input())

print("Digite a nota 2: ")
n2 = float(input())

media = (n1 + n2) / 2
print("Média = ", media)

if media >= 6:
  print("Aluno aprovado!")
elif media < 6:
  print("Aluno de recuperação!")
  print("Digite a nota da recuperação: ")
  n3 = float(input())
  exame = (media + n3) / 2
  if exame >= 6:
    print("Média final = ", exame)
    print("Aluno aprovado!")
  else:
    print("Média final = ", exame)
    print("Aluno reprovado!")


# Exercico 8

numero = int(input("Digite um número: "))

if numero % 2 == 0:
  print(f"O número {numero} é par!")
else:
  print(f"O número {numero} é ímpar!")


# Exercicio 9 

n1 = int(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
n2 = int(input("Digite o segundo número: "))

if operador == "+":
  resultado = n1 + n2

elif operador == "-":
  resultado = n1 - n2

elif operador == "*":
  resultado = n1 * n2

elif operador == "/":
  resultado = n1 / n2

else:
  resultado = "Operação inválida"

print(f"O resultado {n1} {operador} {n2} = {resultado}")



