# La función de recurrencia

$T(n) = a*T(n/c) + f(n)$

# Ejercicio 2: Búsqueda binaria

```plaintext

objetivo = 2

arr = [1, 3, 3, 4, 5 , 10]

izq = 2
der = 1

medio = 1

```

1. 
```python
def busqueda_binaria(arr, objetivo, izq=0, der=len(arr)-1):
    
    # Conquistar
    if izq > der:
        return False  # Elemento no encontrado

    # Divide 
    medio = (izq + der) // 2
    
    # Conquistar
    if arr[medio] == objetivo:
        return medio
    
    # Combine
    elif arr[medio] > objetivo:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)
    else:
        return busqueda_binaria(arr, objetivo, medio + 1, der)
```

2. El problema se divide en un solo subproblema.

3. El tamaño de los subproblemas es $n/2$

4. El costo de combinar los resultados de los subproblemas es $O(1)$

5. $T(n) = 1*T(n/2) + O(1)$

6. Recordemos al teorema maestro:

## Teorema maestro (tu mantra de D&C):

* Permite resolver relaciones de recurrencia de la forma:
$$T(n) = \begin{cases} a \, T(n/c) + f(n) & \text{si } n > 1 \\ 1 & \text{si } n = 1 \end{cases}$$

* Si $f(n) = O(n^{((\log_c a) - \epsilon)})$ para $\epsilon > 0$, entonces $T(n) = \Theta(n^{\log_c a})$
* Si $f(n) = \Theta(n^{\log_c a})$, entonces $T(n) = \Theta(n^{\log_c a} \log n)$
* Si $f(n) = \Theta(n^{\log_c a} \log^k n)$ para algún $k \geq 0$, entonces $T(n) = \Theta(n^{\log_c a} \log^{k+1} n)$ (generalización del caso anterior)
* Si $f(n) = \Omega(n^{((\log_c a) + \epsilon)})$ para $\epsilon > 0$ y $a f(n/c) < k f(n)$ para $k < 1$ y $n$ suficientemente grandes, entonces $T(n) = \Theta(f(n))$

---

Calculamos $n^{\log_{c}{(a)}} = n^{\log_{2}{(1)}} = n^{0} = 1$

Como $O(f(n))= O(1)$ entonces hacemos match con el segundo caso del teorema maestro, y por lo tanto la complejidad es $O(n^{\log_{c}{a}}*\log{(n)}) = O(\log{(n)})$

---
---

# Observación

Para el argumento de nuestra función recursiva podemos -en principio- tener dos casos:

- El tamaño de la entrada se divide -> lo que queremos. 
    - Un ejemplito de esto es el ejercicio 2.
- Al tamaño de la entrada se le resta algo -> no queremos eso. Un ejemplito de esto es búsqueda lineal pero recurisiva.
 
    ```python
    def busquedaLineal(array:list[int], objetivo:int, indice:int)->int | bool:
        
        if indice < 0:
            return False

        if array[indice] == objetivo:
            return indice
        
        return busquedaLineal(array, objetivo, indice-1)
    ```

    $T(n) = 1*T(n-1)+ O(1)$


# Ejercicio 7

Vamos a hacer el 2, el 3 y el 7

### 2

$T(n) = T(n − 1) + n$

$T(n) = (T(n − 2) + (n-1)) + n$

$T(n) = ((T(n − 3) + (n-2)) +(n-1)) + n$

$T(n) = (((T(n − 4) + (n-3)) + (n-2)) + (n-1)) + n$

.

.

.

$T(n) = (((T(0) + 1 + ... + (n-3)) + (n-2)) + (n-1)) + n$

$T(n) = \sum_{k=0}^{n}{k} = \frac{n(n+1)}{2}$

$O(T(n)) = O(\frac{n(n+1)}{2}) = O(n^2)$

### 3


$T(n) = T(n − 1) + \sqrt{n}$

$T(n) = (T(n − 2) + \sqrt{n-1}) + \sqrt{n}$

$T(n) = ((T(n − 3) + \sqrt{n-2}) +\sqrt{n-1}) + \sqrt{n}$

$T(n) = (((T(n − 4) + \sqrt{n-3}) + \sqrt{n-2}) + \sqrt{n-1}) + \sqrt{n}$

.

.

.

$T(n) = (((T(0) + \sqrt{1} + ... + \sqrt{(n-3)}) + \sqrt{(n-2)}) + \sqrt{(n-1)}) + \sqrt{n}$

$T(n) = \sum_{k=0}^{n}{\sqrt{k}} \approx \int_{k=0}^{n}{\sqrt{k}} \ dx = |_{0}^k \ \frac{2}{3} * k^{\frac{3}{2}} \approx \frac{2}{3} * n^{\frac{3}{2}}$

$O(T(n)) \approx O(\frac{2}{3} * n^{\frac{3}{2}}) = O(n^{\frac{3}{2}})$

### 7


$T(n) = T(\frac{n}{2}) + \sqrt{n}$

Identificamos: $a=1$, $c=2$, $f(n)=\sqrt{n}$

Calculamos: $\alpha = \log_{c}{a} = \log_{2}{1} = 0$, luego queremos calcular $n^\alpha = 1$

