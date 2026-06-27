# Dada uma lista numérica, retorne apenas os números positivos

entrada = input("Digite números inteiros positivos e negativos separados por espaços: ")

numeros = [int(x) for x in entrada.split()]

positivos = [num for num in numeros if num > 0]

print("Números positivos encontrados na lista de entrada: {}".format(positivos))