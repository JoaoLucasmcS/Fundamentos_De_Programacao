\\ O usuário digita o seu peso e a altura. O programa calcula o índice de massa corporal. \\

#include <stdio.h>

int main() {
 float peso, altura;

  printf("Declare o peso da pessoa em kg: ");
  scanf("%f", &peso);

  printf("Declare a altura da pessoa em metro: ");
  scanf("%f", &altura);

  printf("\nO índice de massa corporal da pessoa é: %.2f", peso/(altura*altura));
}