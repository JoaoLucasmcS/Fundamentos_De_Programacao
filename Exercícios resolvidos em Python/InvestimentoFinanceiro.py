#Esse programa simula um ivestimento financeiro, recebendo do usuário o valor inicial do investimento, a taxa de juros anual (em porcentagem) e  o número de anos para o investimento. Depois disso, o programa mostra ao usuário o valor do investimento ao final de cada ano. O usuário tem a opção de fazer múltiplas simulações de investimento antes de encerrar o programa.

valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxaJuros = float(input("Digite o valor da taxa de juros anual: "))
quant_anos = int(input("Por quantos anos você deseja investir:  "))
saldo = valor_inicial
continuar = 's'
while(continuar == 's' or continuar == 'S'):
    for ano in range (1, quant_anos + 1):
        saldo *= 1 + taxaJuros/100
        print(f"Saldo após o ano {ano} : R$ {saldo:.2f}")

    continuar = input("Deseja fazer outra simulação? (S/N)").lower()

    


