__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'
__author__="Perros"

from ejercicio4class import Seno
from archivar import Archivo
import math


def main():


            print ("PUNTO 5 BUENO")
            Tono = input("Frecuencia del tono: ")
            Tiempo = input("Tiempo en segundos: ")
            Frecuenciadesampleo = 44100
            MaxBits = 16
            Nombre = raw_input("nombre del archivo: ")
            pico=10000000
            while pico>=29273.8558952:
                print("Ingrese nivele pico de la senal en dBFS menores iguales a -7dBSF: ")
                pico=input("")
            pico=input("")
            max2=2**16
            print max2
            max1=10**(float(pico)/20)
            print max1
            max=max1*max2


            print max





            print("ELIJA TIPO DE ONDA")
            print("1. Seno")
            print("2. Cuadrada")
            print("3. Triangular")
            print("4. Diente de sierra")
            x=input("")

            if x==1:
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo, max)
                datos = onda.generarSeno()

            if x==2:
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo, max)
                datos = onda.generarCuadrada()

            if x==3:
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo, max)
                datos = onda.generarTriangular()

            if x==4:
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo, max)
                datos = onda.generarDiente()


            archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
            archivo.archivar(datos)


            onda.graficar(datos)








if __name__ == "__main__":
    main()