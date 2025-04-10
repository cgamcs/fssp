# Flow Shop Greedy Scheduler

Este proyecto implementa una heurística greedy (codiciosa) para resolver el problema de programación de trabajos en un sistema Flow Shop. La heurística selecciona en cada paso el trabajo con el menor tiempo total de procesamiento.

El objetivo es minimizar el **makespan**, es decir, el tiempo total necesario para completar todos los trabajos en todas las máquinas.

---

## 📥 Entrada

El programa lee un archivo de texto con 15 instancias del problema, cada una con un número diferente de trabajos y máquinas. Las instancias provienen de diferentes fuentes (Carlier, Heller, Reeves).

---

## ⚙️ Algoritmo Greedy

En cada iteración, el algoritmo selecciona el trabajo con la menor suma total de tiempos de procesamiento en todas las máquinas y lo agrega a la secuencia.

---

## 📊 Resultados

A continuación se muestran los resultados del algoritmo greedy aplicado a cada una de las 15 instancias:

| Instancia | Secuencia de trabajos                            | Makespan |
|-----------|--------------------------------------------------|----------|
| 1         | [0, 7, 3, 5, 8, 2, 1, 9, 4, 6, 10]                | 8848.0   |
| 2         | [6, 2, 12, 0, 5, 4, 10, 9, 3, 8, 1, 7, 11]        | 9166.0   |
| 3         | [0, 10, 11, 6, 5, 7, 9, 3, 1, 8, 4, 2]            | 9298.0   |
| 4         | [10, 11, 2, 7, 3, 6, 8, 4, 5, 1, 12, 13, 9, 0]    | 10684.0  |
| 5         | [4, 2, 3, 0, 1, 6, 5, 7, 8, 9]                    | 9265.0   |
| 6         | [7, 3, 0, 1, 4, 6, 5, 2]                          | 9815.0   |
| 7         | [3, 1, 4, 0, 6, 2, 5]                             | 7992.0   |
| 8         | [3, 1, 5, 7, 0, 4, 2, 6]                          | 10037.0  |
| 9         | [12, 36, 55, ..., 60, 38]                         | 590.0    |
| 10        | [12, 17, 11, 0, ..., 6, 18, 7]                    | 165.0    |
| 11        | [18, 5, 8, ..., 14, 3, 12]                        | 1703.0   |
| 12        | [5, 19, 1, ..., 2, 15, 9]                         | 1343.0   |
| 13        | [15, 13, 18, ..., 2, 19]                          | 1693.0   |
| 14        | [13, 9, 19, ..., 7, 4, 14]                        | 2024.0   |
| 15        | [3, 2, 14, ..., 6, 7, 4]                          | 1823.0   |

**Nota:** Para instancias con muchos trabajos, se muestra solo una parte de la secuencia con puntos suspensivos (`...`).

---

## ✅ Conclusión

Este enfoque greedy es simple y rápido, y proporciona soluciones aceptables en la mayoría de los casos. Sin embargo, **no garantiza la mejor solución posible**. Se recomienda usarlo como punto de partida o compararlo con algoritmos más avanzados como NEH, branch-and-bound, o metaheurísticas.

---

## 🚀 Ejecutar el código

Solo asegúrate de tener instalado Python 3 y NumPy. Luego ejecuta el script:

```bash
python scheduler.py
