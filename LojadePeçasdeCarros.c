\\ O programa oferece 4 produtos para o usuário escolher e depois pergunta qual quantidade que ele deseja. O programa mostra ao usuário o preço final da sua compra. \\

#include <stdio.h>

int main() {
  int num1, num2;

  printf("1. Bateria - 200 reais\n");
  printf("2. Pneu - 350 reais\n");
  printf("3. Filtro de óleo - 20 reais\n");
  printf("4. Pastilhas de freio - 100 reais\n");

  printf("\nDigite qual produto você vai querer:\n");
  scanf("%d", &num1);

  printf("\nQuantos itens você deseja adquirir?\n ");
  scanf("%d", &num2);

  switch(num1) {
   case 1: 
    printf("\nO valor da sua compra foi: %d reais", 200*num2);
    break;
   case 2: 
    printf("\nO valor da sua compra foi: %d reais", 350*num2);
  break;
   case 3: 
     printf("\nO valor da sua compra foi: %d reais", 20*num2);
  break;
   case 4: 
    printf("\nO valor da sua compra foi: %d reais", 100*num2);
  break;
  default:
      printf("Número inválido");
  }
}