
def ingresarJugador(jugadores):
    onlineName=input('ingrese su nombre online:').lower
    nombre=input('ingrese su nombre(tanto nombre como apellido): ').lower
    Juegos=input('ingrese los juegos en los que participa:').lower
    PuntajeValo=input('ingrese el puntaje en Valorant(dejar en blanco si no tiene): ')
    PuntajeFort=input('ingrese el puntaje en Fortnite(dejar en blanco si no tiene): ')
    PuntajeFifa=input('ingrese el puntaje en Fifa(dejar en blanco si no tiene): ')
    Dificultad=input('ingrese la dificultad en la que participo(Principiante - Avanzado - Experto): ').lower
    Juegos
    jugadores.append({
        'Id Jugador': onlineName,
        'Nombre': nombre,
        'Valortant': PuntajeValo,
        'Fortnite': PuntajeFort,
        'fifa': PuntajeFifa,
        'Tipo': Dificultad
    })

def listaPuntajes(jugadores):
    for onlineName,nommbre,PuntajeValo,PuntajeFort,PuntajeFifa,Dificultad in jugadores:
        print(f'Id Online {onlineName}')
        print(f'Nombre del jugador {nommbre}')
        print(f'Puntaje valorant {PuntajeValo}')
        print(f'Puntaje Fortnite {PuntajeFort}')
        print(f'Puntaje Fifa {PuntajeFifa}')
        print(f'Tipo Participante {Dificultad}')

def ImprimirPorTipo(jugadores):
    flag2=True
    Imprimir=[]
    while flag2==True:
        try:
            OpcTipo=input(int('ingrese tipo de dificultad a imprimir(1°Principiante, 2°Avanzado o 3°Experto(ingrese numeros)): '))
            if 1<=OpcTipo<=3:
                print('tiene que estar en este rango')
        except:
            print('Tiene que ser numero')

        if OpcTipo == 1:
            OpcTipo = 'principiante'
            for OpcTipo in jugadores:
                Imprimir.append(jugadores)
        elif OpcTipo ==2:
            OpcTipo = 'avanzado'
            for OpcTipo in jugadores:
                Imprimir.append(jugadores)
        elif OpcTipo == 3:
            OpcTipo == 'experto'
            for OpcTipo in jugadores:
                Imprimir.append(jugadores)
        else:   
            print('opcion no correcta')
    JugadoresAImprimir='Imprimir por tipo.txt'
    with open(JugadoresAImprimir,'w') as archivo:
        for jugador in Imprimir:
            archivo.write(f'Id jugador{jugador['onlineName']}\n')
            archivo.write(f'Nombre{jugador['nombre]']}\n')
            archivo.write(f'Puntaje Valorant{jugador['PuntajeValo']}\n')
            archivo.write(f'Puntaje Fortnite{jugador['PuntajeFort']}\n')
            archivo.write(f'Puntaje Fifa{jugador['PuntajeFifa']}\n')
            archivo.write(f'Tipo Participante{jugador['Dificultad']}\n')



