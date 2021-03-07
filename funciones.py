from lxml import etree
def menu():
    print("---------EJERCICIO_JSON_NBA---------\n")
    print("  1. Muestra todos los equipos de 2a división.")
    print("  2. Introduzca el nombre de un canal de TV y cuenta los partidos que ha retransmitido.")
    print("  3. Preguntar por cualquier equipo y te informe en que puesto va en la tabla.")
    print("  4. Introduzca un nombre del equipo y muestra si ha ganado el local o el visitante.")
    print("  5. Mostrar la clasificacion de manera detallada, mostrando el puesto del equipo, los puntos que ha hecho, los partidos ganados y los partidos perdidos.")
    print("  6. Salir")
    print("\n------------------------------------")
def muestra_equipo(LaLiga123):
    equipos = LaLiga123.xpath("//clasificacion/team/name/text()")
    return equipos
def cuenta(tv, LaLiga123):
    aceituna = LaLiga123.xpath('count(//tv[. ="%s"]/text())'%tv)
    return aceituna
def busca_equipo(equipo, LaLiga123):
    busca = LaLiga123.xpath('//clasificacion/team/name[. ="%s"]/../rank/text()'%equipo)
    return busca
def loc_visita(equipo, LaLiga123):
    ganador = LaLiga123.xpath('//equipolocal[. ="s"]/../ganador/@id or //equipovisitante[. ="s"]/../ganador/@id'%equipo)
    return ganador
def posicion(LaLiga123):
    posicion = LaLiga123.xpath('//clasificacion//rank/text()')
    return posicion
def nombre(LaLiga123):
    nombre = LaLiga123.xpath('//clasificacion//name/text()')
    return nombre
def puntos(LaLiga123):
    puntos = LaLiga123.xpath('//clasificacion//points/text()')
    return puntos
def pwin(LaLiga123):
    pwin = LaLiga123.xpath('//clasificacion//won/text()')
    return pwin
def plost(LaLiga123):
    plost = LaLiga123.xpath('//clasificacion//lost/text()')
    return plost
