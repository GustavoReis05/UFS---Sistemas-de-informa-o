# Gere uma lista contendo o tamanho de cada palavra. Ex de entrada: ["python", "java", "javascript", "c"]

lista_palavras = []
palavras = input("Digite uma lista de palavras separadas por espaço para saber quantas vogais existem em cada uma: ")
lista_palavras = palavras.split()
tamanhos = [len(palavra) for palavra in lista_palavras]
print("As palavras {}, possuem os respectivos numeros de vogais {}.".format(lista_palavras, tamanhos))
