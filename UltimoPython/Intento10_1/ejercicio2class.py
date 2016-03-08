__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'
import math
import struct
import wave

class analizarLeq:
    def __init__(self, tamano, time, periodo, ruta, bits):

            self.tamano = tamano
            self.Seconds = time
            self.periodo=periodo
            self.ruta=ruta
            self.bits=bits

    def Leq(self):
        wf=wave.open(self.ruta, 'rb')
        sumatoria=0
        for j in range(0,self.tamano):
            q=wf.readframes(1)
            p=struct.unpack("<h",q)

            sumatoria=sumatoria+((int(p[0])**2)*self.periodo)


        leq=20*math.log10((1.0/self.Seconds)*(sumatoria)/(2**self.bits))
        print("Valor Leq:")
        print leq
        print("")

class analizarRMS:
    def __init__(self, tamano,  ruta, bits):

            self.tamano = tamano
            self.ruta=ruta
            self.bits=bits

    def RMS(self):
        wf=wave.open(self.ruta, 'rb')
        sumatoria=0
        for i in range(0,self.tamano):
            a=wf.readframes(1)

            b=struct.unpack("<h",a)
            sumatoria=sumatoria+int(b[0])**2
            valorrms=math.sqrt(sumatoria/self.tamano)

        vlpico=20*math.log10(valorrms/(2**self.bits))
        print("Valor RMS: ")
        print vlpico
        print("")







