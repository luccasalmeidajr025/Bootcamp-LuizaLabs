# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]
if palavra.lower() == palavra_invertida.lower():
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
    