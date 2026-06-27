'''Considere listas de listas e números. Cada lista, por sua vez, está formada por listas e números, recursivamente. 
Defina uma função achatar que retorne uma lista plana com todos os números da lista original. 
Por exemplo, achatar([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]) deverá retornar [1, 2, 4, 2, 5, 2, 1, 2, 3, 1, 8]. 
Dê duas versões, uma sem compreensões e outra com compreensões. 
A versão com compreensões não precisa retornar os elementos na ordem em que aparecem os números de esquerda à direita.'''
def achatar(lista):
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado += achatar(item)
        else:
            resultado.append(item)
    return resultado

lista_inicial = list(input("Digite a lista de entrada:"))

print(achatar(lista_inicial))