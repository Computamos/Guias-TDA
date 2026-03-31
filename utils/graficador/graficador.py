from typing import Any
from queue import Queue
from pathlib import Path


class Nodo:

    def __init__(self, valor: Any):
        self.valor = valor
        self.hijos: list[Nodo] = []
        self._etiqueta: str = None
        pass

    def agregar_hijo(self, valor_nuevo_nodo: Any):
        new_nodo: Nodo = Nodo(valor_nuevo_nodo)
        self.hijos.append(new_nodo)
        return new_nodo


class Graficador:

    def __init__(self, raiz: Nodo, nombre_arch_salida: str):
        self.raiz: Nodo = raiz
        self.ruta_arch_salida: Path = (
            Path(__file__).resolve().parent / nombre_arch_salida
        )
        pass

    @staticmethod
    def _formatear_nodo(valor: Any) -> str:
        """
        Analiza el tamaño y tipo del valor de un nodo y devuelve
        la sintaxis Mermaid óptima para que entre bien en el diagrama.

        ## Shapes usados:
            (( ))   círculo doble  → valores simples cortos
            ([ ])   estadio        → strings medianos / 1 palabra
            [  ]    rectángulo     → listas 1D o strings largos
            [" "]   rectángulo     → matrices (usa <br/> entre filas)

        ## Nota:
            Esta función la hice con IA.
        """

        # ── Helpers ────────────────────────────────────────────────────────────

        def es_matriz(v: Any) -> bool:
            return isinstance(v, list) and len(v) > 0 and isinstance(v[0], list)

        def es_lista_plana(v: Any) -> bool:
            return isinstance(v, list) and not es_matriz(v)

        # ── Umbrales (caracteres) ───────────────────────────────────────────────
        UMBRAL_CIRCULO = 12  # ((  ))  — muy corto
        UMBRAL_ESTADIO = 30  # ([  ])  — mediano
        # > 30 → rectángulo o rectángulo con <br/>

        # ── Caso 1: matriz (lista de listas) ───────────────────────────────────
        if es_matriz(valor):
            n_filas = len(valor)
            n_cols = len(valor[0])
            col_widths = [
                max(len(str(valor[i][j])) for i in range(n_filas))
                for j in range(n_cols)
            ]
            filas_fmt = [
                "  ".join(str(valor[i][j]).rjust(col_widths[j]) for j in range(n_cols))
                for i in range(n_filas)
            ]
            contenido = "<br/>".join(filas_fmt)
            return f'["{contenido}"]'  # rectángulo con saltos de línea

        # ── Caso 2: lista plana ────────────────────────────────────────────────
        if es_lista_plana(valor):
            contenido = str(valor)  # e.g. "[1, 2, 3]"
            if len(contenido) <= UMBRAL_ESTADIO:
                return f"([{contenido}])"  # estadio
            return f'["{contenido}"]'  # rectángulo si es muy larga

        # ── Caso 3: escalar / string ───────────────────────────────────────────
        contenido = str(valor)
        ancho = len(contenido)

        if ancho <= UMBRAL_CIRCULO:
            return f"(({contenido}))"  # círculo doble
        elif ancho <= UMBRAL_ESTADIO:
            return f"([{contenido}])"  # estadio
        else:
            return f'["{contenido}"]'  # rectángulo

    def graficar(self):

        def construir_nodos(nodo_padre: Nodo):
            nodos_construidos: list[str] = []
            for i, nodo_hijo in enumerate(nodo_padre.hijos):
                nodo_hijo._etiqueta = f"{nodo_padre._etiqueta}{i}"
                valor_nodo: str = self._formatear_nodo(nodo_hijo.valor)
                nodo: str = f"\t{nodo_hijo._etiqueta}{valor_nodo}\n"
                nodos_construidos.append(nodo)

            with open(self.ruta_arch_salida, "a", encoding="utf-8") as f:
                f.writelines(nodos_construidos)

        def enlazar_nodos(nodo_padre: Nodo):
            enlaces_hechos: list[str] = []
            for nodo_hijo in nodo_padre.hijos:
                etiqueta_padre: str = nodo_padre._etiqueta
                etiqueta_hijo: str = nodo_hijo._etiqueta
                enlace: str = f"\t{etiqueta_padre} --- {etiqueta_hijo}\n"
                enlaces_hechos.append(enlace)

            with open(self.ruta_arch_salida, "a", encoding="utf-8") as f:
                f.writelines(enlaces_hechos)

        def graficar_posta():
            cola: Queue = Queue()
            cola.put(self.raiz)
            while not cola.empty():
                nodo_actual: Nodo = cola.get()
                construir_nodos(nodo_actual)
                enlazar_nodos(nodo_actual)
                for hijo in nodo_actual.hijos:
                    cola.put(hijo)

        def inicializar_archivo():

            self.raiz._etiqueta = "N0"
            valor_nodo = self._formatear_nodo(self.raiz.valor)

            with open(self.ruta_arch_salida, "w", encoding="utf-8") as f:
                nodo: str = f"{self.raiz._etiqueta}{valor_nodo}"
                base: str = f"```mermaid\ngraph TD\n\t{nodo}\n"
                f.write(base)

        inicializar_archivo()
        graficar_posta()
        with open(self.ruta_arch_salida, "a", encoding="utf-8") as f:
            f.write("```")


def algoritmo(*args, el_argumento_que_quieres_trackear, nodo_padre: Nodo):
    nuevo_nodo: Nodo = nodo_padre.agregar_hijo(el_argumento_que_quieres_trackear)

    """
    la lógica de tu función acá
    """

    """
    Ahora ponele que llamas a la recursión con otros argumentos
    """

    algoritmo(*args, el_argumento_que_quieres_trackear, nuevo_nodo)

    """
    No interesa qué argumentos le pases a tu función, lo único que importa
    es que -efectivamente- le pases el nuevo nodo en cuestión.
    """


def main():

    raiz: Nodo = Nodo("Raíz")
    graficador: Graficador = Graficador(raiz, "mi_grafito.md")

    algoritmo("los_argumentos_iniciales", raiz)
    graficador.graficar()


if __name__ == "__main__":
    main()
