__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'
import wave
import pyaudio
import struct
from ejercicio1class import Seno
def main():
    print ("PUNTO 5 (Modifica dBFS de un archivo .WAV)")

    print("ingrese ruta del archivo")
    ruta=raw_input("")
    print("Ingrese nivele pico de la senal en dBFS")
    pico=input("")


    wf = wave.open(ruta, 'rb')
    rate = wf.getframerate()
    tamano = wf.getnframes()
    print tamano
    CHUNK = 1024
    sampwidth = wf.getsampwidth()
    print sampwidth
    channels = wf.getnchannels()
    para=wf.getparams()
    data=wf.readframes(CHUNK)
    time=(tamano/rate)*50
    data=data*time
    b=para[1]
    bits=b*8

    max=(2**bits)*10**(pico/20)
    print(max)
    print para
    salida="Editado2.wav"
    wk = wave.open(salida, 'w')
    Set_Bits = bits/8
    wk.setparams((channels, Set_Bits, rate, max, 'NONE', 'not compressed'))
    wk.writeframes(data)
    wk.close()










    print("Indique onda deseada:")
    print("1. Seno")
    print("2. Cuadrada")
    print("3. Triangular")
    print("4. Cuadrada")














if __name__ == "__main__":
    main()