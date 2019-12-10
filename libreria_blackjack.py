# ====LIBRERIAS
import random
import os

# ====PROCEDIMIENTOS
def partidaMultiApuesta():
    print ("Bienvenido al modo 'Multi con apuestas'")
    numeroJugadores()
    definirOrden()
    tiradaJugadores()
    definirApuestas()
    apuestas()
    tiradaIA()
    comprobarGanador()

def partidaMultiSinApuesta():
    print ("Bienvenido al modo 'Multi sin apuestas'")
    numeroJugadores()
    definirOrden()
    tiradaJugadores()
    tiradaIA()
    comprobarGanador()

def partidaSolo():
    print ("Bienvenido al modo 'Solo vs casa'")
    tiradaUnJugador()
    tiradaIA()
    comprobarGanadorSimple()
    
def numeroJugadores():
    global numero_jugadores
    numero_jugadores= int(input("Número de jugadores: "))
    while numero_jugadores<2 or numero_jugadores>7:
        print ("La cantidad de jugadores en el modo multijugador debe ser entre 2 y 7")
        numero_jugadores = int(input("Número de jugadores (entre 2 y 7): "))

def guardarPuntuacion(jugador,puntuacion):
    jugadores[jugador][1]=puntuacion

def limpiarPantalla():
    a=input("Pulsa <Enter> para limpiar pantalla y pasar al siguiente jugador ")
    os.system('cls')

def comprobarGanador():
    puntero=[0]
    puntuacion=0
    for a in range(len(jugadores)):
        variable=jugadores[a][1]
        if variable>puntuacion:
            puntuacion=jugadores[a][1]
            puntero=[a]
        elif variable==puntuacion:
            puntero.append(a)
    ganadores=""
    for b in puntero:
        ganadores+=" "+str(jugadores[b][0])
            
    if puntuacion==contadorIA and len(puntero)!=1:
        print("Los jugadores -{} - han empatado con la banca con {} puntos.".format(ganadores, puntuacion))
    elif puntuacion==contadorIA and len(puntero)==1:
        print("El jugador -{}- ha empatado con la banca con {} puntos.".format(jugadores[puntero[0]][0],puntuacion))
    elif puntuacion>contadorIA and len(puntero)==1:
        print("El jugador -{}- ha ganado con {} puntos.".format(jugadores[puntero[0]][0],puntuacion))
    elif puntuacion>contadorIA and len(puntero)!=1:
        print("Los jugadores -{}- han ganado con {} puntos.".format(ganadores,puntuacion))
    elif puntuacion<contadorIA:
        print("Ha ganado la banca con {} puntos.".format(contadorIA))
    a=input("Si estás de acuerdo con la resolución pulsa <Enter>. Si no estás de acuerdo pulsa <Enter> también.")

def apuestas():
    print("HORA DE LAS APUESTAS!")
    copiajugadores=jugadores.copy()
    copiaorden=turno
    igualar=True
    
    global bote
    bote=0
    apuestaanterior=0
    ultimojugador=""
    while igualar==True:
        for  jugador in turno:
            if apuestaanterior!=0 and apuestaanterior==jugadores[jugador][3]:
                    print("Apuesta finalizada")
                    igualar=False
                    break
            if jugadores[jugador][4]==True:

                print("\n Jugador -{}- es su turno, lleva {} apostados y necesita minimo {} para seguir en la partida".format(jugadores[jugador][0],jugadores[jugador][3],(apuestaanterior-jugadores[jugador][3])))
                apuesta=int(input("     Introduce su apuesta: "))
                if (apuesta+jugadores[jugador][3]-1)<tope and apuestaanterior<=(apuesta+jugadores[jugador][3]):
                    print("El jugador -{}- sigue en la partida con su apuesta de {}.".format(jugadores[jugador][0],apuesta))
                    jugadores[jugador][2]-=apuesta
                    jugadores[jugador][3]+=apuesta
                    bote+=apuesta
                    apuestaanterior=jugadores[jugador][3]
                    ultimojugador=jugadores[jugador][0]
    
                else:
                    print("El jugador -{}- está fuera de la partida.".format(jugadores[jugador][0]))
                    jugadores[jugador][4]=False
               
                if apuesta==0:
                    indice=turno.index(jugador)
                    iterador=iter(turno[indice:]+turno[:indice+1])
                    siguiente=next(iterador)
                    siguiente=next(iterador)
                    while jugadores[siguiente][4]==False:
                        siguiente=next(iterador)
                    if apuestaanterior==jugadores[siguiente][3]:
                        print("Apuesta finalizada")
                        igualar=False
                        break
def definirApuestas():
    global tope
    tope=int(input("Introduce las fichas iniciales de cada jugador: "))
    while tope<0:
        tope=int(input("Introduce un numero positivo: "))
    for a in range(len(jugadores)):
        jugadores[a][2]=tope

def ganadorapuestas(jugador):
        print("El jugador {} se ha llevado el bote de {} fichas.".format(bote))

def tiradaIA():
    global contadorIA
    contadorIA=0
    a=input("Turno de la banca. Pulsa <Enter> para continuar ")
    while contadorIA<16:
        contadorIA+=int(random.randint(1,12))
    if contadorIA>21:
        print("La banca se ha pasado de 21")
        contadorIA= -1
    else:
        print("La banca ha sacado un {}.".format(contadorIA))          

