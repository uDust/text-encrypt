#   modulos  #
import base64
from colorama import Fore 
import sys
import time


#   variables   #

#strings para decorancion
banner = """        _
        ..._
      .'     '.      _
     /    .-""-\   _/ \\
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .=  *=|ASTRO _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\\
\__/'._;.  ==' ==\\
         \    \   |
         /    /   /
         /-._/-._/
          \   `\  \\
          `-._/._/

    Text Encrypter/Decrypter
    In 
    Base64
    
          """

helpstr = """
uso:
    -e: para encryptar un texto en base64
    -d: para desencryptar untexto en base64
"""

#opciones 
try:
    dore = str(sys.argv[1])
except IndexError:
    print(helpstr)
    sys.exit(1)
#colores
green = Fore.GREEN 
red = Fore.RED 
purple = Fore.MAGENTA
reset = Fore.RESET 
#   funciones   #

#funciones para encryptar en diferentes tipos de encryptaciones

#funcion para encryptar un texto en b64 
def b64(text: str):
    
    #variables para encryptar el texto en base64
    textbytes = text.encode('ascii')
    b64_bytes = base64.b64encode(textbytes)
    msg = b64_bytes.decode('ascii')
    
    #devolvemos el texto encryptado 
    return msg 

#funcion pero para desencryptar el texto
def b64_decrypt(text: str):
    b64bytes = text.encode('ascii')
    textbytes = base64.b64decode(b64bytes)
    msg = textbytes.decode('ascii')

    return msg 
    
#encryptar/desencryptar usando las anteriores funciones 
#funcion para encryptar varias capas
def crypt(txt: str, laps: int):
    #condiciones para las vueltas 
    if laps == 0:
        #si las vueltas son < 0 ...
        print("no puedes encryptar un texto 0 veces tonto")
        sys.exit(1)

    elif laps > 50:
        #si las vueltas son mayores a 50...
        confirm = input("si son mas de 50 vueltas el programa puede ocacionar un crasheo, seguro que quieres continuar y/n: ")
        confirm.lower()

        if confirm == "y" or confirm == "yes":
            #si la confirmacion es si...
            pass 

        elif confirm == 'n' or confirm == 'no':
            #si la confirmacion es no...
            print('saliendo del programa, adios!')
            sys.exit(0)

    #bucle que encrypta varias veces el textto en b64 
    for x in range(laps):
        encodedtxt = b64(txt)
        txt = encodedtxt
    
    
    return txt 
#funcion para desencryptar un texto en b64 
def decrypt(txt: str, laps: int):

    #bucle para desencryptar un texto segun las laps
    for _ in range(laps):
        decodedtxt = b64_decrypt(txt)
        txt = decodedtxt

    #devuelve el texto 
    return txt
     


if __name__ == "__main__":
    
    op = ''
    if dore == '-e' or dore == '-E':
        op += 'crypt'

    elif dore == '-d' or dore == '-D':
        op += 'decrypt'

    else:
        print(helpstr)
        sys.exit()

    print(purple, banner, reset)
    try:
        laps = int(input("introduce cuantas veces quiere que se encrypte el texto (enter para 1na vuelta): "))
    except ValueError:
        laps = 1

    text = input("introduce el texto que quieres encryptar: ")

    if op == 'crypt':

        print(crypt(text, laps))

    else:
        print(decrypt(text, laps))
