#include <stdio.h> // conumicacao com o usuário
#include <stdlib.h> // alocacao de espaço na memória
#include <locale.h> //alocacao de texto
#include <string.h>// biblioteca das strings

int teste()
{
    printf("Funcionou a função Pedro");
    system("pause");// depois que sai de uma função, para não voltar automaticamente para main
}

int registro()
{
    char arquivo[40];
    char cpf[40];
    char nome[40];
    char sobrenome[40];
    char cargo[40];

    printf("Digite o CPF a ser cadastrado: ");
    scanf("%s", cpf);//enquando digitar 40 numeros, vai colocar no cpf
    // para não perguntar do usuário duas vezes, armazena o CPF na variável arquivo
    strcpy(arquivo, cpf);
    FILE *file;//procupa na biblioteca uma estrutura file pois vai ser criado um arquivo (parece comando SQL)
    file = fopen(arquivo, "w");//abre um arquivo com o que tiver dentro da variável
    fprintf(file,cpf);//salva o valor
    fclose(file);// fechar o arquivo
    file = fopen(arquivo, "a");//para atualizar o arquivo
    fprintf(file,",");
    fclose(file);

    printf("Digite o nome a ser cadastrado: ");
    scanf("%s", nome);
    file = fopen(arquivo, "a");
    fprintf(file, nome);
    fclose(file);
    
    printf("Qual o sobrenome a ser cadastrado: ");
    scanf("%s", sobrenome);
    file =  fopen(arquivo, "a");
    fprintf(file, sobrenome);
    fclose(file);

    file = fopen(arquivo, "a");
    fprintf(file, ",");
    fclose(file);

    printf("Digite o cargo a ser cadastrado: ");
    scanf("%s", cargo);
    file = fopen(arquivo, "a");
    fprintf(file, cargo);
    fclose(file);

    system("pause");



}

int consulta()
{
    setlocale(LC_ALL, "Portuguese");
    char cpf[40];
    char conteudo[200];

    printf("Digite o cpf a ser consultado:"); //recebendo qual usuário vai ser consultado
    scanf("%s",cpf);

    FILE *file;
    file = fopen(cpf, "r");

    if(file == NULL)
    {
        printf("não foi possivel localizar arquivo \n");

    }
    while(fgets(conteudo, 200, file) != NULL)
    {
        printf("\nEssas são as informações do usuário: ");
        printf("%s", conteudo);
        printf("\n\n");
    }

    system("pause");

}

int deletar()
{
    char cpf[40];
    printf("Digite o CPF a ser deletado: ");
    scanf("%s", cpf);//lembrando: vai varrer o que foi digitado na variável p armazenar. como é string, usa o %s
    remove(cpf);

    FILE *file;
    file = fopen(cpf, "r");

    if(file == NULL)
    {
        printf("O usuário não se encontra no sistema.\n");
        system("pause");
    }


}

int main()
{
    
    int opcao=0;//definindo variáveis
// a variavel do tipo int está ocupada valendo 0, o delete só afirma que o espaço está vazio, não que necessariamente deletou
    int laco=1;
    char senhadigitada[]="a";
    int comparacao;


    printf("### Cartorio da EBAC ###\n\n");
    printf("Login de adminsitrador \n\nDigite a sua senha");
    scanf("%s", senhadigitada);

    comparacao = strcmp(senhadigitada, "admin");


    if(comparacao == 0)
    {
        system("cls");
        for(laco=1;laco=1;)
        {

    
            setlocale(LC_ALL, "Portuguese");//linguagem definida


            printf("### Cartorio da EBAC###/n/n");//inicio do menu
            printf("Escolha a opcao de desejada no menu:\n\n");
            printf("\t1 - Registrar nomes\n");
            printf("\t2 - Consultar nomes\n");
            printf("\t3 - Deletar nomes\n\n");
            printf("\t4 - Sair do sistema\n\n");
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
                printf("Obrigado por utilizar o sistema!\n");
                return 0;
                break;


                default:
                printf("essa opção não está disponível\n");
                system("pause");
                break;

             }

        }
    }
    else
        printf("senha incorreta");

}