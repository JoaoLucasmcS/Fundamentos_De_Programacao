# Esse programa simula um funcionamento de saques de um caixa eletrônico

saldo = 1000.0
resposta = input("Você deseja realizar um saque? (S/N)")

while(resposta == 's' or resposta == 'S'):
    
    valor_saque = float(input("Digite o valor que você quer sacar: "))
    if(valor_saque > saldo):
        print("Saldo insuficiente")
    elif(valor_saque <= 0):
        print("Valor inválido")
    else:
        saldo -= valor_saque
        print("Saque realizado com sucesso")
        print(f"Seu novo saldo é de {saldo:.2f}")

    resposta = input("Você deseja realizar outro saque? (S/N)")
print("Obrigado por usar o simulador de caixa eletrônico!")    