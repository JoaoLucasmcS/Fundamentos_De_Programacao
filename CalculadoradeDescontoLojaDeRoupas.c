\\ O usuário digita o valor da sua compra e quantos itens ele comprou. Dependendo da quantidade de itens que ele comprou ele ganha um certo desconto. O programa mostra o valor do desconto e o valor final da compra. Depois disso, o programa pergunta ao usuário se ele quer calcular um outro valor ou encerrar o programa. \\

#include <stdio.h>

int main() {
  float valordacompra, quantidadedeitens;
  char continuar;

      do{
      printf("Qual valor da sua compra? \n");
      scanf("%f", &valordacompra);
  
      printf("Quantos itens voce adquiriu? \n");
      scanf("%f", &quantidadedeitens);

      if(quantidadedeitens<=5){
       printf("Sua compra não possui desconto.\nO valor da sua compra foi %.1f reais.", valordacompra);
  }
     else if(quantidadedeitens>5 && quantidadedeitens<=10){
       printf("Parabéns! Voce ganhou um desconto de 5% \n");
       printf("O novo preço da sua compra é igual a %.1f reais.",valordacompra*0.95);
    }else{
       printf("Parabéns! Voce ganhou um desconto de 10% \n");
       printf("O novo preço da sua compra é igual a %.1f reais.",valordacompra*0.9);
    }
          printf("\nDeseja realizar outro cálculo? (s/n)\n");
          scanf(" %c", &continuar);
  }
        while(continuar == 's' || continuar == 'S');

      printf("Obrigado por utilizar a calculadora de descontos!\n");
        
}