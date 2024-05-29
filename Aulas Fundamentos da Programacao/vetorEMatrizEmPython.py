"""Desenvolva um programa que receba do usuário cinco valores inteiros e guarde em um vetor (lista). Ao final,mostre os valores na tela."""

valores = []

for i in range (5):
    valores.append(int(input("Digite um novo valor apra ser adicionado em uma array: ")))

print(valores)


"""Desenvolva um programa que receba valores inteiros e guarde em um vetor (lista). O programa deve continuar solicitando valores até que o usuário insira o valor 0 para indicar o fim da entrada.. Ao final, mostre os valores na tela."""

valores = []

while True:
    valor = int(input("Digite um novo valor para ser adicionado em uma array: (0 para parar) "))
    if valor == 0:
        break
    else: 
        valores.append(valor)

print("Os valores informados foram: ", valores)


"""Adicionar valores em uma Matriz 2x4! Exibir a matriz na tela."""

matriz = [[],[]]

for linha in range(2):
    for coluna in range(4):
        matriz[linha].append(int(input(f"Digite o valor para a posição [{linha}] [{coluna}]: ")))

for linha in matriz:
    print(linha)        

"""Adicionar valores em uma Matriz 4x2! Exibir a matriz na tela."""

matriz = [[],[],[],[]]

for linha in range(4):
    for coluna in range(2):
        matriz[linha].append(int(input(f"Digite o valor para a posição [{linha}] [{coluna}]: ")))

for linha in matriz:
    print(linha)


