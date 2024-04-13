#Esse programa lê a idade de 5 pessoas e mostra no final Quantos homens foram cadastrados, a idade da mulher mais velha, a média de idade do grupo (ambos os sexos) e quantas mulheres tem mais de 20 anos.

quantHomens = 0
idadeMulherMaisVelha = 0
somaIdades = 0 
mulheresMais20 = 0

for i in range(5):
    sexo = input("Digite o sexo da pessoa: (Masculino/Feminino)").lower()

    while sexo not in ['masculino' , 'feminino']:
        print("Sexo inválido. Por favor, digite 'Masculino' ou 'Feminino'.")
        sexo = input("Digite o sexo da pessoa: (Masculino/Feminino)").lower()

    if(sexo == 'masculino'):
        quantHomens += 1
        idadeM = int(input("Digite a idade da pessoa: "))
        somaIdades += idadeM
        print("Cadastro concluído.")

    elif(sexo == 'feminino'):
        idadeF = int(input("Digite a idade da pessoa: "))
        somaIdades += idadeF

        if idadeF > idadeMulherMaisVelha:
            idadeMulherMaisVelha = idadeF
        if idadeF > 20:
            mulheresMais20 += 1
        print("Cadastro concluído.")


mediaIdade = somaIdades / 5
print("A quantidade de homens cadastrados foram: ", quantHomens)
print("A idade da mulher mais velha foi: ", idadeMulherMaisVelha)
print("A quantidade de mulheres que possuem mais de 20 anos é: ", mulheresMais20)
print("A média de idade do grupo foi: ", mediaIdade)
