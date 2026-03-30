from typing import Callable
from pprint import pprint
from time import perf_counter
from shutil import get_terminal_size
from math import inf
from random import randint, uniform
from itertools import permutations


def es_magico(cuadrado, n):
    # suma de la primera fila como referencia
    suma_ref = sum(cuadrado[0])

    # filas
    for i in range(n):
        if sum(cuadrado[i]) != suma_ref:
            return False

    # columnas
    for j in range(n):
        if sum(cuadrado[i][j] for i in range(n)) != suma_ref:
            return False

    # diagonal principal
    if sum(cuadrado[i][i] for i in range(n)) != suma_ref:
        return False

    # diagonal secundaria
    if sum(cuadrado[i][n-1-i] for i in range(n)) != suma_ref:
        return False

    return True


def contar_magiCuadrados_bruto(n):
    numeros = list(range(1, n*n + 1))
    contador = 0

    for perm in permutations(numeros):
        # convertir permutación en matriz
        cuadrado = [
            list(perm[i*n:(i+1)*n])
            for i in range(n)
        ]

        if es_magico(cuadrado, n):
            contador += 1

    return contador

usados: set = set()
cuadrado: list[list[int]] = []

def es_valido(i: int, j: int, n: int, suma_objetivo) -> bool:
    global cuadrado

    if suma_objetivo is None:
        return True

    # Fila i (parcial hasta columna j)
    suma_fila:int = 0
    for k in range(0, j+1):
        suma_fila += cuadrado[i][k]

    if suma_fila > suma_objetivo:
        return False
    if j == n - 1 and suma_fila != suma_objetivo:   # fila completa
        return False

    # Columna j (parcial hasta fila i)
    suma_col = 0
    for k in range(0, i+1):
        suma_col += cuadrado[k][j]
    
    if suma_col > suma_objetivo:
        return False
    if i == n - 1 and suma_col != suma_objetivo:    # columna completa
        return False

    # Diagonal principal (solo si (i,j) pertenece a ella)
    if i == j:
        suma_dp = 0
        for k in range(0, i+1):
            suma_dp += cuadrado[k][k]
        if suma_dp > suma_objetivo:
            return False
        if i == n - 1 and suma_dp != suma_objetivo: # diagonal completa
            return False

    # Diagonal secundaria (solo si (i,j) pertenece a ella)
    if i + j == n - 1:
        suma_ds = 0
        for k in range(0, i+1):
            suma_ds += cuadrado[k][n- 1- k]
        if suma_ds > suma_objetivo:
            return False
        if i == n - 1 and suma_ds != suma_objetivo: # diagonal completa
            return False

    return True


def magiCuadrados(i: int, j: int, n: int, suma_objetivo) -> int:
    global usados
    global cuadrado

    if i == n:          # todas las filas completas → cuadrado mágico encontrado
        return 1

    # Siguiente posición en orden fila por fila
    i_sig = i
    j_sig = j

    if j < n - 1:
        j_sig = j + 1
    else:
        i_sig = i + 1
        j_sig = 0

    cant_cuadrados_validos:int = 0
    for valor in range(1, pow(n, 2) + 1):
    
        if valor in usados:
            continue

        usados.add(valor)
        cuadrado[i][j] = valor

        # ── Punto clave ──────────────────────────────────────────────────────
        # Al colocar el último elemento de la primera fila, la suma de esa
        # fila se convierte en la suma objetivo para todo el cuadrado.
        # Antes de eso, suma_objetivo es None (sin restricción de suma aún).
        nueva_suma = suma_objetivo
        if i == 0 and j == n - 1:
            nueva_suma = sum(cuadrado[0])

        if es_valido(i, j, n, nueva_suma):
            cant_cuadrados_validos += magiCuadrados(i_sig, j_sig, n, nueva_suma)

        usados.remove(valor)
        cuadrado[i][j] = 0

    return cant_cuadrados_validos

def contarMagiCuadrados(n: int) -> int:
    global usados
    global cuadrado

    usados = set()                              # ← reinicio obligatorio
    cuadrado = [[0] * n for _ in range(n)]
    return magiCuadrados(0, 0, n, None)        # empieza sin suma conocida

# n:int = 3
# input(contarMagiCuadrados(n))

usados: set = set()
cuadrado: list[list[int]] = []

def es_valido(i: int, j: int, n: int) -> bool:
    global cuadrado

    suma_objetivo:int = n*(pow(n, 2)+1) / 2

    # Fila i (parcial hasta columna j)
    suma_fila:int = 0
    for k in range(0, j+1):
        suma_fila += cuadrado[i][k]

    if suma_fila > suma_objetivo:
        return False
    if j == n - 1 and suma_fila != suma_objetivo:   # fila completa
        return False

    # Columna j (parcial hasta fila i)
    suma_col = 0
    for k in range(0, i+1):
        suma_col += cuadrado[k][j]
    
    if suma_col > suma_objetivo:
        return False
    if i == n - 1 and suma_col != suma_objetivo:    # columna completa
        return False

    # Diagonal principal (solo si (i,j) pertenece a ella)
    if i == j:
        suma_dp = 0
        for k in range(0, i+1):
            suma_dp += cuadrado[k][k]
        if suma_dp > suma_objetivo:
            return False
        if i == n - 1 and suma_dp != suma_objetivo: # diagonal completa
            return False

    # Diagonal secundaria (solo si (i,j) pertenece a ella)
    if i + j == n - 1:
        suma_ds = 0
        for k in range(0, i+1):
            suma_ds += cuadrado[k][n- 1- k]
        if suma_ds > suma_objetivo:
            return False
        if i == n - 1 and suma_ds != suma_objetivo: # diagonal completa
            return False

    return True


