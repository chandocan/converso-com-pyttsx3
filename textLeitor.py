
import pyttsx3
from os import system, name
import glob

from pyttsx3 import engine

def limpar_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def apresentaMenu():
    print('escolha o arquivo digite o nome completo digite sair paran\
    encerra digite o nome completo do arquivo para pode ler')

limpar_terminal()
apresentaMenu()

# procura uma forma de deixa o texto em portuguễs por padrão
engine = pyttsx3.init()
engine.setProperty('rate', 85) #90
engine.setProperty('voice', 'brazil-mbrola-1')
#voices = engine.getProperty('voices')

# vai pecorre uma liasta das vozes quando chega em  b'\x05pt-br' que é a brasileira vai para
#for voice in voices:
#    if voice.languages[0] == b'\x05pt-br':
#        engine.setProperty('voice', voice.id)
#        break


#print(" - Languages: %s" % voice.languages)
#print(voice)
engine.say('Bem vindo alfredo a programação com python')
# esperando o texto termina para poder roda o restante do codigo
engine.runAndWait()
input('Pressione Enter para continuar')

# esta estraindo a lista de arquivos presentes no diretorio atual
# usou uma compressão de lista
lista_arquivo = [f for f in glob.glob("*.txt")]
while True:
    limpar_terminal()
    apresentaMenu()
    print(lista_arquivo)
    # vai perdi a entrada de dados do teclado
    arquivo_selecao = input('qual arquivo você quer ouvir  da lista use a exetenção do arquivo ou sair p/quit ?').lower()
    if arquivo_selecao == 'sair':
        limpar_terminal()
        exit()
    else:
        try:
            with open((arquivo_selecao), 'r') as arquivo:
                # variavel texto recebe o arquivo aqui
                texto = arquivo.read()
                print(texto)

                # mudando a velocidade da fala
                #rate = engine.getProperty('rate')
                #engine.setProperty('rate', rate-55) # 55

                engine.say(texto)
                engine.runAndWait()
                limpar_terminal()
                apresentaMenu()
        except FileExistsError:
            print('Digite um arquivo na lista apresentada use as extenções dos arquivos ou [sair] para finalizar o programa')
            input('Enter para continuar')





