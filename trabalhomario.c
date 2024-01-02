#include <stdio.h>
#include <cs50.h>

// receber a altura da pirâmide
int main(void) {
    int h, i, j;
    do {
        h = get_int("Insira a altura da pirâmide (nota: tem que constar entre 1 e 9): ");
    } while (h < 1 || h > 9);
    for (i = 0; i < h; i++) {
        // imprimir os espaços
        for (j = h - i; j > 0; j--)
            printf(" ");
        // inprimir pirâmide esquerda
        for (j = 0; j <= i; j++)
            printf("#");
        // imprimir espaços
        printf("  ");
        // impirmir pirâmide direita
        for (j = 0; j <= i; j++)
            printf("#");
        printf("\n");
    }
    // imprimir base
    for (j = 0; j < 2 * h + 6; j++) {
        printf("=");
    }
    printf("\n");
    return 0;
}
