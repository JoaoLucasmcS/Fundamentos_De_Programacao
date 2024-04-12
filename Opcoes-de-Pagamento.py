#Esse exercício mostra 3 opções de pagar uma bolsa cujo valor é digitado pelo usuário
valor_bolsa = float(input("Digite o valor da bolsa: "))

valor_avista = valor_bolsa - (valor_bolsa * 10/100)
parcela3 = valor_bolsa/3
valor_parcelado10 = valor_bolsa + (valor_bolsa * 5/100)
parcela10 = valor_parcelado10/10

print("\nPreço a vista: R$", valor_avista)
print(f"\nPreço final da bolsa parcelada em 3x: R$ {valor_bolsa:.2f}")
print(f"Valor das 3 parcelas: R$ {parcela3:.2f}")
print(f"\nPreço final da bolsa parcelada em 10x: R$ {valor_parcelado10:.2f}")
print(f"Valor das 10 parcelas: R$ {parcela10:.2f}")

