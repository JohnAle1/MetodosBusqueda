#Ordenamiento Burbuja
def Ord_Burbuja(Lista):
    n = len(Lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if Lista[j] > Lista[j+1]:
                Lista[j], Lista[j+1] = Lista[j+1], Lista[j]
    return Lista
#Ordenamiento Seleccion
def Ord_Seleccion(Lista):
    n = len(Lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if Lista[j] < Lista[min_idx]:
                min_idx = j
        Lista[i], Lista[min_idx] = Lista[min_idx], Lista[i]
    return Lista
#Ordenamiento Inserción
def Ord_Insercion(Lista):
    for i in range(1, len(Lista)):
        key = Lista[i]
        j = i-1
        while j >= 0 and key < Lista[j]:
            Lista[j + 1] = Lista[j]
            j -= 1
        Lista[j + 1] = key
    return Lista
#Busqueda Lineal
def Bus_Lineal(Lista, x):
    for i in range(len(Lista)):
        if Lista[i] == x:
            return i
    return -1
#Busqueda Binaria
def Bus_Binaria(Lista, x):
    low = 0
    high = len(Lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if Lista[mid] == x:
            return mid
        elif Lista[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#Listas para procesos
ListaElementos = [5,1,6,4,3,8,2,7]
ListaElementos1 = [1,2,3,4,5,6,7,8]
#Resultados de procesos
print(f"Burbuja es: {Ord_Burbuja(ListaElementos)}")
print(f"Seleccion es: {Ord_Seleccion(ListaElementos)}")
print(f"Insercion es: {Ord_Insercion(ListaElementos)}")
#Busquedas
print(f"Bus Binaria es: {Bus_Binaria(ListaElementos1, 5)}")
print(f"Bus Lineal es: {Bus_Lineal(ListaElementos1, 8)}")
#Ordenamiento Rapido
def Ordenamiento_Rapido(Lista):
    if len(Lista) <= 1:
        return Lista
    else:
        pivot = Lista[len(Lista) // 2]  # Selecciona el pivote
        izquierda = [x for x in Lista if x < pivot]  # Sublista de elementos menores que el pivote
        centro = [x for x in Lista if x == pivot]  # Sublista de elementos iguales al pivote
        derecha = [x for x in Lista if x > pivot]  # Sublista de elementos mayores que el pivote
        return Ordenamiento_Rapido(izquierda) + centro + Ordenamiento_Rapido(derecha)

# Ejemplo de uso
Lista = [3, 6, 8, 10, 1, 2, 1]
print(Ordenamiento_Rapido(Lista))  # Debería imprimir [1, 1, 2, 3, 6, 8, 10]
