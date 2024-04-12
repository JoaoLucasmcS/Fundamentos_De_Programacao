#Nesse exercício o usuário digita a idade do imóvel e o programa responde se ele é novo, moderamente antigo ou antigo.
idadeImovel = int(input("Digite a idade do imóvel: "))

if(idadeImovel<=10):
    print("Seu imóvel é novo")

elif(idadeImovel>10 and idadeImovel<30):
    print("Seu imóvel é moderamente antigo")

else:
    print("Seu imóvel é antigo")
