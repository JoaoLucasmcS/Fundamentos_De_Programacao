# Esse exercício calcula o valor da compra pra festa no escritório e o valor que fica para cada um que vai participar da cotinha

bolo = float (input("Digite o valor do bolo: "))
valor_salgado = float (input("Digite o valor do salgado: "))
quant_salgado = float(input("Digite a quantidade de salgados comprados: "))

valor_final = bolo + (valor_salgado*quant_salgado)
valor_unit = valor_final/11

print(f"O valor final da compra foi de : R$ {valor_final:.2f}")
print(f"O valor a ser pago por cada um é de: R$ {valor_unit:.2f}")