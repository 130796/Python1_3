__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'

from ejercicio2class import analizarLeq
from ejercicio2class import analizarRMS

from archivar import Archivo
import struct
import wave
import pyaudio
import math

def main():
    print ("PUNTO 4")
    print("")

    print("ingrese ruta del archivo")
    ruta=raw_input("")

    wf = wave.open(ruta, 'rb')
    rate = wf.getframerate()
    tamano= wf.getnframes()
    para=wf.getparams()
    print para
    b=para[1]
    print b
    bits=b*8
    print("Numero de bits:")
    print bits
    print("")
    dB=20*math.log10(float(tamano)/(2**bits))

    time=tamano/rate
    T=1.0/rate


    print("Valor maximo de frames")
    print tamano

    print("")

    print("Valor maximo en dBFS")
    print dB

    print("")



    rms=analizarRMS( tamano,  ruta, bits)
    datos1=rms.RMS()


    leq = analizarLeq( tamano, time, T, ruta, bits)
    datos1=leq.Leq()












if __name__ == "__main__":
    main()