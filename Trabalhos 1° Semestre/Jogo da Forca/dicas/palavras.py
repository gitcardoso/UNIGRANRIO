import random


# função para escolher palavra secreta
def sorteiap():

    nrodica = random.randrange(1,15)  # gera nro aleatório de 1 a 15
    arquivo = open('dicas/pd.txt','r')
    dados = list()
    
    # procura nro randômico gerado no arquivo da variável 'arquivo'
    for linha in arquivo:
        vlista = linha.split('|')
        dados.append(vlista)
            
        for x in range(0,len(dados)):    
            vnrdica = int(dados[x][0])
            if vnrdica == nrodica:
                vpalavra = dados[x][1]
                vdica = dados[x][2]
    # fecha arquivo
    arquivo.close()
    
    # joga palavra e dica encontrada no txt para a variavel vretorno
    vretorno = vpalavra+'|'+vdica
    
    return  vretorno