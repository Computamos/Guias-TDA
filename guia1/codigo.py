from typing import Callable
from pprint import pprint
from time import perf_counter
from shutil import get_terminal_size
from math import inf
from random import randint, uniform


C_RESET:str = "\033[0m"
C_ACEPTADO:str = "\033[38;2;39;245;166m"
C_RECHAZADO:str = "\033[38;2;245;77;39m"


class Nodo:
    def __init__(self, valor:int, izq:int = None, der:int = None):
        self.valor = valor
        self.izq = izq
        self.der = der
        pass

class ArbolBinario:

    def __init__(self, raiz:Nodo):
        self.raiz = raiz
        pass


def izquierdaDominante_bruto(i, j, arr):
    if i == j:
        return True
    
    medio = (i + j) // 2

    suma_izq = sum(arr[i:medio+1])
    suma_der = sum(arr[medio+1:j+1])

    if suma_izq < suma_der:
        return False
    
    return izquierdaDominante_bruto(i, medio, arr) and \
           izquierdaDominante_bruto(medio+1, j, arr)

def izquierdaDominante(i:int, j:int, arreglo:list[int])->bool:

    # Conquer
    if j - i == 1:
        return arreglo[i] > arreglo[j]
    
    # Divide
    medio:int = (j + i) // 2 

    # Conquer
    suma_izq = 0
    for k in range(i, medio+1):
        suma_izq += arreglo[k]

    suma_der:int = 0
    for k in range(medio+1, j+1):
        suma_der += arreglo[k]

    if suma_izq < suma_der:
        return False
    
    # Combine
    return izquierdaDominante(i, medio, arreglo) and izquierdaDominante(medio+1, j, arreglo) 


def indiceEspejo_bruto(arreglo:list[int]):
    for i in range(len(arreglo)):
        if arreglo[i] == i:
            return True
    return False

def indiceEspejo(i:int, j:int, arreglo:list[int]):

    if i > j:
        return False
    
    indice_act = (j+i) // 2
    actual = arreglo[indice_act]
    
    if actual == indice_act:
        return True
    elif actual > indice_act:
        return indiceEspejo(i, indice_act-1, arreglo)
    else:
        return indiceEspejo(indice_act+1, j, arreglo)
    
# arreglo:list[int] = [-4, -1, 2, 4, 7]
# print(indiceEspejo(0, len(arreglo)-1, arreglo))

def potenciaLogaritmica_bruto(base:int, potencia:int)->int:
    return pow(base, potencia)

def potenciaLogaritmica(base:int, potencia:int)->int:

    # Conquer
    if potencia == 0:
        return 1
    elif potencia == 1:
        return base

    # Divide
    potencia_en_par:int = potencia // 2
    otro_calculo:int = potenciaLogaritmica(base, potencia_en_par)
    
    # Combine
    if potencia % 2 == 1:
        return base * potenciaLogaritmica(base, potencia - 1)

    return otro_calculo * otro_calculo

# base:int = 2
# potencia:int = 10
# print(potenciaLogaritmica(base, potencia))

def maximoMontania_bruto(arreglo: list[int]) -> int:
    if not arreglo:
        return -inf
    
    # Inicializamos con el primer elemento
    maximo = arreglo[0]
    
    # Recorremos todo el arreglo comparando
    for numero in arreglo:
        if numero > maximo:
            maximo = numero
            
    return maximo

def maximoMontania(i:int, j:int, arreglo:list[int])->int:

    if i > j:
        return -inf

    indice_actual = (j + i) // 2
    actual = arreglo[indice_actual]

    va_creciendo:bool = arreglo[indice_actual-1] < actual
    va_decreciendo:bool = arreglo[indice_actual+1] < actual
    
    if va_creciendo and va_decreciendo:
        return actual
    elif va_creciendo and not va_decreciendo:
        return maximoMontania(indice_actual+1, j, arreglo)
    else:
        # not va_creciendo and va_decreciendo:
        return maximoMontania(i, indice_actual, arreglo)

# arreglo:list[int] = [-1, 3, 8, 22, 30, 22, 8, 4, 2, 1]
# input(maximoMontania(0, len(arreglo), arreglo))

def maximaSubsecuencia_bruto(array: list[int]) -> int:
    n = len(array)
    if n == 0: return -float('inf')
    
    max_suma = -float('inf')
    
    for i in range(n):
        suma_acumulada = 0
        for j in range(i, n):
            # En cada paso del segundo bucle, ya tenemos la suma anterior
            # Solo le sumamos el nuevo elemento array[j]
            suma_acumulada += array[j]
            if suma_acumulada > max_suma:
                max_suma = suma_acumulada
                
    return max_suma

