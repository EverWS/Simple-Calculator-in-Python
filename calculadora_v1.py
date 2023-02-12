# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n")

num1 = float(input("Digite o primeiro número para operação: "))
num2 = float(input("Digite o segundo número da operação: "))

print("\n***Selecione a operação desejada***\n")
print("(+) para a soma")
print("(-) para a subtração")
print("(*) para a multiplicação")
print("(/) para a divisão\n")

operador = input("Digite aqui a operação desejada: \n")

if operador == "+":
    soma = num1 + num2
    print ("\nA soma entre {} e {} é igual a: {}\n".format(num1, num2, soma))

elif operador == "-":
    subtr = num1 + num2
    print ("\nA subtraçã entre {} e {} é igual a: {}\n".format(num1, num2, subtr))

elif operador == "*":
    multip = num1 * num2
    print ("\nA multiplicação entre {} e {} é igual a: {}\n".format(num1, num2, multip))

elif operador == "/":
    if num2 == 0.0:
        print ("\nNão existe divisão por 0.\n")
    else:
        div = num1 / num2
        print ("\nA divisão entre {} e {} é igual a: {}\n".format(num1, num2, div))

else:
    print("\nOperação inválida!\n")


