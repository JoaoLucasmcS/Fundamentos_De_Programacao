\\ O programa pergunta ao usuário se ele gosta de futebol até que a resposta seja 'N'. depois exibi na tela quantas pessoas gostam de futebol.  \\



#include <stdio.h>

int main() {
  char resposta;
  int contador = 0;

  printf("Voce gosta de futebol? (S/N)\n");
  scanf(" %c", &resposta);

  if(resposta == 'S'){
    while(resposta == 'S'){
      contador ++;
       printf("Voce gosta de futebol? (S/N)\n");
       scanf(" %c", &resposta);
    }
  }
  if(resposta == 'N'){
    
    printf("O número de pessoas que gostam de futebol é: %d", contador);
  }
}