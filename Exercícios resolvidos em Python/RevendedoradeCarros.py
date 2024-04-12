#O programa lê o número de carros vendidos, o valor total das suas vendas , seu salário fixo e a comissão que ele recebe por cada carro vendido

carros_vendidos = float(input("Digite o valor de carros vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas: "))
salario_fixo = float(input("Digite qual salário fixo: "))
valor_comissao = float(input("Digite o valor da comissão pra cada carro vendido: "))

salaraio_final =  (valor_comissao*carros_vendidos) + (valor_vendas*0.05) + salario_fixo

print(f"O salário dinal do vendedor é R$: {salaraio_final:.2f}")

