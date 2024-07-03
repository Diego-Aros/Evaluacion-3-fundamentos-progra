import Dfunciones as fun
jugadores =[]
flag=True
opc=1

while 1<=opc<=4:
    print('1°-Registrar puntajes torneo')
    print('2°-Listas Puntajes')
    print('3°-Imprimir por tipo')
    print('4°-Salir')
    opc=int(input('ingrese opcion:'))
    if opc==1:
        fun.ingresarJugador(jugadores)
    elif opc==2: 
        fun.listaPuntajes(jugadores)
    elif opc==3:
        fun.ImprimirPorTipo(jugadores)
    elif opc==4:
        print('Saliendo')
    else:
        print('opcion no valida')