def maximaSubsecuencia(i:int, j:int, array:list[int]):
    
    # Conquistar
    if i == j:
        return array[i]
    
    # Dividir
    medio:int = (i + j) // 2
    mitad_izquierda:int = maximaSubsecuencia(i, medio, array)
    mitad_derecho:int = maximaSubsecuencia(medio+1, j, array)

    acc:int = 0
    suma_izquierda:int = -inf
    for k in range(medio, i-1, -1):
        acc +=  array[k]
        suma_izquierda = max(suma_izquierda, acc)
    
    acc:int = 0
    suma_derecha:int = -inf
    for k in range(medio+1, j+1):
        acc +=  array[k]
        suma_derecha = max(suma_derecha, acc)

    suma_medio:int = suma_izquierda + suma_derecha

    # Combine
    return max(mitad_izquierda, mitad_derecho, suma_medio)

# arreglo:list[int] = [3, -1, 4, 8, -2, 2, -7, 5]
# input(maximaSubsecuencia(0, len(arreglo)-1, arreglo))

def potenciaSum_bruto(base:int, potencia:int)->int:
    
    sumatoria:int = 0
    for i in range(1, potencia+1):
        sumatoria += pow(base, i) 
    return sumatoria

# input(potenciaSum_bruto(2, 4))

def potenciaSum(base:int, potencia:int)->int:
    """
    Voy a dar el algoritmo trabajando con enteros 
    porque es exactamente el mismo concepto y me da fiaca hacerlo con matrices posta.
    """

    if potencia == 1:
        return base

    potencia_mitad:int = potencia // 2
    res_parcial:int = potenciaSum(base, potencia_mitad)

    return res_parcial + pow(base, potencia_mitad) * res_parcial

# input(potenciaSum(2, 4))

def armar_arbol_binario(cantidad_nodos: int) -> Nodo:
    
    if cantidad_nodos <= 0:
        return None

    # Generar valores únicos
    valores = set()
    while len(valores) < cantidad_nodos:
        valores.add(randint(-1000000, 1000000))
    lista = list(valores)

    # Crear todos los nodos
    nodos = [Nodo(v) for v in lista]

    # Conectarlos aleatoriamente: cada nodo (salvo la raíz)
    # se asigna como hijo de algún nodo anterior
    for i in range(1, len(nodos)):
        while True:
            padre = nodos[randint(0, i - 1)]
            if padre.izq is None:
                padre.izq = nodos[i]
                break
            elif padre.der is None:
                padre.der = nodos[i]
                break
            # Si el padre elegido ya está lleno, se elige otro

    return nodos[0]

def distanciaMaxima_bruto(raiz: Nodo) -> int:

    def obtener_nodos(nodo) -> list:
        if nodo is None:
            return []
        return [nodo] + obtener_nodos(nodo.izq) + obtener_nodos(nodo.der)

    def calcular_profundidades(nodo, prof=0, mapa=None) -> dict:
        """Devuelve un dict {nodo: profundidad} para todos los nodos."""
        if mapa is None:
            mapa = {}
        if nodo is None:
            return mapa
        mapa[nodo] = prof
        calcular_profundidades(nodo.izq, prof + 1, mapa)
        calcular_profundidades(nodo.der, prof + 1, mapa)
        return mapa

    def lca(nodo_actual, a, b) -> Nodo | None:
        """Encuentra el ancestro común más bajo de a y b."""
        if nodo_actual is None:
            return None
        if nodo_actual is a or nodo_actual is b:
            return nodo_actual
        izq = lca(nodo_actual.izq, a, b)
        der = lca(nodo_actual.der, a, b)
        if izq and der:
            return nodo_actual  # a y b están en subárboles distintos
        return izq if izq else der

    nodos = obtener_nodos(raiz)
    profundidades = calcular_profundidades(raiz)
    max_dist = 0

    for i in range(len(nodos)):
        for j in range(i + 1, len(nodos)):
            ancestro = lca(raiz, nodos[i], nodos[j])
            d = profundidades[nodos[i]] + profundidades[nodos[j]] - 2 * profundidades[ancestro]
            if d > max_dist:
                max_dist = d

    return max_dist

