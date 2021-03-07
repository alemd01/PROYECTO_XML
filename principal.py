from lxml import etree
from funciones import menu, muestra_equipo, cuenta, busca_equipo, loc_visita, posicion, nombre, puntos, pwin, plost
import time
LaLiga123 = etree.parse('LaLiga123.xml')
while True:
    menu()
    opc = int(input("Introduzca una opcion: "))
    if opc == 1:
        equipo=muestra_equipo(LaLiga123)
        print("Estos son los equipos de 2a division: ")
        for a in range (0,len(equipo)):
            print(equipo[a])
            time.sleep(0.2)
    elif opc == 2:
        print("Esta jornada ha sido retransmitida por: TDP, MARCA TV, Esports 3, Telecable, C+1, TVG2, TVC ")
        nombretv = input("Introduzca un nombre de TV:")
        cuentatv=cuenta(nombretv,LaLiga123)
        print("El canal %s ha emitido %i partidos esta jornada" % (nombretv, cuentatv))
    elif opc == 3:
        equip3 = input("Introduzca el nombre de un equipo de 2a division: ")
        for nombre in busca_equipo(equip3, LaLiga123):
            print("El equipo %s se encuentra en la posicion: %s"% (equip3, nombre))
    elif opc == 4:
        #No terminado, no consigo realizarlo.
        equip4 = input("Introduzca el nombre de un equipo de 2a division: ")
        for nombre1 in loc_visita(equip4, LaLiga123):
            print("El partido que ha jugado equipo %s ha ganado el %s " % (equip4, nombre1))
    elif opc == 5:
        print("POS  EQUIPOS  PTOS  PG  PP")
        for nombre2 in zip(posicion(LaLiga123), nombre(LaLiga123), puntos(LaLiga123), pwin(LaLiga123), plost(LaLiga123)):
            print(nombre2[0], nombre2[1], nombre2[2], nombre2[3], nombre2[4])
    elif opc == 6:
        print("Has elegido la opcion Salir.")
        break
    elif opc >6:
        print("-----------------------------------------")
        print("ERROR HAS INTRODUCIDO UN NUMERO NO VALIDO")
        print("-----------------------------------------")
