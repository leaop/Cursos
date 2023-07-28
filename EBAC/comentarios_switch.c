#include <stdio.h> // conumicacao com o usuário
#include <stdlib.h> // alocacao de espaço na memória
#include <locale.h> //alocacao de texto


int main()
{
    
    int opcao=0;//definindo variáveis
// a variavel do tipo int está ocupada valendo 0, o delete só afirma que o espaço está vazio, não que necessariamente deletou
    int laco=1;

    for(laco=1;laco=1;)
    {

    
        setlocale(LC_ALL, "Portuguese");//linguagem definida

        system("cls");
        
        printf("### Cartorio da EBAC###/n/n");//inicio do menu
        printf("Escolha a opcao de desejada no menu:\n\n");
        printf("\t1 - Registrar nomes\n");
        printf("\t2 - Consultar nomes\n");
        printf("\t3 - Deletar nomes\n\n");
        printf("Opção final:");// final do menu

        scanf("%d", &opcao);// armazenar na variavel opcao o valor digitado pelo usuario

        
        switch(opcao)//para diminuir o codigo refazendo o if
        //caso a variavel tenha determinado valor, faça isso. 
        {
            case 1:
            printf("voce escolheu o registro de nomes\n");
            system("pause");
            break;

            case 2:
            printf("voce escolheu consultar os nomes\n");
            system("pause");
            break;

            case 3:
            printf("voce escolheu deletar um cadastro\n");
            system("pause");
            break;

            default:
            printf("essa opção não está disponível\n");
            system("pause");
            break;


        }

       
    }

}