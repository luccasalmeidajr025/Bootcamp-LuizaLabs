# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

texto = input("Digite uma string: ")
num = int(input("Digite um número inteiro: "))
resultado = " ".join([texto] * num)
print("O resultado da repetição é:", resultado)
