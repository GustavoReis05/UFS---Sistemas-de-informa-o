# Contar quantidade de vogais de uma string

palavra = input("Digite uma palavra para verificar o numero de vogais: ")
vogais = [1 for letra in palavra if letra in "aeiouAEIOU"]
total_vogais = sum(vogais)
print("A palavra {}, possui um total de {} vogais.".format(palavra, total_vogais))
