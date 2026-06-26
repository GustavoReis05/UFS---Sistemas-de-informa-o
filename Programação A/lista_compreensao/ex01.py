'''Defina uma função que leia do teclado uma sequência de números inteiros dados em uma única linha. 
A função deve retornar uma lista contendo os números que estão na linha.'''

def listaNumerica():
    return [int(x) for x in input("Digite uma lista de numeros separados por espaços: ").split()]

minha_lista = listaNumerica()

print(minha_lista)
