import random
def patear():
    goles = 0
    atajadas = 0
    goles_maquina = 0
    for i in range (5):
        direccion = random.randint(1,3)
        lado = int(input("DISPARAR: 1=izquierda, 2=centro, 3=derecho: "))
        if lado == direccion:
            print("FALLASTE!!!")
        else:
            print ("GOLAZO!!!")
            goles = goles+1
        direccion_simulacion = random.randint(1,3)
        atajar = int(input("ATAJAR: 1=izquierda, 2=centro, 3=derecho: "))
        if direccion_simulacion != atajar:
            print("GOL")
            goles_maquina += 1
        else:
            print("Penal atajado!!!")
            atajadas += 1
    print("Has marcado estos goles: ", goles)  
    print("Has atajado estos tiros: ", atajadas )   
    if goles_maquina == goles:
        print("Empate")
    elif goles_maquina < goles:
        print("Ganaste")
    else:
        print("Perdiste")      


patear()    