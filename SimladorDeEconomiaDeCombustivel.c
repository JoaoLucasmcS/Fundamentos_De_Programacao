\\ O usuário digita o tipo do veículo, distância em km, consumo médio de combustível do veículo e o preço médio do combustível. O programa mostra a quantidade total de combustível utilizada na vaigem, o custo total do combustível necessário e o custo com um desconto de 10%. Logo em seguida, pergunta ao usuário se deseja simular outra viagem, caso não encerra o programa. \\

#include <stdio.h>

int main() {
char veiculo_tipo[20], continuar;
float distancia, consumo_medio, preco_medio, quantidade_combustivel;

do{
  printf("Tipo do veículo (Carro, Caminhão, Ônibus): ");
  scanf("%s", &veiculo_tipo);
  printf("Distância a ser percorrida (em quilômetros): ");
  scanf("%f", &distancia);
  printf("Consumo médio de combustível (km/L): ");
  scanf("%f", &consumo_medio);
  printf("Preço médio do combustível por litro R$: ");
  scanf("%f", &preco_medio);

  quantidade_combustivel = distancia/consumo_medio;

  printf("\nQuantidade total de combústivel a ser usado: %.2f litros", distancia/consumo_medio);
  printf("\nCusto total do combustível: R$ %.2f",  quantidade_combustivel*preco_medio);
  printf("\nCusto total do combustível com desconto: R$ %.2f", quantidade_combustivel*(preco_medio*0.9));

  printf("\nDeseja realizar outra simulação? (s/n)\n");
  scanf(" %c", &continuar);

}while(continuar == 's' || continuar == 'S');

  printf("\nObrigado por utilizar o simulador de economia de combustível!");
  
}