> Vemos que el último caso hace match: Si $f(n) = \Omega(n^{((\log_c a) + \epsilon)})$ para $\epsilon > 0$ y $a f(n/c) < k f(n)$ para $k < 1$ y $n$ suficientemente grandes, entonces $T(n) = \Theta(f(n))$

Calculamos: $a*f(n/c)= 1*\sqrt{\frac{n}{c}}$ Luego queremos ver que:

$\sqrt{\frac{n}{2}} \lt \frac{1}{2} *\sqrt{n}$

$\sqrt{\frac{n}{2}} \lt \frac{\sqrt{n}}{2}$

$k=\frac{1}{\sqrt{\frac{3}{2}}}$

$\sqrt{\frac{n}{2}} \lt \frac{1}{\sqrt{\frac{3}{2}}} *\sqrt{n}$


$\sqrt{\frac{n}{2}} \lt \sqrt{\frac{2*n}{3}}$

$\frac{n}{2} \gt \frac{2*n}{3}$

$3\frac{n}{4} \lt n$

$3\frac{1}{4} \lt 1$

Entonces por el último caso del teorema maestro tenemos que nuestra $T$ tiene complejidad $\theta{(\sqrt{n})}$

---
---

# Ejercicio 12

# Ejemplito visual

```
n = 4
i_0 = 0
i_1 = 1
j_0 = 0
j_1 = 1

[
    [True,  True,   True, True],
    [False, True,   True, True ],

    [False, False,  True, False],
    [False, False,  True, True ],
]
```

### 1

```python
def cazadorDeFalsos(i_0:int, i_1:int, j_0:int, j_1:int, matriz:list[list[int]])->tuple[int, int]

    # Conquer
    if i_1 - i_0 == 1 and j_1 - j_0 == 1:
        if matriz[i_0][j_0] == False:
            return (i_0, j_0)
        else:
            return None

    # Divide
    mitad_filas:int = (i_1 + i_0) // 2    
    mitad_colum:int = (j_1 + j_0) // 2    

    mitades:list[tuple[int, int, int, int]] = (
        (i_0, mitad_filas, j_0, mitad_columnas),
        (i_0, mitad_filas, mitad_columnas, j_1),
        (mitad_filas, i_1, j_0, mitad_columnas),
        (mitad_filas, i_1, mitad_columnas, j_1),
    )

    # Combine
    for coord_submatriz in mitades:
        i, i_, j, j_ = coord_submatriz
        if conjuncionSubmatriz(i, i_, j, j_) == False:
            return cazadorDeFalsos(i, i_, j, j_, matriz)
```

$a=1$, $c=2$, $f(n) = O(1)$

$T(n^2) = 1*T(\frac{n^2}{4}) + O(1)$

Si bajamos la potencia...

$T(n) = 1*T(\frac{n}{2}) + O(1)$

Calculamos: $\alpha = \log_{c}{a} = \log_{2}{1} = 0$, luego queremos calcular $n^\alpha = 1$

Por el segundo caso del teorema maestro tenemos que la complejidad temporal es $O(\log{(n)})$

### 2

```python
def cazadorDeFalsosContador(i_0:int, i_1:int, j_0:int, j_1:int, matriz:list[list[int]])->tuple[int, int]

    # Conquer
    if i_1 - i_0 == 1 and j_1 - j_0 == 1:
        if matriz[i_0][j_0] == False:
            return 1
        else:
            return 0

    # Divide
    mitad_filas:int = (i_1 + i_0) // 2    
    mitad_colum:int = (j_1 + j_0) // 2    

    mitades:list[tuple[int, int, int, int]] = (
        (i_0, mitad_filas, j_0, mitad_columnas),
        (i_0, mitad_filas, mitad_columnas, j_1),
        (mitad_filas, i_1, j_0, mitad_columnas),
        (mitad_filas, i_1, mitad_columnas, j_1),
    )

    # Combine
    contador:int = 0
    for coord_submatriz in mitades:
        i, i_, j, j_ = coord_submatriz
        if conjuncionSubmatriz(i, i_, j, j_) == False:
            contador += cazadorDeFalsos(i, i_, j, j_, matriz)

    return contador
```

Identificamos: $a=4$, $c=2$, $f(n)= O(1)$

$T(n^2) = 4*T(\frac{n^2}{4}) + O(1)$

$T(n) = 4*T(\frac{n}{2}) + O(1)$

Sabemos que a lo sumo tenemos 5 false en la matriz, luego en el peor caso sabemos que vamos a tener un false en cada submatriz. Entonces sabemos que al evaluar cada submatriz podemos llegar a lo sumo a 2 false en esa submatriz, luego realizar la búsqueda de false dentro de esa submatriz es logarítmica pues estamos aplicando un algoritmo con las mismas complejidades del algoritmo del inciso 1, luego tendríamos que ver cada submatriz de la instancia inicial es $O(\log{(n)})$, finalmente estaríamos evaluando 5 instancias de la instancia inicial del algoritmo, formalmente:

$T(n) = 5 *O(\log{(n)})$

$O(T(n)) = O(5 *O(\log{(n)}))$

$O(T(n)) = O(\log{(n)})$