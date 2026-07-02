parlay = 1
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

monto = float(input("Ingrese monto a apostar: "))
supestaGanancia = monto * parlay
print("El total de ganancia de tu parlay es: ", supestaGanancia)
print("El total de cuota de tu parlay es: ", parlay)
    