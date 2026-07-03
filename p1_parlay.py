<<<<<<< HEAD
def pedir_cuota():
    while True:
        numero = input("Ingresa la cuota o listo para terminar: ")
        if numero == 'listo':
            break
        else:
            cuota = float(numero)  
            if cuota <= 1 :
                print("Ingrese una cuota mayor a 1")
            else:
                parlay = cuota * parlay

def calcular_ganancia(monto, parlay):
    monto = float(input("Ingrese monto a apostar: "))
    supestaGanancia = monto * parlay
    print("El total de ganancia de tu parlay es: ", supestaGanancia)
    print("El total de cuota de tu parlay es: ", parlay)

        
=======
def pedir_cuota():
    cuota_total = 1
    while True:
        numero = input("Ingresa la cuota o listo para terminar: ")
        if numero == 'listo':
            break
        else:
            cuota = float(numero)  
            if cuota <= 1 :
                print("Ingrese una cuota mayor a 1")
            else:
                cuota_total = cuota * cuota_total
    return cuota_total               



def calcular_ganancia(parlay):
    monto = float(input("Ingrese monto a apostar: "))
    supestaGanancia = monto * parlay
    print("El total de ganancia de tu parlay es: ", supestaGanancia)
    print("El total de cuota de tu parlay es: ", parlay)

           
mi_parlay = pedir_cuota()
calcular_ganancia(mi_parlay)
>>>>>>> 17b2f3041438a0eb44172cb7194acec461c4c562
