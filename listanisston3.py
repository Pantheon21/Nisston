def calcular_media(notas):
    return sum(notas) / len(notas)

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def eh_palindromo(texto):
    texto = texto.replace(" ", "").replace(",", "").replace(".", "").lower()
    return texto == texto[::-1]

def soma_digitos(numero):
    return sum(map(int, str(numero)))

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Escolha uma opção:")
    print("1. Calcular média de notas e verificar aprovação/reprovação.")
    print("2. Calcular fatorial de um número inteiro positivo.")
    print("3. Verificar se uma palavra/frase é um palíndromo.")
    print("4. Calcular a soma dos dígitos de um número inteiro positivo.")
    print("5. Verificar se um número é primo.")
    print("6. Contar vogais em uma string.")
    print("7. Calcular IMC (Índice de Massa Corporal).")
    print("8. Converter temperatura (Celsius/Fahrenheit).")
    
    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        notas = []
        for _ in range(5):
            nota = float(input("Digite uma nota: "))
            notas.append(nota)

        media = calcular_media(notas)

        if media >= 7:
            print(f"Média: {media:.2f}. Aluno Aprovado!")
        else:
            print(f"Média: {media:.2f}. Aluno Reprovado.")
    
    elif escolha == 2:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("O número deve ser positivo.")
        else:
            fatorial = calcular_fatorial(numero)
            print(f"{numero}! = {fatorial}")
    
    elif escolha == 3:
        frase = input("Digite uma palavra ou frase: ")
        if eh_palindromo(frase):
            print("É um palíndromo.")
        else:
            print("Não é um palíndromo.")
    
    elif escolha == 4:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("O número deve ser positivo.")
        else:
            soma = soma_digitos(numero)
            print(f"A soma dos dígitos de {numero} é {soma}.")
    
    elif escolha == 5:
        numero = int(input("Digite um número inteiro: "))
        if eh_primo(numero):
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")
    
    elif escolha == 6:
        texto = input("Digite uma string: ")
        qtd_vogais = contar_vogais(texto)
        print(f"A quantidade de vogais na string é: {qtd_vogais}")
    
    elif escolha == 7:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
    
    elif escolha == 8:
        print("Escolha a conversão:")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        opcao = int(input("Digite 1 ou 2: "))
        
        if opcao == 1:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C é igual a {fahrenheit:.2f}°F.")
        elif opcao == 2:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F é igual a {celsius:.2f}°C.")
        else:
            print("Opção inválida.")
    
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()