def comprobarGanadorSimple():
    a=input("Y el ganador es...")
    if contadorIA>puntuacion:
        print ("La casa ha ganado con {} puntos".format(contadorIA))
    if contadorIA<puntuacion:
        print ("Has ganado con {} puntos".format(puntuacion))
    if contadorIA==puntuacion:
        print ("Habéis empatado con {} puntos. Todos tristes".format(puntuacion))
    a=input("Si estás de acuerdo con la resolución pulsa <Enter>. Si no estás de acuerdo pulsa <Enter> también.")

def tiradaJugadores():
    for jugador in turno:
        enter=input("\nTe toca -{}-. Pulsa <Enter> para tirar. ".format(jugadores[jugador][0]))
        findeturno=True
        while findeturno:
            jugadores[jugador][1]+=tirada2()
            if jugadores[jugador][1]>21:
                print("Te has pasado de 21")
                findeturno=False
                limpiarPantalla()
                jugadores[jugador][1]=-1
            else:
                pregunta=input("Tus tiradas suman {}, ¿quieres seguir tirando? Sí/NO ".format(jugadores[jugador][1]))    
                if pregunta=="no":
                    findeturno=False
                    limpiarPantalla()
                else:
                    while jugadores[jugador][1]>15 and findeturno==True:
                        elegir_tirada=int(input("¿Cuántos dados quieres tirar? (1 o 2): "))
                        if elegir_tirada==1:
                            jugadores[jugador][1]+=tirada1()
                        elif elegir_tirada==2:
                            jugadores[jugador][1]+=tirada2()
                        else:
                            print("Elección no válida")
                        if jugadores[jugador][1]>21:
                            print("Te has pasado de 21")
                            findeturno=False
                            limpiarPantalla()
                            jugadores[jugador][1]=-1
                        else:
                            pregunta=input("Tus tiradas suman {}, ¿quieres seguir tirando? ".format(jugadores[jugador][1]))    
                            if pregunta=="no":
                                findeturno=False
                                limpiarPantalla()

# ====FUNCIONES
def menuJuego():
    juego = True
    while juego:

        print()
        print("       *** BLACKJACK con DADOS ***       ")
        print("*****************************************")
        print("*****************************************")
        print("*                                       *")
        print("*          1- Solo vs Casa              *")
        print("*          2- Multi sin apuestas        *")
        print("*          3- Multi con apuestas        *")
        print("*          4- Salir                     *")
        print("*                                       *")
        print("*****************************************")
        print("*****************************************")
        print()

        opcion = input("Ingresa tu opción: ")
        if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
            print("La opción ingresada es incorrecta. Ingresa\
            una del menú :)")
        elif opcion == "" or opcion == " ": 
            print("La opción ingresada es incorrecta. Ingresa\
            una del menú :)")
        else:
            juego = False
    return int(opcion)

def tirada1():    
    tiradauno=int(random.randint(1,6))
    print("Tu tirada ha sido de un {}.".format(tiradauno))
    return tiradauno

def tirada2():
    tiradauno=int(random.randint(1,6))
    tiradados=int(random.randint(1,6))
    print("Tu tirada ha sido de un {} y un {}.".format(tiradauno,tiradados))
    return tiradauno+tiradados

def nombreJugadores():
    global jugadores
    jugadores=[]
    for a in range(numero_jugadores):
        nombre=input("Introduce el nombre del {} jugador: ".format(d[a+1]))
        jugadores.append([nombre,0,0,0,True])
        #[nombre, mano del jugador, bote, apuesta en mesa, levantarse de la mesa]
    return jugadores      

def definirOrden():
    global turno
    turno=[]
    for a in range(numero_jugadores):
        turno.append(a)
    random.shuffle(turno)
    jugadores=nombreJugadores()
    orden="El orden de tirada será:"
    b=0
    for a in turno:
        b+=1
        orden+=" ["+str(b)+"] "+jugadores[a][0]
    print(orden)  

def tiradaUnJugador():
    a=input("Pulsa <Enter> para tirar los dados. ")
    global puntuacion
    puntuacion=0
    puntuacion+=tirada2()
    while puntuacion<22:
        pregunta=input("Tus tiradas suman {}, ¿quieres seguir tirando? Sí/NO ".format(puntuacion))    
        if pregunta=="no":
            return puntuacion
        elif puntuacion<16:
            puntuacion+=tirada2()
        elif puntuacion>15:
            elegir_tirada=int(input("¿Cuántos dados quieres tirar? (1 o 2): "))
            if elegir_tirada==1:
                puntuacion+=tirada1()
            elif elegir_tirada==2:
                puntuacion+=tirada2()
            else:
                print("Elección no válida")
            if puntuacion>21:
                a=input("Te has pasado de 21. Has perdido")
                menuJuego()
    if puntuacion>21:
        a=input("Te has pasado de 21. Has perdido")
        menuJuego() 

# ====DICCIONARIOS
d={
1:"primer",
2:"segundo",
3:"tercer",
4:"cuarto",
5:"quinto",
6:"sexto",
7:"séptimo"
}

# ====LISTAS
jugadores=[]

# ====VARIABLES
contador = 0
contadorIA = 0
findeturno = False