def distanciaMaxima(nodoAct:Nodo)->tuple[int, int]:

    if nodoAct is None:
        return (0, 0)

    h_izq, c_izq = distanciaMaxima(nodoAct.izq)
    h_der, c_der = distanciaMaxima(nodoAct.der)
    
    h_actual:int = 1 + max(h_izq, h_der)
    cruzado:int = h_izq + h_der
    
    return h_actual, max(c_izq, c_der, cruzado)

# raiz = armar_arbol_binario(100)
# input(f"bruto={distanciaMaxima_bruto(raiz)}, D&C={distanciaMaxima(raiz)}")

def desordenSort_bruto(array:list[int])->int:

    largo = len(array)
    desordenados:int = 0
    for i in range(largo):
        for j in range(i+1, largo):
            if array[i] > array[j]:
                desordenados += 1

    return desordenados

def merge(array_izq:list[int], array_der:list[int])->tuple[list[int], int]:

    k = t = 0

    largo_izq:int = len(array_izq)
    largo_der:int = len(array_der)

    mergeados:list[int] = []

    cant_p_desorden:int = 0 
    while k < largo_izq and t < largo_der:
        if array_izq[k] <= array_der[t]:
            mergeados.append(array_izq[k])
            k += 1
        else:
            cant_p_desorden += largo_izq - k
            mergeados.append(array_der[t])
            t += 1

    mergeados += array_izq[k:]
    mergeados += array_der[t:]
        
    return mergeados, cant_p_desorden

def desordenSort(array:list[int])->tuple[list[int], int]:

    largo = len(array)

    # Conquer
    if largo <= 1:
        return array, 0
    
    # Divide
    mitad:int = largo // 2
    array_izq, cant_izq = desordenSort(array[:mitad])
    array_der, cant_der = desordenSort(array[mitad:])
    
    # Combine
    array, cant_merge = merge(array_izq, array_der)

    # Conquer
    return array, cant_izq + cant_der + cant_merge

# array:list[int] = [3, 7, 1, 2, 5]
# input(desordenSort_bruto(array))

def armar_matriz_booleana(cant_filas: int) -> list[list[bool]]:

    matriz: list[list[bool]] = []
    cant_bools: dict[bool, int] = {True: 0, False: 0}
    for _ in range(cant_filas):
        fila: list[bool] = []
        for _ in range(cant_filas):
            valor: bool = bool(randint(0, 1))
            cant_bools[valor] += 1
            fila.append(valor)

        matriz.append(fila)

    if cant_bools[False] == 0: # Forzamos que haya un False (por consigna)
        i: int = randint(0, cant_filas - 1)
        j: int = randint(0, cant_filas - 1)
        matriz[i][j] = False

    return matriz


def conjuncionSubmatriz(
        i_0: int, i_1: int, j_0: int, j_1: int, matriz: list[list[bool]]
) -> bool:

    for i in range(i_0, i_1):
        for j in range(j_0, j_1):
            if not matriz[i][j]: # if matriz[i][j] == False
                return False

    return True


def cazadorDeFalsos(
        i_0: int, i_1: int, j_0: int, j_1: int, matriz: list[list[bool]]
) -> tuple[int, int]:

    # Conquer
    if i_1 - i_0 == 1 and j_1 - j_0 == 1:
        if not matriz[i_0][j_0]: # if matriz[i_0][j_0] == False
            return (i_0, j_0)
        return None

    # Divide
    mitad_filas: int = (i_1 + i_0) // 2
    mitad_columnas: int = (j_1 + j_0) // 2

    mitades = (
        (i_0, mitad_filas, j_0, mitad_columnas),
        (mitad_filas, i_1, j_0, mitad_columnas),
        (i_0, mitad_filas, mitad_columnas, j_1),
        (mitad_filas, i_1, mitad_columnas, j_1),
    )

    # Combine
    for mitad in mitades:
        i, i_, j, j_ = mitad
        if not conjuncionSubmatriz(i, i_, j, j_, matriz):
            return cazadorDeFalsos(i, i_, j, j_, matriz)


# cant_filas: int = 4
# matriz: list[list[bool]] = armar_matriz_booleana(cant_filas)

# pprint(matriz, indent=2)
# input(cazadorDeFalsos(0, cant_filas, 0, cant_filas, matriz))


def cazadorDeFalsosContador_bruto(matriz: list[list[bool]]) -> tuple[int, int]:
    largo = len(matriz)
    contador: int = 0
    for i in range(largo):
        for j in range(largo):
            if not matriz[i][j]: # if matriz[i][j] == False
                contador += 1

    return contador


