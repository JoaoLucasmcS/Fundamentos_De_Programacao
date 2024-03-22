\\ O usuário digita o valor em dólar e o programa mostra o mesmo convertido para real. \\

#include <stdio.h>
#include <math.h>

int main() {
  float num;

  printf("Digite o valor em dólar: " );
  scanf("%f", &num);

  printf("\nO valor em real é igual a:  %.2f", num/4.94);

}
  