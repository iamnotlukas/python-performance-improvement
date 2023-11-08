# Lê três números do usuário
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# Cria uma lista com os números
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros_ordenados = sorted(numeros, reverse=True)

# Imprime os números em ordem decrescente
print('Os números em ordem decrescente são:', numeros_ordenados)
