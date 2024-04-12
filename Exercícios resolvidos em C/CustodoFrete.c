\\ O usuário digita a distância em km da entrega e o peso da encomenda. O programa calcula o valor do frete.\\

#include <stdio.h>

int main() {
  float d, p,f;
  printf("Digite a distância da entrega em Km: ");
  scanf("%f", &d);
  printf("Digite o peso da encomenda em Kg: ");
  scanf("%f", &p);

  if(d>100){
    f = 2*d;
  }
 else if(d<=100){
    f = 1.5*d;   
  }
  if(p>10){
    f = f+5;
  }
  printf("O custo do frete é: %.1f reais.", f);
}

