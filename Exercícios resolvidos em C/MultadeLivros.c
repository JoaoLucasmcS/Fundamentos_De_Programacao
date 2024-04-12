\\ O usuário digita a quantidade de dias que ficou com o livro e o programa calcula a multa. \\

#include <stdio.h>

int main() {
    float d;
    printf("Digite a quantidade de dias que você ficou com o livro: ");
    scanf("%f", &d);

    if (d <= 7) {
        printf("A multa é de: %.1f reais", 0.5 * d);
    } else if (d >= 8 && d <= 14) {
        printf("A multa é de: %.1f reais", 1.0 * d);
    } else {
        printf("A multa é de: %.1f reais", 2.0 * d);
    }
}
