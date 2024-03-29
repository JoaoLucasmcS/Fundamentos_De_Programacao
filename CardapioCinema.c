\\O programa apresenta o cardápio e atende o usuário com quantos pedidos for necessário. No final o programa mostra o valor total da compra.\\


#include <stdio.h>

int main() {
  char resposta;
  int pedido;
  float quantidadepedido;
  float valordacompra;

  printf("Deseja fazer um pedido? (s/n)\n");
  scanf("%c", &resposta);

  while(resposta == 's'){
    printf(" 100.  Pipoca---------R$ 20,00\n");
    printf(" 101.  Refrigerante---R$ 09,30\n");
    printf(" 102.  Chocolate------R$ 05,50\n");
    printf(" 103.  Água --------- R$ 02,00\n");

    printf("\nDigite o código do produto que você quer: ");
    scanf("%d", &pedido);

    printf("Quantos itens desse produto você deseja: \n");
    scanf("%f", &quantidadepedido);

    switch(pedido){
      case 100: valordacompra = quantidadepedido*20;
      break;
      case 101: valordacompra = quantidadepedido*9.30;
      break;
      case 102: valordacompra = quantidadepedido*5.5;
      break;
      case 103: valordacompra = quantidadepedido*2;
      break;
    }
   
    printf("Deseja fazer outro pedido? (s/n)\n");
    scanf(" %c", &resposta);
    }

  
  printf("O valor da sua compra foi de R$ %.1f", valordacompra);
  
}