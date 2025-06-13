#include <stdio.h>

void modificar_por_referencia(int* ponteiro_numero) {
    printf("  -> Dentro da função (antes): %d\n", *ponteiro_numero);
    *ponteiro_numero = 100;
    printf("  -> Dentro da função (depois): %d\n", *ponteiro_numero);
}

int main() {
    int valor_original = 10;
    printf("Valor original (antes): %d\n", valor_original);

    modificar_por_referencia(&valor_original); 
    
    printf("Valor original (depois): %d\n", valor_original);
    return 0;
}