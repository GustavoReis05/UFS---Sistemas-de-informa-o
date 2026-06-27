# Dada uma lista com nomes, filtrar palavras maiores que 5 letras

nomes_entrada = input("Digite os nomes separados por espaço: ").split()

maiores_que_5 = [nome for nome in nomes_entrada if len(nome) > 5]
print("Lista original: {}".format(nomes_entrada))
print("Palavras com mais de 5 letras:", maiores_que_5)