\\ O usuário digita 2 números e o programa mostra as 4 operações feitas com esses dois números. \\

#include <stdio.h>
#include <math.h>

int main(void) {
  float n1, n2;

  printf("Digite o primeiro número: ");
  scanf("%f", &n1);

  printf("Digite o segundo número: ");
  scanf("%f", &n2);

  printf("\nSoma = %.1f\n", n1+n2);
  printf("Subtração = %.1f\n", n1-n2);
  printf("Multiplicação = %.1f\n", n1*n2);
  printf("Divisão = %.1f\n", n1/n2);


}