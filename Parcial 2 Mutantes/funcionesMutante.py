# Función para crear una lista de ADN con 6 líneas, cada una de 6 caracteres válidos.
def AdnCreation():
    adn=[]# Lista vacía para almacenar las líneas de ADN
    Validation=True # Variable de validación para comprobar si una línea de ADN es válida
    iteration=0# Contador de iteraciones, se detendrá después de 6 iteraciones
    while(6>iteration):
        Validation=True
        ValidationAmount=0
        while (Validation):
            # Solicitar al usuario que ingrese una línea de ADN
            lineString=input(str("Ingrese una linea de adn solo con estos caracteres(A,C,G,T) ej: acgtta "))
            # Validar los datos para que sean los pedidos en caso contrario volver a ingresar 
            if len(lineString)==6:
                for i in lineString:
                    if i.lower()=="a" or i.lower()=="c" or i.lower()=="t" or i.lower()=="g":
                        ValidationAmount+=1
                    else:
                        print("Dato incorrecto")
                        Validation=True
                    if ValidationAmount==6:
                        print("Datos correctos")
                        adn.append(lineString.lower())# Agregar la línea de ADN válida a la lista
                        Validation=False
            else:
                print("Dato incorrecto")
                Validation=True
        iteration+=1
    return adn

# Función para verificar si hay una secuencia de 4 caracteres idénticos en una fila.
def MutantLine(adn):
    num=0
    for i in range(3):
        for j in range(3):
            if adn[i][j]==adn[i][j+1] and adn[i][j+1]==adn[i][j+2] and adn[i][j+2]==adn[i][j+3]:
                num+=1
                if num >= 1:  # Si se encuentra una secuencia, detener la búsqueda
                    return num
    return num
            
# Funcion para verificar si hay una secuencia de 4 caracteres idénticos en una columna
def MutanColum(adn):
    num=0
    for i in range(3):
        for j in range(3):
            if adn[j][i]==adn[j+1][i] and adn[j+1][i]==adn[j+2][i]and adn[j+2][i]==adn[j+3][i]:
                num+=1
                if num >= 1:  # Si se encuentra una secuencia, detener la búsqueda
                    return num
    return num

# Funcion para verificar si hay una secuencia de 4 caracteres idénticos en una diagonal
def MutantDigonal(adn):
    num=0
    for i in range(3):
        for j in range(3):
                if adn[i][j]==adn[i+1][j+1]and adn[i+1][j+1]==adn[i+2][j+2] and adn[i+2][j+2]==adn[i+3][j+3]:
                    num+=1
                    if num >= 1:  # Si se encuentra una secuencia, detener la búsqueda
                        return num
    return num

# Funcion para verificar si hay una secuencia de 4 caracteres idénticos en una digonal empezando desde abajo a la izquierda
def MutantDigonalRevez(adn):
    num=0
    for i in range(5,2,-1):
        for j in range(3):
                if adn[i][j]==adn[i-1][j+1]and adn[i-1][j+1]==adn[i-2][j+2] and adn[i-2][j+2]==adn[i-3][j+3]:
                    num+=1
                    if num >= 1:  # Si se encuentra una secuencia, detener la búsqueda
                        return num
    return num

# Función principal para verificar si un ADN es mutante.
def is_Mutant(adn):
    total_mutations = MutantLine(adn) + MutanColum(adn) + MutantDigonal(adn) + MutantDigonalRevez(adn)
    print(f"Cantidad de mutaciones en linea={MutantLine(adn)}")
    print(f"Cantidad de mutaciones en columna={MutanColum(adn)}")
    print(f"Cantidad de mutaciones en diagonal={MutantDigonal(adn)}")
    print(f"Cantidad de mutaciones en diagonal inversa={MutantDigonalRevez(adn)}")
    if total_mutations > 1:  # Si hay más de una secuencia de 4 caracteres idénticos, se considera mutante
        return True
    else:
        return False
