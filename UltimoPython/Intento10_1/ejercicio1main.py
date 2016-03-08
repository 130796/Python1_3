__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'

from ejercicio1class import Seno
from archivar import Archivo


def main():



            Tono = input("Frecuencia del tono: ")
            Tiempo = input("Tiempo en segundos: ")
            Frecuenciadesampleo = 44100
            MaxBits = 16
            Nombre = raw_input("nombre del archivo: ")

            print("ELIJA TIPO DE ONDA")
            print("1. Seno")
            print("2. Cuadrada")
            print("3. Triangular")
            print("4. Diente de sierra")
            x=input("")
            if x==1:
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                datos = onda.generarSeno()

            if x==2:
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                datos = onda.generarCuadrada()

            if x==3:
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                datos = onda.generarTriangular()

            if x==4:
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
                datos = onda.generarDiente()






            archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
            archivo.archivar(datos)


            onda.graficar(datos)








if __name__ == "__main__":
    main()