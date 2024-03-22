\\ O usuário digita as 3 notas e o programa calcula a média dessas. \\

#include <stdio.h>
#include <math.h>

int main() {
  float n1, n2, n3;

  printf("Digite a primeira nota: ");
  scanf("%f", &n1);

  printf("Digite a segunda nota: ");
  scanf("%f", &n2);

  printf("Digite a terceira nota: ");
  scanf("%f", &n3);

  printf("\nA média das notas é:  %.1f", (n1+n2+n3)/3);
}