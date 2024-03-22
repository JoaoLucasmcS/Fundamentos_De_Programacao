\\ O usuário digita sua idade e o programa mostra se ele é de maior ou de menor. \\

#include <stdio.h>

int main() {
  int idade;

  printf("Digite a idade: ");
  scanf("%d", &idade);

  if(idade>=18){
    printf("\nA pessoa é de maior.");
   }
  else{
    printf("\nA pessoa é de menor.");
  }
  
}
  
