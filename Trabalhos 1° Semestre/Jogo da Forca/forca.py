from visual.forca import forca
from visual.cabeçalho import título
from dicas.palavras import sorteiap


título('\033[34mJOGO DA FORCA\033[m')
jogador = input(str('\033[33mDigite seu Nome: \033[m'))  # Guarda em uma variavél o nome do Jogador


continuar = 'S'
partidas=vitorias=derrotas = 0  # armazena nro de partidas, vitorios e derrotas e inseri 0 como default


while continuar in 'Ss':

    # Incrementa o nro de partidas em +1
    erros=0
    partidas +=1

    # SORTEIA PALAVRA E DICA INICIAL
    lletras = list()
    dadospalavra = list()  # lista de palavra sorteada
    listasorteio = sorteiap()  # gera a palavra e dica aleatória
    vlistap = listasorteio.split('|')  # explode string recebida
    dadospalavra.append(vlistap)  # joga string em uma lista para resgatar os dados

    for x in range(0,len(dadospalavra)):
        word = dadospalavra[x][0]  # resgata palavra
        dicauser = dadospalavra[x][1]  # resgata dica

    temp=[]

    for letra in word:
        temp.append('_')

    while True:


        print('\n'*20)
        forca(erros, jogador)   # imprime desenho da forca

        # Imprime a Dica
        print(f'Dica: \033[4m{dicauser}\033[m')

        # imprime a palavra secreta
        print('\n\n\033[33mPalavra Secreta:\033[m ', end='')

        for let in temp:
            print(let, end=' ')
        print('\n'*2)

        # Verifica se perdeu
        if erros==6:
            derrotas +=1  # Incrementa o nro de derrotas em +1
            print(f'\n LAMENTO \033[4m{jogador}\033[m, VOCÊ PERDEU!!!')
            print('')
            print(f'\033[51mTotal Partidas:\033[m {partidas}')
            print(f'\033[36mTotal Vitórias:\033[m {vitorias}')
            print(f'\033[31mTotal Derrotas:\033[m {derrotas}')
            print('\n'*2)
            continuar = str(input('Jogar Novamente? [S/N] : ')).upper().strip()[0]
            break  # sai do jogo (sai do while)

        # Verifica ganhou
        ganhouJogo=True
        for let in temp:
            if let=='_':
                ganhouJogo=False

        if ganhouJogo:
            vitorias +=1    # Acrescenta mais 1 ao número de vitórias
            print(f'\n PARABÉNS {jogador}, VOCE ACERTOU!!!')
            print('')
            print(f'\033[51mTotal de  Partidas:\033[m {partidas}')
            print(f'\033[36mNúmero de Vitórias:\033[m {vitorias}')
            print(f'\033[31mNúmero de Derrotas:\033[m {derrotas}')
            print('\n'*2)
            continuar = str(input('Jogar Novamente? [S/N] : ')).upper().strip()[0]

            break

        # captura a letra do usuario
        print(f'\033[31mLETRAS JÁ DIGITADAS:\033[m')
        print(lletras)
        letraDig=input("Digite uma letra: ")
        letraDig = letraDig.upper()     #Deixa a letra maiúscula
        lletras.append(letraDig)

        # verifica se acertou alguma letra
        errouLetra=True
        for i, let in enumerate(word):
            if word[i]==letraDig:
                temp[i]=word[i]
                errouLetra=False
        if errouLetra:
            erros=erros+1


