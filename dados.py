'''
Arquivo dados.py

Arquivo usado para definição das classes usadas no programa principal.
'''

from random import randrange
import random

def leArquivo():
  '''
  Lê o arquivo de texto pré criado na pasta do programa principal. Variáveis do programa:

  arquivo = variável que recebe o arquivo de texto
  palavras = lista criada para receber as palavras do arquivo
  sorteia = variável utilizada para sortear a palavra chave contida na lista
  word = variável utilizada para receber a palavra sorteada do arquivo
  '''
  arquivo = open("palavras_forca.txt", "r")
  palavras = []

  for linha in arquivo: #loop responsável por adicionar todas as palavras do arquivo em uma lista
    palavras.append(linha.strip()) #adicionando as palavras em uma lista e tirando todos os espaços a mais

  arquivo.close() #fecha o arquivo
  sorteia = random.randrange(1, len(palavras)) #sorteia de 1 ao tamanho do arquivo
  word = palavras[sorteia] #escolhe uma palavra sorteada do arquivo
  return word

def daDica():
  '''
    Lê o arquivo de texto pré criado na pasta do programa principal para verificar a dica da palavra chave.
    Variáveis da função:

    arquivo = variável que recebe o arquivo de texto
    dic = lista criada para receber a dica do arquivo
    dica = variável utilizada para alocar a dica contida no arquivo
    '''
  arquivo = open("palavras_forca.txt", "r")
  dic = []

  for linha in arquivo: #loop responsável por adicionar a dica em uma lista
    dic.append(linha.strip())  #adicionando a dica em uma lista e tirando todos os espaços a mais

  arquivo.close() #fecha o arquivo
  dica = (dic[0]) #verifica qual palavra está contida no espaço 0 do arquivo texto e a aloca na variável dica
  print(f'====== A dica da palavra chave é: {dica} ======\n') #retorna a dica da palavra na inicialização do jogo
  return dica

def desenhoForca(x=0):
  '''
      Desenha a forca na inicialização do jogo
      Variáveis da função:

      x = variável que recebe a quantidade de erros na jogabilidade, para adicionar os caracteres de
      enforcamento do boneco.
      '''
  if x == 0:
    print("------------")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x == 1:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x == 2:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x == 3:
    print("------------")
    print("|          |")
    print("|          0")
    print("|         -|")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x == 4:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|               ")
    print("|               ")
    print("|               ")
    print("|")
  elif x == 5:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         /      ")
    print("|               ")
    print("|               ")
    print("|")
  elif x == 6:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         / \   ")
    print("|               ")
    print("|    Lamento! Perdeu! ")
    print("|")