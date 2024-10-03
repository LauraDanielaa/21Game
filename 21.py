import random

#Funcion para barajar las cartas
def crearBaraja():
    return [(v,p) for v in ['Az',2,3,4,5,6,7,8,9,'J','K','Q'] for p in ['D','C','T','P']]

def barajar():
    return random.sample(crearBaraja(),len(crearBaraja()))

#funcion para asignar el valor de las cartas J, Q, K

def Valor(valor):
    if type(valor)==int:
        return valor
    elif(valor=="J" or valor=="Q" or valor=="K"):
        return 10
    elif(valor=='Az'):
        return 1
    else:
        return 0

#funcion para verificar si la lista tiene un as

def tiene_A(mano):
    if mano [0] [0] == "Az":
        return True
    if mano != []:
        return tiene_A(mano[1 , ])
    if mano == []:
        return False

#Funcion para sumar los valores de las listas
def sumMano(mano):
    if mano==[]:
        return 0
    return Valor(mano[0][0])+sumMano(mano[1:])

#funcion para determinar si el as se toma como un 1 o un 11

def valor_A(mano):
    if tiene_A(mano) and sumMano(mano)<=11:
        return sumMano(mano)+10

#funcion para no tener manos iguales o cartas iguales

def comparar(mano, carta):
    if carta not in mano:
        return True
    else:
        return False

#pide otra carta adicional
def pedirCartaJug(mano, baraja):
    print(sumMano(mano))
    if sumMano(mano)==21: #este if pasarlo a comparar mano junto con el if de pedir cartas dealer y dejar una unica funcion pedirCarta
        return mano
    if(input("s: Pedir Carta\nn: Plantar\n")=='s'):
      pedirCartaGeneral(baraja,mano)
      return pedirCartaJug(mano, baraja)
    return mano,baraja

def pedirCartaDealer(mano,baraja):
    if sumMano(mano)<17:
        return mano.append(random.sample(baraja,1))
#funcion para comparar las cartas entre el dealer y el jugador, puede ser la funcion control


def ganador(bool,mano1,mano2):
    if (bool and sumMano(mano2)==21) or (bool and sumMano(mano2)>sumMano(mano1) and sumMano(mano2)<=21) or (bool and sumMano(mano1)>21) or (bool and (sumMano(mano1)==sumMano(mano2))):
        return False
    if (bool and sumMano(mano1)==21) or (bool and sumMano(mano1)>sumMano(mano2) and sumMano(mano1)<=21) or (bool and sumMano(mano2)>21):
        return True

def pedirCartaGeneral(baraja, mano):
    if not baraja:  # Baraja vacía
        return mano, baraja
    mano.append(baraja.pop(0))
    return mano, baraja

def jugar21(baraja, manoJugador, manoDealer):
    pedirCartaJug(manoJugador, baraja)


def jugar(baraja,jugador,dealer):
    pedirCartaGeneral(baraja,jugador)
    pedirCartaGeneral(baraja,dealer)
    pedirCartaGeneral(baraja,jugador)
    pedirCartaGeneral(baraja,dealer)
    print(jugador)
    print(dealer)
    jugar21(baraja, jugador, dealer)
    print(jugador)


jugar(barajar(),[],[])