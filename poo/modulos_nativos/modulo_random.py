import random as rndm

# 1 - Seleciona valor aleatório de uma lista
list1 = [7, 6, 5, 4, 3, 2, 1]
print(rndm.choice(list1))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = rndm.randint(5, 15)
print(r1)

# 3 - Seleciona caractere aleatória de uma string
name = "Curso Python"
r2 = rndm.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatório
# rndm.sample(sequencia, tamanho)
print(rndm.sample(list1, 2))
print(rndm.sample(list1, 3))
s = "Olá Mundo"
print(rndm.sample(s, 2))

# 5 - Programa de Sorteio
done = False
while not done:
    print("O que você deseja fazer:")
    print("1. Adivinhar o número")
    print("2. Sair")

    choice = input(">")
    if choice == "1":
        print("===============Adivinhe m número de 1 a 10:===============\n")
        number = int(input("Digite um número de 1 a 10:\n"))
        result = rndm.randint(1, 10)
        if number == result:
            print("Parabéns. Você acertou")
        else:
            print(f"Tente novamente. O número sorteado foi: {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção Inválida. Escolha a opção 01 ou 02.")
