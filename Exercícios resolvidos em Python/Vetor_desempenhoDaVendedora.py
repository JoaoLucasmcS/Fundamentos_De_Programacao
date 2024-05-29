"""Uma vendedora deseja analisar seu desempenho de vendas diárias.
Desenvolva um programa que:
• Solicite ao usuário a quantidade de produtos vendidos no dia.
• Crie um vetor para armazenar o peso de cada produto vendido,
onde o usuário insere o peso de cada produto.
• Calcule e exiba o peso médio das vendas.
• Identifique e exiba o maior e o menor peso vendidos.
• Considere que cada quilograma (kg) de produto vendido custa R$
4.35 e imprima o valor total arrecadado no dia."""

quantProdutos = int(input("Digite a quantidade de produtos vendidos no dia: "))

pesoProdutos = []
for i  in range (1, quantProdutos+1):
    pesoProdutos.append(float(input(f"Digite o peso do produto(kg) {i}: ")))

mediaPeso =  sum(pesoProdutos)/len(pesoProdutos)
print(f"A média de peso dos produtos é:  {mediaPeso:.2f} kg")

print(f"O maior peso vendido foi: {max(pesoProdutos)} kg")
print(f"O menor peso vendido foi: {min(pesoProdutos)} kg")

valorTotal = sum(pesoProdutos)*4.35
print(f"O preço de todos produtos vendidos foi de: R${valorTotal:.2f}") 