# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))    
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2 
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Erro: Operação inválida."
print("O resultado da operação é:", resultado)

