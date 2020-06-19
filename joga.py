'''
Arquivo joga.py

Arquivo que contém o programa principal.

'''

import dados
from dados import *

#criação de variáveis
erros = 0
temp = []
disputadas = 1
perdeu = 0
ganhou = 0

daDica() #chama a função que gera a dica da palavra chave

#coleta o nome do jogador
nome = str(input('Para começar, informe o seu nome: '))
nome = nome.upper() #transforma o nome em maiusculo
print(f'É bom ter você aqui, {nome}. Vamos jogar!')

#função principal do jogo
def joga_forca(erros):

    #criação de variáveis globais dentro da função principal
    global disputadas
    global perdeu
    global ganhou

    #le o arquivo de texto e sorteia a palavra do jogo
    word = leArquivo()

    #inicializa novamente a variável erros, zerando-a a cada rodada jogada
    erros = 0

    #limpa quaisquer informações contidas na variável temp a cada rodada jogada
    temp.clear()
    for letra in word: #loop para criação dos underlines do jogo, respeitando a quantidade de letras da palavra sorteada
        temp.append('_')

    #loop principal do jogo
    while True:
        print('\n' * 10)
        desenhoForca(erros)  #imprime desenho da forca

        print('\nAdivinhe: ', end='') #imprime a adivinhacao

        #loop que permite a separação dos underlines criados na variável temp, para uma melhor visualização do jogo
        for let in temp:
            print(let, end=' ')
        print('\n' * 1)

        #verifica se perdeu
        if erros == 6:
            perdeu += 1 #incrementa + 1 a cada rodada jogada dentro da variável perdeu
            print(f'=== A palavra correta era: {word} ===\n') #gera na tela a palavra correta
            break  #sai do jogo (sai do while principal)

        #verifica se o jogador ganhou
        ganhouJogo = True
        #loop que verifica se a variável let contém algum underline. Se sim, jogador ainda não ganhou.
        for let in temp:
            if let == '_':
                ganhouJogo = False
        #if que identifica se variável ganhouJogo retornou True.
        if ganhouJogo:
            ganhou += 1 #incrementa + 1 a cada rodada jogada dentro da variável ganhou
            print('=== Parabéns! Você acertou a palavra chave. ===\n') #gera na tela uma frase informando que o jogador
            # ganhou o jogo
            break #sai do jogo (sai do while principal)

        # captura a letra do usuario
        letraDig = str(input("Informe uma letra: "))
        letraDig = letraDig.lower() #caso seja digitada letra maiúscula, a mesma é transformada em minúscula

        # verifica se acertou alguma letra
        errouLetra = True
        #loop que verifica se a letra digitada está contida na palavra sorteada
        for i, let in enumerate(word):
            if word[i] == letraDig:
                temp[i] = word[i]
                errouLetra = False
        #if que verifica se errou a letra digitada
        if errouLetra:
            print(f'\nDesculpe, a letra {letraDig} não se encontra na palavra sorteada.') #se errou, gera uma mensagem
            # informando que a letra digitada não está contida na palavra sorteada
            erros = erros + 1 #se errou, erros incrementa + 1 para contagem de erros

    #loop que verifica se o jogador deseja jogar novamente
    while True:
        resposta = str(input('Deseja jogar novamente? (S | N) '))
        resposta = resposta.upper()
        #loop que verifica se o usuário digitou algo diferente de S ou N
        if resposta in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')

    #if que verifica se jogador digitou S
    if resposta == 'S':
        disputadas += 1 #incrementa + 1 a cada rodada jogada dentro da variável disputadas
        joga_forca(erros) #chama o loop principal do jogo
    #if que verifica se jogador digitou N
    if resposta == 'N':
        #gera as informações como nome, quantidade de partidas disputadas, ganhas e perdidas
        print('\n'*5)
        print(f'============= Foi bom jogar com você! =============')
        print(f'\n============= TABELA DE PONTUAÇÃO DE {nome} =============')
        print(f'Você disputou: {disputadas} rodada(s)')
        print(f'Você venceu: {ganhou} rodada(s)')
        print(f'Você perdeu: {perdeu} rodada(s)')