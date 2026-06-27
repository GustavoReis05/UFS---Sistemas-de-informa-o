#Faça uma lista com os números pares de uma lista de inteiros

entrada = input("Digite uma lista de inteiros separados por espaços: ")
numeros = entrada.split()

pares = [int(texto) for texto in numeros if int(texto) % 2 == 0]

print("Números pares encontrados:", pares)