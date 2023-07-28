#include <stdio.h> // conumicacao com o usuário
#include <stdlib.h> // alocacao de espaço na memória
#include <locale.h> //alocacao de texto

int teste()
{
    printf("Funcionou a função Pedro");
    system("pause");// depois que sai de uma função, para não voltar automaticamente para main
}

int registro()
{
    printf("voce escolheu o registro de nomes\n");
    system("pause");
}

int consulta()
{
    printf("voce escolheu a consulta de nomes\n");
    system("pause");
}

int deletar()
{
    printf("voce escolheu deletar nomes\n");
    system("pause");
}

int main()
{
    
    int opcao=0;//definindo variáveis
// a variavel do tipo int está ocupada valendo 0, o delete só afirma que o espaço está vazio, não que necessariamente deletou
    int laco=1;

    for(laco=1;laco=1;)
    {

    
        setlocale(LC_ALL, "Portuguese");//linguagem definida


        printf("### Cartorio da EBAC###/n/n");//inicio do menu
        printf("Escolha a opcao de desejada no menu:\n\n");
        printf("\t1 - Registrar nomes\n");
        printf("\t2 - Consultar nomes\n");
        printf("\t3 - Deletar nomes\n\n");
        printf("Opção final:");// final do menu

        scanf("%d", &opcao);// armazenar na variavel opcao o valor digitado pelo usuario

        system("cls");
        switch(opcao)//para diminuir o codigo refazendo o if
        //caso a variavel tenha determinado valor, faça isso. 
        {
            case 1:
            registro();
            break;

            case 2:
            consulta();
            break;

            case 3:
            deletar();
            break;

            case 4:
            teste();
            break;


            default:
            printf("essa opção não está disponível\n");
            system("pause");
            break;


        }

       
    }

}