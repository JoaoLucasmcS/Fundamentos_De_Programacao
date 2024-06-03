import os 
os.system("cls")

matriz = [[], [], [], []]
regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
soma = 0

for r in range(5):
    for t in range(4):
        matriz[t].append(float(input(f"Digite o número de vendas do {t+1}º trimestre na região {regioes[r]}: ")))
        soma += matriz[t][r]

print(f"O número total de vendas é: {soma}")
