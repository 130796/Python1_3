___author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz_Corregido'
import math
import matplotlib.pylab as plt
import wave
import pyaudio

class Seno:
        wavearray = []
        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = sampling * time


        def generarCuadrada(self):

            for i in range(0,self.tamano):
                    A=((4.0/float(math.pi))*(2**self.NumeroBit))/100.0
                    datos=0
                    k=1
                    for j in range(0,50):


                        value=(1/float(k))*math.sin((k*math.pi*self.Frecuencia*i)/self.SamplingRate)

                        datos=datos+value
                        k=k+2



                    frame=datos*A

                    Seno.wavearray.append(frame)


            print max(Seno.wavearray)

            return Seno.wavearray


        def generarTriangular(self):

            for i in range(0,self.tamano):
                    A=((8.0/float(math.pi**2))*(2**self.NumeroBit))/100.0
                    datos=0
                    k=1
                    for j in range(0,50):

                        value=(((-1)**((float(k-1))/2.0))/float(k**2))*math.sin((k*math.pi*self.Frecuencia*i)/self.SamplingRate)

                        datos=datos+value
                        k=k+2



                    frame=datos*A
                    Seno.wavearray.append(frame)

            print max(Seno.wavearray)
            return Seno.wavearray

        def generarDiente(self):

            for i in range(0,self.tamano):
                    A=(((0.5)-(1/float(math.pi)))*(2**self.NumeroBit))/100.0
                    datos=0

                    for j in range(0,100):
                        par=j%2
                        if par:
                            value=(1/float(j))*math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)

                            datos=datos+value



                    frame=datos*A
                    Seno.wavearray.append(frame)

            print max(Seno.wavearray)
            return Seno.wavearray


        def generarSeno(self):

            for i in range(0, self.tamano):

                    datos = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)
                    Seno.wavearray.append(datos)



            return Seno.wavearray






        def graficar(self, array):
                plt.plot(array, color="green", linewidth=1.0, linestyle="-")
                plt.show()



