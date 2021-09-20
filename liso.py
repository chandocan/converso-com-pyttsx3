
import pyttsx3
from os import system, name
import glob

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
som_pt = pyttsx3.init()
voices = som_pt.getProperty('voices')

for voice in voices:
   som_pt.setProperty('voice', voices[53].id) # 1 espanhol 4 chegou perto do portugês
   
print(voice)
#print(" - Languages: %s" % voice.languages)
som_pt.say('Bem vindo alfredo a programação com python')
# esperando o texto termina para poder roda o restante do codigo
som_pt.runAndWait()
input('Pressione Enter para continuar')

# esta estraindo a lista de arquivos presentes no diretorio atual
# usou uma compressão de lista
lista_arquivo = [f for f in glob.glob("*.txt")]
while True:
    limpar_terminal()
    apresentaMenu()
    print(lista_arquivo)
    arquivo_selecao = input('qual arquivo você quer ouvir  da lista ?').lower()
    if arquivo_selecao == 'sair':
        limpar_terminal()
        exit()
    else:
        try:
            with open((arquivo_selecao), 'r') as arquivo:
                # variavel texto recebe o arquivo aqui
                texto = arquivo.read()
                print(texto)
                som_pt.say(texto)
                som_pt.runAndWait()
                limpar_terminal()
                apresentaMenu()
        except FileExistsError:
            print('Digite um arquivo na lista apresentada ou sair para finalizar o programa')
            input('Enter para continuar')
