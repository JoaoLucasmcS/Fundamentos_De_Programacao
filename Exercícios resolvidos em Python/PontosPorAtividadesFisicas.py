#Esse programa recebe quantas horas você fez de atividade física e converte para pontos.

horas = float(input("Digite a quantidade de horas em que você praticou atividade física: "))


if (horas>0 and horas<10):
    pontos_totais = horas*2

elif(horas>=10 and horas<20):
    pontos_totais = horas*5

else:
    pontos_totais = horas*10

print(f"A quantidade de pontos que você possui é: {pontos_totais:.2f}")