def cazadorDeFalsosContador(
    i_0: int, i_1: int, j_0: int, j_1: int, matriz: list[list[bool]]
) -> tuple[int, int]:

    # Conquer
    if i_1 - i_0 == 1 and j_1 - j_0 == 1:
        res:int = 0
        if not matriz[i_0][j_0]: # if matriz[i_0][j_0] == False
            res += 1
        return res

    # Divide
    mitad_filas: int = (i_1 + i_0) // 2
    mitad_columnas: int = (j_1 + j_0) // 2

    mitades = (
        (i_0, mitad_filas, j_0, mitad_columnas),
        (mitad_filas, i_1, j_0, mitad_columnas),
        (i_0, mitad_filas, mitad_columnas, j_1),
        (mitad_filas, i_1, mitad_columnas, j_1),
    )

    # Combine
    contador: int = 0
    for mitad in mitades:
        i, i_, j, j_ = mitad
        if not conjuncionSubmatriz(i, i_, j, j_, matriz):
            contador += cazadorDeFalsosContador(i, i_, j, j_, matriz)

    return contador


# cant_filas: int = 4
# matriz: list[list[bool]] = armar_matriz_booleana(cant_filas)

# pprint(matriz, indent=2)
# input(cazadorDeFalsosContador(0, cant_filas, 0, cant_filas, matriz))