def magiCuadrados(i: int, j: int, n: int) -> int:
    global usados
    global cuadrado

    if i == n:
        return 1

    # Siguiente posición en orden fila por fila
    i_sig = i
    j_sig = j

    if j < n - 1:
        j_sig = j + 1
    else:
        i_sig = i + 1
        j_sig = 0

    cant_cuadrados_validos:int = 0
    for valor in range(1, pow(n, 2) + 1):
    
        if valor in usados:
            continue

        usados.add(valor)
        cuadrado[i][j] = valor

        if es_valido(i, j, n):
            cant_cuadrados_validos += magiCuadrados(i_sig, j_sig, n)

        usados.remove(valor)
        cuadrado[i][j] = 0

    return cant_cuadrados_validos

def contarMagiCuadrados(n: int) -> int:
    global usados
    global cuadrado

    usados = set()
    cuadrado = [[0] * n for _ in range(n)]
    return magiCuadrados(0, 0, n)

# n:int = 3
# input(contarMagiCuadrados(n))

def maxiSubconjunto_posta(matriz:list[list[int]], I:set[int], inicio:int, n:int, k:int, I_mejor_actual:set[int], sum_mejor_actual:int)->tuple[set, int]:
    
    if k == 0:
        acc:int = 0
        for valor in I:
            for valor_2 in I:
                acc += matriz[valor][valor_2]
        if acc >= sum_mejor_actual:
            return I.copy(), acc
        return I_mejor_actual, sum_mejor_actual

    for valor in range(inicio, n):
        I.add(valor)
        parc_mejor, parc_sum_mejor = maxiSubconjunto_posta(matriz, I, valor+1, n, k-1, I_mejor_actual, sum_mejor_actual)
        if parc_sum_mejor > sum_mejor_actual:
            I_mejor_actual = parc_mejor.copy()
            sum_mejor_actual = parc_sum_mejor
        I.remove(valor)

    return I_mejor_actual, sum_mejor_actual

def maxiSubconjunto(matriz:list[list[int]], k:int)->set:
    conj, _ = maxiSubconjunto_posta(matriz, set(), 0, len(matriz), k, set(), 0)
    res:set = set()
    for elem in conj:
        res.add(elem+1)
    return res

matriz = [
    [0, 10, 10, 1],
    [10, 0, 5, 2],
    [10, 5, 0, 1],
    [1, 2, 1, 0]
]
k = 3
input(maxiSubconjunto(matriz, k)) 

def testear_todo(cant_test_por_ejercicio:int = 100):

    C_RESET:str = "\033[0m"
    C_ACEPTADO:str = "\033[38;2;39;245;166m"
    C_RECHAZADO:str = "\033[38;2;245;77;39m"
    
    ancho, _ = get_terminal_size()
    frase_en:str = "⏤ Testeando ⏤"
    frase_st:str = "⏤ Stats ⏤"
    frase_out:str = "⏤ Tests finalizados ⏤"
    divisor_en = "\n" + " "*((ancho- len(frase_en)) // 2) + frase_en 
    divisor_st = " "*((ancho- len(frase_st)) // 2) + frase_st
    divisor_in = "⊰" + "⏤"*(ancho-2) +"⊱"
    divisor_out = " "*((ancho-len(frase_out)) // 2) + frase_out

    def t_contarMagiCuadrados():
        for _ in range(cant_test_por_ejercicio):
            n:int = randint(1, 5)
            res_bruto:int  = contar_magiCuadrados_bruto(n)
            res_ejer:int = contarMagiCuadrados(n)

            paso:bool = res_bruto == res_ejer
            if not paso:
                return False
        return True

    tests:list[Callable] = [
        t_contarMagiCuadrados,
        ]

    print(divisor_en)
    stats_test:dict[bool, int] = {True: 0, False: 0}
    for t in tests:
        nombre_test:str = t.__name__
        nombre_test = nombre_test[2:len(nombre_test)]

        print(divisor_in)
        print(f"Probando {cant_test_por_ejercicio} tests para {nombre_test}.")
        start:float = perf_counter()
        res:bool = t()
        finish:float = perf_counter()

        stats_test[res] += 1

        print(f"Estado: {f'{C_ACEPTADO}Aceptado{C_RESET}' if res else f'{C_RECHAZADO}Rechazado{C_RESET}'}")
        print(f"Tiempo de ejecución tomado para {cant_test_por_ejercicio} tests: {finish-start: .4f} segundos.")


    print(divisor_in)
    print(divisor_st)

    cantidad_tests:int = len(tests)
    print(f"Cantidad de test {C_ACEPTADO}Aceptado{C_RESET}: {stats_test[True]}/{cantidad_tests}")
    print(f"Cantidad de test {C_RECHAZADO}Rechazado{C_RESET}: {stats_test[False]}/{cantidad_tests}")
    print(f"Porcentaje de aceptación: {(stats_test[True] * 100) / len(tests): .2f}%")
    print(divisor_in)
    print(divisor_out)

if __name__ == "__main__":
    testear_todo()