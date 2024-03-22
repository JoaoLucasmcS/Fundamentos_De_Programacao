\\ O usuário digita a velocidade do carro e o programa calcula a multa (caso ele tenha ultrapassado o limite de velocidade).\\

#include <stdio.h>

int main() {
  int v;
  printf("Digite a velocidade: ");
  scanf("%d", &v);
  
      if(v>80 && v<100){
        printf("Você ultrapassou o limite de velocidade\n");
        printf("O valor da multa é: %d reais\n" , (v-80)*5);
      }
      else if(v>=100){
        printf("Você ultrapassou o limite de velocidade\n");
        printf("O valor da multa é: %d reais\n" , (v-80)*10);
      }
      else (printf("Você está no limite correto de velocidade.")); 
  
}

