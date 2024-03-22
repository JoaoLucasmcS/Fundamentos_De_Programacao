\\ O usuário digita o salário inicial. O programa calcula o valor do acréscimo e o novo salário. \\

#include <stdio.h>
#include <math.h>

int main() {
  float si, sf, va;

  printf("Digite o salário inicial: ");
  scanf("%f", &si);

  va = (si/10); 
  printf("O valor do acréscimo é igual a: %.1f\n", va);

  sf = (si+va);
  printf("Seu salário com acréscimo é igual a: %.1f", sf);
  
}