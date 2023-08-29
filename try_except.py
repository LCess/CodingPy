#Funcion de prueba sobre el try - except
#aqui alirio me ayudó a entender

print("Vamos a probar la función con tru/except")

def main():
    try:
        divisor= float(input("Introduce el número a dividir entre 10:"))
        result= 10/divisor
        print(f"El resultado es: {result} ")
    except ZeroDivisionError:
        print("El cero no es un número válido en esta operación")
    except ValueError:
        print("Las letras no son validas para esta operación")

main()

