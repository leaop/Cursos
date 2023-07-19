#include <stdio.h> // conumicacao com o usuário
#include <stdlib.h> // alocacao de espaço na memória
#include <locale.h> //alocacao de texto


int main()
{
    setlocale(LC_ALL, "Portuguese");
    printf("### Cartório da EBAC ###\n\n");
    printf("Escolha a opcao de desejada no menu:\n\n");
    printf("\t1 - Registrar nomes\n");
    printf("\t2 - Consultar nomes\n");
    printf("\t3 - Deletar nomes\n\n");
    printf("Esse Software é de livre uso dos alunos\n");


}