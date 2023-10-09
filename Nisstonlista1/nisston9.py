nomes = input("Digite uma lista de nomes separados por espaço: ").split()
nomes_com_a = [nome for nome in nomes if nome.startswith('A') or nome.startswith('a')]

if nomes_com_a:
    print("Nomes que começam com 'A':", nomes_com_a)
else:
    print("Nenhum nome começa com 'A'.")
