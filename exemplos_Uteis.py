'''
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

'''
'''
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print (voice)
    if voice.languages[0] == u'en_US':
        engine.setProperty('voice', voice.id)
        break

engine.say('Hello World')
engine.runAndWait()
'''

'''
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print (voice)
    if voice.languages[0] == b'\x05pt-br':
        engine.setProperty('voice', voice.id)
        break

engine.say('Ola amigos estamos aqui estamos apanhando muito para apreender')
engine.runAndWait()
'''


'''
import pyttsx3
engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''


''''
# para achar o indice da voz a do barasil é 53
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1
engine.runAndWait()
'''



'''
#vai criar um arquivo de mp3 com arquivo de texto
import pyttsx3
engine = pyttsx3.init()
engine.save_to_file('Hello World' , 'test.mp3')
engine.runAndWait()
'''
'''
import pyttsx3
# mudando velocidade da fala
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''

