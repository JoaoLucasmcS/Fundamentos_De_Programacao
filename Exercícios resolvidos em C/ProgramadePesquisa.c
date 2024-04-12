\\ O programa para 10 mulheres, uma por uma, a quantidade de filhos que elas possuem. Depois o programa exibe a quantidade de mulheres que tem até dois filhos e a quantidade de mulheres que tem mais de dois filhos. \\

#include <stdio.h>

int main() {
  int contador = 1;
  int mais2filhos = 0;
  int atedoisfilhos = 0;
  int filhos;


  while(contador<=10){
    printf("\nDigite quantos filhos você possui: ");
    scanf("%d", &filhos);

      if(filhos >= 0 && filhos <= 2){
         atedoisfilhos++;
      }
      else if(filhos > 2 ){
        mais2filhos++;
      }
      else{
        printf("Número de filhos inválido");
      }
    contador++;
  }
  printf("\nA quantidade de mulheres que tem até dois filhos é: %d ", atedoisfilhos);
  printf("\nA quantidade de mulheres que tem mais de dois filhos é: %d" , mais2filhos);
}