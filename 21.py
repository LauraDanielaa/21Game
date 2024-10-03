import random

# Funcion para barajar las cartas


def crearBaraja():
    return [(v, p) for v in ['Az', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'K', 'Q'] for p in ['D', 'C', 'T', 'P']]


def barajar():
    return random.sample(crearBaraja(), len(crearBaraja()))

# funcion para asignar el valor de las cartas J, Q, K


def Valor(valor):
    if type(valor) == int:
        return valor
    elif (valor == "J" or valor == "Q" or valor == "K"):
        return 10
    elif (valor == 'Az'):
        return 1
    else:
        return 0

# funcion para verificar si la lista tiene un as


def tiene_A(mano):
    if mano and len(mano[0]) > 0 and mano[0][0] == "Az":
        return True
    if mano:  # Si mano no está vacía
        # Llama recursivamente con el resto de la lista
        return tiene_A(mano[1:])
    return False

# Funcion para sumar los valores de las listas


def sumMano(mano):
    if mano == []:
        return 0
    return Valor(mano[0][0])+sumMano(mano[1:])

# funcion para determinar si el as se toma como un 1 o un 11


def valor_A(mano):
    if tiene_A(mano) and sumMano(mano) <= 11:
        return sumMano(mano)+10
    else:
        return sumMano(mano)

# pide otra carta adicional


def pedirCartaJug(mano, baraja):
    if valor_A(mano) == 21:  # este if pasarlo a comparar mano junto con el if de pedir cartas dealer y dejar una unica funcion pedirCarta
        return 21
    while (True):
        if (input("s: Pedir Carta\nn: Quedarse\n") == 's'):
            print("Nueva mano: \n")
            pedirCartaGeneral(baraja, mano)
            print(mano)
            print("Nuevo valor de la mano", valor_A(mano))
            if valor_A(mano) > 21:
                break
        else:
            break
    return valor_A(mano)


def pedirCartaDealer(mano, baraja):
    if valor_A(mano) == 21:
        return 21
    while (valor_A(mano) < 17):
        pedirCartaGeneral(baraja, mano)
        print(mano)
        print("Nuevo valor de las cartas del dealer: ", valor_A(mano))
    return valor_A(mano)
# funcion para comparar las cartas entre el dealer y el jugador, puede ser la funcion control


def pedirCartaGeneral(baraja, mano):
    if not baraja:  # Baraja vacía
        return mano, baraja
    mano.append(baraja.pop(0))
    return mano, baraja


def ganador(manoJugador, manoDealer):
    print("---------------\nValor de mano final jugador: ",
          manoJugador, "\nValor de mano final dealer: ", manoDealer)
    if manoDealer == 21:
        print("Gana el dealer")
    elif manoJugador == 21 and manoDealer != 21:
        print("Gana el jugador")
    elif manoJugador == manoDealer:
        print("Gana Dealer por empate")
    elif manoDealer > 21 and manoJugador < 21:
        print("Gana el jugador")
    elif manoJugador > 21 and manoDealer < 21:
        print("Gana el dealer")
    elif manoJugador < 21 and manoJugador > manoDealer:
        print("Gana jugador")
    elif manoDealer < 21 and manoDealer > manoJugador:
        print("Gana Dealer")
    elif manoDealer > 21 and manoJugador > 21:
        print("Gana el dealer")


def jugar21(baraja, manoJugador, manoDealer):
    ganador(pedirCartaJug(manoJugador, baraja),
            pedirCartaDealer(manoDealer, baraja))


def jugar(baraja, jugador, dealer):
    pedirCartaGeneral(baraja, jugador)
    pedirCartaGeneral(baraja, dealer)
    pedirCartaGeneral(baraja, jugador)
    pedirCartaGeneral(baraja, dealer)
    print("Mano del jugador: ", jugador,
          "\nValor de la mano del juagdor: ", valor_A(jugador))
    print("---------------------\nMano del dealer: ", dealer,
          "\nValor de la mano del dealer ", valor_A(dealer))
    jugar21(baraja, jugador, dealer)


# Menu para jugar o salir
def menu():
    while True:
        print("\nBienvenido! A continuación podrás jugar 21 con la maquina que será el dealer\nEl que llegue a 21 o se aproxime mas será el ganador\n\nQue empiece el juego :)\n")
        jugar(barajar(), [], [])

        # Preguntar al usuario si desea jugar otra vez
        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra_vez == 'n':
            print("Gracias por jugar. ¡Hasta luego!")
            break


# Ejecutar el menú
menu()
