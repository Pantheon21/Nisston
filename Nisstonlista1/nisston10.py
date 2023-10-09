import random

opcoes = ["Pedra", "Papel", "Tesoura"]
escolha_usuario = input("Escolha Pedra, Papel ou Tesoura: ")
escolha_computador = random.choice(opcoes)

print(f"Você escolheu: {escolha_usuario}")
print(f"Computador escolheu: {escolha_computador}")

if escolha_usuario == escolha_computador:
    print("Empate!")
elif (escolha_usuario == "Pedra" and escolha_computador == "Tesoura") or \
     (escolha_usuario == "Papel" and escolha_computador == "Pedra") or \
     (escolha_usuario == "Tesoura" and escolha_computador == "Papel"):
    print("Você venceu!")
else:
    print("Computador venceu!")
