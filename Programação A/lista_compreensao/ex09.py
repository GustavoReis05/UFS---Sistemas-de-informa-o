# Crie uma lista com todos os números primos de 1 a n

n = int(input("Digite o ultimo numero da sequencia que deve ser avaliada:"))

primos = [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, x))]

print("Os numeros primos presentes entre 1 e {} são os seguintes: {}".format(n, primos))