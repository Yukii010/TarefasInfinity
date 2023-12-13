lista = []
pares = []
impares = []

for i in range(10):
    valor = float(input("Digite um valor: "))
    lista.append(valor)

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

qtd_pares = len(pares)
qtd_impares = len(impares)

soma_pares = sum(pares)
soma_impares = sum(impares)

print("Números pares:", pares)
print("Números ímpares:", tuple(impares))
print("Quantidade de números pares:", qtd_pares)
print("Quantidade de números ímpares:", qtd_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
