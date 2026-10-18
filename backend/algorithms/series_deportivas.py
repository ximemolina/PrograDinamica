''' Algoritmo de series deportivas '''

def series(juegos, probabilidad_casa, probabilidad_visita, formato):

    if(juegos > 11 or juegos < 0 or not juegos % 2):
        return {"error": "Los juegos deben ser un número impar de 1 a 11"}

    if(len(formato) < juegos):
        return{"error": "Debe de ingresar el formato para todos los juegos"}

    if(probabilidad_casa > 1 or probabilidad_visita > 1 or probabilidad_visita < 0 or probabilidad_casa < 0):
        return {"error": "Las probabilidades deben ser un número del 0 al 1"}
        
    juegos_a_ganar= juegos//2 + 1
    matriz_respuesta= []
    for i in range(juegos_a_ganar+1 ): # comienza por 0, por eso el +1
        matriz_respuesta.append([])
        for j in range(juegos//2 + 2 ):

            matriz_respuesta[i].append([])
            
            if(i==0 and j==0):
                matriz_respuesta[i][j]= "-"
            elif(i==0):
                matriz_respuesta[i][j] = 1
            elif (j==0):
                matriz_respuesta[i][j]= 0
            elif( formato[(juegos_a_ganar-i) + (juegos_a_ganar-j)] ):
                matriz_respuesta[i][j]=round((1-probabilidad_casa)*matriz_respuesta[i][j-1]+ probabilidad_casa*matriz_respuesta[i-1][j],4)
            else:
                matriz_respuesta[i][j]=round((1-probabilidad_visita)*matriz_respuesta[i][j-1]+ probabilidad_visita*matriz_respuesta[i-1][j],4)

    return {"resultado": matriz_respuesta}