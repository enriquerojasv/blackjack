from libreria_blackjack import *

jugando = True
while jugando:
    op = menuJuego()
    if op == 1:
        partidaSolo()
    elif op == 2:
        partidaMultiSinApuesta()
    elif op == 3:
        partidaMultiApuesta()
    elif op == 4:
        jugando = False

print("Terminó el juego. Te esperamos de nuevo!!!")





