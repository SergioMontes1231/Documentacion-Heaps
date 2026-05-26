class Paciente():
    def __init__(self, gravedad: int, id_paciente=None) -> None:
        self.id_paciente = id_paciente
        self.gravedad = gravedad

    def __str__(self) -> str:
        return f"Paciente: {self.id_paciente}\ngravedad: {self.gravedad}"


class MinHeap:
    def __init__(self):
        self.heap = []

    def padre(self, indice: int):
        return (indice - 1) // 2

    def izquierdo(self, indice: int) -> int:
        return (indice * 2) + 1

    def derecho(self, indice: int) -> int:
        return (indice * 2) + 2

    def tamanio(self) -> int:
        return len(self.heap)

    def esta_vacia(self) -> bool:
        return len(self.heap) == 0

    def comparar(self, a: Paciente, b: Paciente) -> bool:
        return a.gravedad < b.gravedad

    def cima(self):
        if self.esta_vacia():
            return None
        return self.heap[0]

    def subir(self, indice):
        while indice > 0:
            padre = self.padre(indice)
            if self.comparar(self.heap[padre], self.heap[indice]):
                break
            self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
            indice = padre

    def hundir(self, indice) -> None:
        n = self.tamanio()
        while True:
            izquierdo = self.izquierdo(indice)
            derecho = self.derecho(indice)
            menor = indice
            if izquierdo < n and self.comparar(self.heap[izquierdo], self.heap[menor]):
                menor = izquierdo
            if derecho < n and self.comparar(self.heap[derecho], self.heap[menor]):
                menor = derecho
            if menor == indice:
                break
            self.heap[menor], self.heap[indice] = self.heap[indice], self.heap[menor]
            indice = menor

    def insertar(self, paciente: Paciente) -> None:
        self.heap.append(paciente)
        self.subir(len(self.heap) - 1)

    def extraer_cima(self):
        if self.esta_vacia():
            return None
        cima = self.cima()
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if not self.esta_vacia():
            self.hundir(0)
        return cima

    def mostrar_heap(self):
        if self.esta_vacia():
            print("Heap vacio")
            return
        print("Estado del heap (gravedades):", [p.gravedad for p in self.heap])
        for paciente in self.heap:
            print(paciente)
            print("-" * 30)


class SistemaUrgencias():
    def __init__(self):
        self.heap_emergencias = MinHeap()
        self.ultimos_atendidos = []
        self.cola = 1

    def pedir_gravedad(self, mensaje):
        while True:
            try:
                entrada = input(mensaje)
                if entrada == "":
                    print("No puede estar vacio. Ingrese un numero del 1 al 10")
                    continue
                gravedad = int(entrada)
                if 1 <= gravedad <= 10:
                    return gravedad
                else:
                    print("Error: La gravedad debe ser un numero entre 1 y 10")
            except ValueError:
                print("Error: Debe ingresar un numero entero")

    def agregar_paciente(self, gravedad=None, id_paciente=None):
        if gravedad is None:
            print("=== Agregar Paciente ===")
            gravedad = self.pedir_gravedad("Cual es la gravedad del 1 al 10? ")
        
        if id_paciente is None:
            id_paciente = self.cola
            self.cola += 1
        
        nuevo_paciente = Paciente(gravedad, id_paciente)
        self.heap_emergencias.insertar(nuevo_paciente)
        print("Paciente agregado con exito")
        self.heap_emergencias.mostrar_heap()

    def atender_paciente(self):
        if self.heap_emergencias.esta_vacia():
            print("Error: No hay pacientes en espera")
            return
        
        print("=== Se atendio a: ===")
        paciente = self.heap_emergencias.extraer_cima()
        self.ultimos_atendidos.append(paciente)
        print(paciente)
        print("=" * 40)
        print("Orden de atencion hasta ahora:")
        for i, p in enumerate(self.ultimos_atendidos, 1):
            print(f"{i}. Paciente {p.id_paciente} (gravedad {p.gravedad})")

    def siguiente(self):
        if self.heap_emergencias.esta_vacia():
            print("No hay pacientes en espera")
            return
        print("=== El siguiente en ser atendido es =====")
        paciente = self.heap_emergencias.cima()
        print(paciente)
        print("=" * 40)

    def lista_espera(self):
        if self.heap_emergencias.esta_vacia():
            print("No hay nadie en espera")
            return
        print("=== Pacientes en espera ===")
        self.heap_emergencias.mostrar_heap()

    def cantidad_en_espera(self):
        cantidad = self.heap_emergencias.tamanio()
        print(f"Pacientes en espera: {cantidad}")

    def ultimos_atendidos_mostrar(self):
        if not self.ultimos_atendidos:
            print("No se ha atendido a nadie aun")
            return
        print("=== Ultimos pacientes atendidos ===")
        for i, paciente in enumerate(self.ultimos_atendidos[-5:], 1):
            print(f"{i}. {paciente}")
            print("-" * 30)

    def cargar_datos_prueba(self):
        print("=== Cargando datos de prueba ===")
        pacientes_prueba = [
            (1, 101), (3, 102), (2, 103), (5, 104), (1, 105),
            (4, 106), (2, 107), (8, 108), (3, 109), (1, 110),
            (6, 111), (2, 112), (9, 113), (4, 114), (5, 115)
        ]
        for gravedad, id_paciente in pacientes_prueba:
            self.agregar_paciente(gravedad, id_paciente)
        self.cola = 116
        print(f"Se cargaron {len(pacientes_prueba)} pacientes de prueba")

    def menu(self):
        while True:
            print("\n" + "=" * 40)
            print("SISTEMA DE URGENCIAS HOSPITALARIO")
            print("MIN-HEAP PARA TRIAGE")
            print("=" * 40)
            print("1. Agregar paciente")
            print("2. Atender paciente (extraer el mas grave)")
            print("3. Ver siguiente paciente en atender")
            print("4. Ver lista de espera completa")
            print("5. Ver cantidad de pacientes en espera")
            print("6. Ver ultimos atendidos")
            print("7. Cargar datos de prueba")
            print("8. Salir")
            print("=" * 40)
            
            opcion = input("Seleccione una opcion (1-8): ")
            
            if opcion == "1":
                self.agregar_paciente()
                input("Presione Enter para continuar...")
            elif opcion == "2":
                self.atender_paciente()
                input("Presione Enter para continuar...")
            elif opcion == "3":
                self.siguiente()
                input("Presione Enter para continuar...")
            elif opcion == "4":
                self.lista_espera()
                input("Presione Enter para continuar...")
            elif opcion == "5":
                self.cantidad_en_espera()
                input("Presione Enter para continuar...")
            elif opcion == "6":
                self.ultimos_atendidos_mostrar()
                input("Presione Enter para continuar...")
            elif opcion == "7":
                if not self.heap_emergencias.esta_vacia():
                    confirmar = input("Cargar datos de prueba borrara los actuales. Continuar? (s/n): ")
                    if confirmar.lower() != "s":
                        print("Carga cancelada")
                        input("Presione Enter para continuar...")
                        continue
                self.heap_emergencias = MinHeap()
                self.ultimos_atendidos = []
                self.cola = 1
                self.cargar_datos_prueba()
                input("Presione Enter para continuar...")
            elif opcion == "8":
                print("Saliendo del sistema...")
                break
            else:
                print("Error: Opcion no valida")
                input("Presione Enter para continuar...")


if __name__ == '__main__':
    sistema = SistemaUrgencias()
    sistema.menu()
