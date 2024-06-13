#Ordenamiento Burbuja
def Ord_Burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#Ordenamiento Seleccion
def Ord_Seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
#Ordenamiento Inserción
def Ord_Insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
#Busqueda Lineal
def Bus_Lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
#Busqueda Binaria
def Bus_Binaria(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
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