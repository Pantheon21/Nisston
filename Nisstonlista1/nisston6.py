def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("O número deve ser positivo.")
else:
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")
