numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
pares = [x for x in numeros if x % 2 == 0]

if pares:
    media = sum(pares) / len(pares)
    print(f"A média dos números pares é: {media:.2f}")
else:
    print("Não há números pares na lista.")
