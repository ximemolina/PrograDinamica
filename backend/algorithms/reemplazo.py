''' Algoritmo de reemplazos '''

def obtener_costos_anuales(periodos, costo_inicial): # costo = compra + mantenimiento acumulado - reventa
    costo_acumulado = 0
    for i in range(len(periodos)):
        costo_acumulado += periodos[i]['mantenimiento']
        periodos[i]['costo_acumulado'] = costo_inicial + costo_acumulado - periodos[i]['reventa']

def rutas(año_compro, plazo, mejores):

    if año_compro == plazo: # La única ruta posible es la que solo contiene el año final
        return [[plazo]]

    todas_las_rutas = []

    for año_vendo in mejores[año_compro]: # Probamos cada año de venta que empata en el mínimo

        rutas_siguientes = rutas(año_vendo, plazo, mejores)

        for ruta in rutas_siguientes:
            ruta_completa = [año_compro] + ruta
            todas_las_rutas.append(ruta_completa)

    return todas_las_rutas

def formatear_tabla(plazo, costo_min, mejores):
    encabezado = ["t", "G(t)", "Proximo"]
    filas = [encabezado]

    for año_compro in range(plazo + 1):  # de 0 hasta plazo
        if mejores[año_compro]:           # hay decisión (lista con elementos)
            siguientes = mejores[año_compro]
        else:                             # año final, lista vacía
            siguientes = "fin"

        filas.append([año_compro, costo_min[año_compro], siguientes])

    return filas

def reemplazo(costo_inicial, plazo, vida_util, periodos):
    if(plazo < 1 or plazo > 30):
        return {"error": "El plazo del proyecto debe ser de 1 a 30"}

    if(vida_util < 1 or vida_util > 10):
        return {"error": "La vida util del proyecto debe ser 1 a 10"}

    if(len(periodos)!=vida_util):
        return {"error": "El arreglo de periodos debe tener una cantidad de elementos igual a VidaUtil"}

    obtener_costos_anuales(periodos, costo_inicial)

    costo_min = {plazo: 0}
    mejores = {plazo: []}        # lista de años de venta que logran ese mínimo


    for año_compro in range(plazo - 1, -1, -1):
        opciones = {}
        for año_vendo in range(año_compro + 1, min(año_compro + vida_util, plazo) + 1):
            opciones[año_vendo] = periodos[año_vendo - año_compro - 1]['costo_acumulado'] + costo_min[año_vendo]

        costo_min[año_compro] = min(opciones.values())

        mejores[año_compro] = []
        for año_vendo, costo in opciones.items():
            if costo == costo_min[año_compro]:
                mejores[año_compro].append(año_vendo)

 

    tabla = formatear_tabla(plazo, costo_min, mejores)

    return {"resultado": costo_min[0],"rutas": rutas(0, plazo, mejores),"tabla":tabla}
