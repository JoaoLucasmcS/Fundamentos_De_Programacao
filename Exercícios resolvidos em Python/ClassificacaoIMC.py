#Esse programa calcula o imc do usuário e o classifica.
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

valor_imc = peso/(altura*altura)

if(valor_imc<18.5):
    print("Abaixo do peso")

elif(valor_imc>=18.5 and valor_imc<24.9):
    print("Peso ideal")

elif(valor_imc>=25 and valor_imc<30):
    print("Sobrepeso")

elif(valor_imc<18.5):
    print("Abaixo do peso")

elif(valor_imc>=30 and valor_imc<40):
    print("Obesidade")

else:
    print("Obesidade mórbida")