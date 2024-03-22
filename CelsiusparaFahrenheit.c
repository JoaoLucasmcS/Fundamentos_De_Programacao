\\ O usuário digita a temperatura em celsius e o programa mostra a conversão para fahrenheit. \\

#include <stdio.h>

int main() {
  float c;

  printf("Digite a temperatura em celsius: ");
  scanf("%f", &c);

  printf("\nA temperatura em fahrenheit é :  %.2f", c*1.8+32);
}