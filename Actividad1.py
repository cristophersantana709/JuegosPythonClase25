from random import randint
def adivina_el_numero():
    Numero_secreto= randint(0,100)
    intentos=0
    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    while True:
        intento=int(input("Ingresar tu numero: "))
        intentos = intentos + 1
        distancia=abs(Numero_secreto-intento)
        if intento < Numero_secreto:
            if distancia<=10:
                print("Demasiado bajo y esta cerca, intenta de nuevo.")
            else:
                print("demasido bajo y esta lejos, intenta de nuevo")
        elif intento > Numero_secreto:
            if distancia<=10:
                print("Demasiado alto y esta cerca, intenta de nuevo.")
            else:
                 print("Demasiado alto y esta lejos, intenta de nuevo.")
            print("Demasiado alto,intenta de nuevo.")
        else:
            print(f"Felicidades,adivinaste el numero en {intentos} intentos")
            break
adivina_el_numero()