def testear_todo(cant_test_por_ejercicio:int = 100):
    
    ancho, _ = get_terminal_size()
    frase_en:str = "⏤ Testeando ⏤"
    frase_out:str = "⏤ Tests finalizados ⏤"
    divisor_en = "\n" + " "*((ancho- len(frase_en)) // 2) + frase_en 
    divisor_in = "⊰" + "⏤"*(ancho-2) +"⊱"
    divisor_out = " "*((ancho-len(frase_out)) // 2) + frase_out

    def t_izquierdaDominante()->bool:

        for _ in range(cant_test_por_ejercicio):

            tamanio_array:int = pow(2, randint(1, 20))
            
            arreglo_temp:list[int] = [] # esperemos que con esto salga un array que sea izqDom
            for _ in range(tamanio_array):
                arreglo_temp.append(randint(0, 100000))
            
            res_bruto:bool = izquierdaDominante_bruto(0, tamanio_array-1, arreglo_temp)
            res_ejer:bool = izquierdaDominante(0, tamanio_array-1, arreglo_temp)
            
            paso:bool = res_bruto == res_ejer
            if not paso:
                return False
            
        return True

    def t_indiceEspejo()->bool:

        for _ in range(cant_test_por_ejercicio):

            tamanio_array:int = pow(2, randint(1, 20))
            
            arreglo_temp:list[int] = [] # esperemos que con esto salga un array que tenga indEspj
            ultimo_gen:int= uniform(-1000000, 1000000)
            for _ in range(tamanio_array):
                ultimo_gen += randint(1, randint(2, 10))
                arreglo_temp.append(ultimo_gen)

            res_bruto:bool = indiceEspejo_bruto(arreglo_temp)
            res_ejer:bool = indiceEspejo(0, tamanio_array-1, arreglo_temp)
            
            paso:bool = res_bruto == res_ejer
            if not paso:
                return False
            
        return True
    
    def t_potenciaLogaritmica():

        for _ in range(cant_test_por_ejercicio):

            base:int = randint(1, 100)
            potencia:int = randint(1, 15)

            res_bruto:int = potenciaLogaritmica_bruto(base, potencia)
            res_ejer:int = potenciaLogaritmica(base, potencia)

            paso:bool = res_bruto == res_ejer
            if not paso:
                return False
            
        return True
        
    def t_maximoMontania():

        for _ in range(cant_test_por_ejercicio):
                
                tamanio_array: int = pow(2, randint(2, 20)) 
                
                # 1. Decidir en qué índice estará el pico (mínimo en la posición 1, máximo en n-2)
                indice_pico = randint(1, tamanio_array - 2)
                
                arreglo_temp = [0] * tamanio_array
                
                # 2. Generar la parte creciente
                valor_actual = randint(-1000, 0)
                for i in range(indice_pico + 1):
                    arreglo_temp[i] = valor_actual
                    valor_actual += randint(1, 10) # Siempre sube
                    
                # 3. Generar la parte decreciente
                # Empezamos desde el valor del pico y restamos
                valor_actual = arreglo_temp[indice_pico]
                for i in range(indice_pico + 1, tamanio_array):
                    valor_actual -= randint(1, 10) # Siempre baja
                    arreglo_temp[i] = valor_actual

                # 4. Ejecutar ambos algoritmos
                # Nota: Asegúrate de que maximoMontania_bruto devuelva el VALOR, no un bool
                res_bruto = maximoMontania_bruto(arreglo_temp)
                res_ejer = maximoMontania(0, tamanio_array - 1, arreglo_temp)
                
                # 5. Comparar resultados
                if res_bruto != res_ejer:
                    return False
                    
        return True

    def t_maximaSubsecuencia()->bool:

        for _ in range(cant_test_por_ejercicio):

            tamanio_array:int = randint(1, 3000)
            
            arreglo_temp:list[int] = []
            for _ in range(tamanio_array):
                arreglo_temp.append(randint(-1000000, 1000000))
            
            res_bruto:bool = maximaSubsecuencia_bruto(arreglo_temp)
            res_ejer:bool = maximaSubsecuencia(0, tamanio_array-1, arreglo_temp)
            
            paso:bool = res_bruto == res_ejer
            if not paso:
                return False
            
        return True
    
    def t_potenciaSum():

        for _ in range(cant_test_por_ejercicio):

            base:int = randint(1, 10)
            potencia:int = pow(2, randint(1, 14))

            res_bruto:int = potenciaSum_bruto(base, potencia)
            res_ejer:int = potenciaSum(base, potencia)

            paso:bool = res_bruto == res_ejer
            if not paso:
                return False
            
        return True
    
    def t_distanciaMaxima():

        for _ in range(cant_test_por_ejercicio):

            cant_nodos:int = randint(1, 200)
            raiz = armar_arbol_binario(cant_nodos)

            res_bruto:int = distanciaMaxima_bruto(raiz)
            _, res_ejer = distanciaMaxima(raiz)

            paso:bool = res_bruto == res_ejer
            if not paso:
                return False
            
        return True

    def t_desordenSort()->bool:

        for _ in range(cant_test_por_ejercicio):

            tamanio_array:int = randint(1, 3000)
            
            arreglo_temp:list[int] = []
            for _ in range(tamanio_array):
                arreglo_temp.append(randint(-1000000, 1000000))
            
            res_bruto:int = desordenSort_bruto(arreglo_temp)
            _, res_ejer = desordenSort(arreglo_temp)
            
            paso:bool = res_bruto == res_ejer
            if not paso:
                print(res_bruto, res_ejer)
                return False
            
        return True

    def t_cazadorDeFalsos():

        for _ in range(cant_test_por_ejercicio):

            n: int = randint(1, 500)
            matriz: list[list[int]] = armar_matriz_booleana(n)

            i_res, j_res = cazadorDeFalsos(0, n, 0, n, matriz)

            if matriz[i_res][j_res]: # if matriz[i_res][j_res] == False
                return False

        return True

    def t_cazadorDeFalsosContador():
        for _ in range(cant_test_por_ejercicio):

            n: int = randint(1, 500)
            matriz: list[list[int]] = armar_matriz_booleana(n)

            res_bruto: int = cazadorDeFalsosContador_bruto(matriz)
            res_ejer: int = cazadorDeFalsosContador(0, n, 0, n, matriz)

            paso: bool = res_bruto == res_ejer
            if not paso:
                return False

        return True

    tests:list[Callable] = [
        t_izquierdaDominante, 
        t_indiceEspejo, 
        t_potenciaLogaritmica, 
        t_maximoMontania,
        t_maximaSubsecuencia,
        t_potenciaSum,
        t_distanciaMaxima,
        t_desordenSort,
        t_cazadorDeFalsos,
        t_cazadorDeFalsosContador,
        ]

    print(divisor_en)
    for t in tests:
        nombre_test:str = t.__name__
        nombre_test = nombre_test[2:len(nombre_test)]

        print(divisor_in)
        print(f"Probando {cant_test_por_ejercicio} tests para {nombre_test}.")
        start:float = perf_counter()
        res:bool = t()
        finish:float = perf_counter()

        print(f"Estado: {f'{C_ACEPTADO}Aceptado{C_RESET}' if res else f'{C_RECHAZADO}Rechazado{C_RESET}'}")
        print(f"Tiempo de ejecución tomado para {cant_test_por_ejercicio} tests: {finish-start: .4f} segundos.")

    print(divisor_in)
    print(divisor_out)

if __name__ == "__main__":
    testear_todo()