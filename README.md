# README - Sistema de Urgencias Hospitalarias con Min-Heap

## Descripcion General

El Sistema de Urgencias Hospitalarias es una aplicación desarrollada en Python que simula la gestión de pacientes en una sala de emergencias utilizando una estructura de datos Min-Heap.

El objetivo principal es organizar la atención médica según la gravedad de cada paciente, donde un valor menor representa una mayor prioridad de atención.

---
## Contenido
- [Descripcion General](#Descripcion-General)
- [Funcionamiento del sistema](#Funcionamiento-del-sistema)
    - [Características principales](#Características-principales)
- [Requisitos e instalación](#Requisitos-e-instalación)
    - [Requisitos](#Requisitos)
    - [Ejecución](#Ejecución)
- [Menú principal](#Menú-principal)
- [Opciones del sistema](#Opciones-del-sistema)
- [Estructura del código](#Estructura-del-código)
- [Funcionamiento del Min Heap](#Funcionamiento-el-Min-Heap)
- [Ejemplo de uso](#Ejemplo-de-uso)
    - [Agregar paciente](#Agregar-paciente)
    - [Atender paciente](#Atender-paciente)
- [Datos de prueba](#Datos-de-prueba)
- [Personalización](#Personalización)
    - [Cambiar rango de gravedad](#Cambiar-rango-de-gravedad)
    - [Cambiar historial mostrado](#Cambiar-historial-mostrado)
- [Posibles errores](#Posibles-errores)
- [Complejidad algorítmica](#Complejidad-algorítmica)
- [Autor](#Autor)
- [Referencias](#Referencias)
---
## Funcionamiento del sistema

El sistema utiliza un Min-Heap para mantener al paciente con mayor prioridad en la parte superior de la estructura. Esto permite que el paciente más grave sea atendido primero.

### Características principales

| Característica | Descripción |
|---|---|
| Prioridad | Menor número = Mayor gravedad |
| Estructura | Min-Heap implementado desde cero |
| Capacidad | Limitada únicamente por la memoria disponible |
| Persistencia | Datos almacenados durante la ejecución |

---

## Requisitos e instalación

### Requisitos

- Python 3.6 o superior
- No requiere librerías externas

### Ejecución

```bash
python act1.py
```

---

## Menú principal

```text
========================================
SISTEMA DE URGENCIAS HOSPITALARIO
MIN-HEAP PARA TRIAGE
========================================
1. Agregar paciente
2. Atender paciente
3. Ver siguiente paciente
4. Ver lista de espera
5. Ver cantidad de pacientes
6. Ver ultimos atendidos
7. Cargar datos de prueba
8. Salir
========================================
```

---

## Opciones del sistema

| Opción | Función |
|---|---|
| 1 | Agregar un paciente |
| 2 | Atender al paciente más grave |
| 3 | Mostrar el siguiente paciente |
| 4 | Ver la lista de espera |
| 5 | Mostrar cantidad de pacientes |
| 6 | Ver historial de pacientes atendidos |
| 7 | Cargar datos de prueba |
| 8 | Finalizar el programa |

---

## Estructura del código

El programa está organizado mediante clases principales:

```python
class Paciente:
    Representa a un paciente con ID y gravedad

class MinHeap:
    Implementación de la estructura Min-Heap

class SistemaUrgencias:
    Control principal del sistema
```

---

## Funcionamiento del Min Heap

```text
          [1]
         /   \
       [2]   [3]
      /  \   /
    [5] [4] [6]
```

Los pacientes con menor gravedad numérica tienen mayor prioridad.

---

## Ejemplo de uso

### Agregar paciente

```python
=== Agregar Paciente ===
Cual es la gravedad del 1 al 10? 2

Paciente agregado con exito
Estado del heap: [2]
```

### Atender paciente

```python
=== Se atendio a: ===
Paciente: 1
gravedad: 2
```

---

## Datos de prueba

La opción 7 carga automáticamente pacientes con distintas prioridades.

| ID | Gravedad |
|---|---|
| 101 | 1 |
| 102 | 3 |
| 103 | 2 |
| 104 | 5 |
| 105 | 1 |

---

## Personalización

### Cambiar rango de gravedad

```python
if 1 <= gravedad <= 10:
```

Modificar el valor máximo según sea necesario.

### Cambiar historial mostrado

```python
self.ultimos_atendidos[-5:]
```

Cambiar el número 5 por la cantidad deseada.

---

## Posibles errores

| Error | Causa | Solución |
|---|---|---|
| ValueError | Entrada no numérica | Ingresar valores numéricos |
| Heap vacío | No hay pacientes | Agregar pacientes primero |
| IDs repetidos | Datos duplicados | Reiniciar el sistema |

---

## Complejidad algorítmica

| Operación | Complejidad |
|---|---|
| Insertar | O(log n) |
| Extraer | O(log n) |
| Ver cima | O(1) |
| Mostrar heap | O(n) |

---

## Autor
Montes Olivares Sergio

Práctica realizada para la materia de Estructuras de Datos, utilizando una implementación de Min-Heap aplicada a un sistema de triaje hospitalario.

---

## Referencias

- Documentación oficial de Python: https://www.python.org/doc/
- Heap Queue Algorithm - Python Docs: https://docs.python.org/3/library/heapq.html
