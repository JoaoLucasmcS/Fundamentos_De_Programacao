# Este programa mostra o fatorial de um número digitado pelo usuário

resposta = 's'

while(resposta == 's' or resposta == 'S'):
    numero = int(input("Digite o número o qual você deseja calcular o fatorial: "))
    if(numero == 1 or numero == 0):
        fat = 1   

    else:
        fat = 1

        while(numero > 1 ):       
            fat *= numero
            numero -= 1

    print("O fatorial é:", fat)
    resposta = input("Você deseja calcular o fatorial de outro número? (S/N)")
print("Obrigo por utlizar a calculadora de fatorial!")    
    


        