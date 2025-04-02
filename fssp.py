import numpy as np
import pandas as pd

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv('problem_10m_100j.csv', index_col=0)

# Convertir el DataFrame a una matriz numpy
processing_times = df.to_numpy()

class FlowShopScheduler:
    def __init__(self, processing_times):
        """
        Inicializa el problema del Flow Shop Scheduling.
        :param processing_times: Matriz donde processing_times[i][j] es el tiempo de la tarea i en la máquina j.
        """
        self.processing_times = np.array(processing_times)
        self.num_jobs, self.num_machines = self.processing_times.shape
    
    def makespan(self, job_sequence):
        """
        Calcula el makespan (tiempo total) para una secuencia de tareas dada.
        :param job_sequence: Lista con el orden de las tareas.
        :return: Valor del makespan y matriz de tiempos de finalización.
        """
        completion_times = np.zeros((self.num_jobs, self.num_machines))
        for i, job in enumerate(job_sequence):
            for j in range(self.num_machines):
                if i == 0 and j == 0:
                    completion_times[i][j] = self.processing_times[job][j]
                elif i == 0:
                    completion_times[i][j] = completion_times[i][j - 1] + self.processing_times[job][j]
                elif j == 0:
                    completion_times[i][j] = completion_times[i - 1][j] + self.processing_times[job][j]
                else:
                    completion_times[i][j] = max(completion_times[i - 1][j], completion_times[i][j - 1]) + self.processing_times[job][j]
        
        return completion_times[-1][-1], completion_times
    
    def is_feasible(self, job_sequence):
        """
        Verifica si la secuencia dada es factible.
        :param job_sequence: Lista con el orden de las tareas.
        :return: True si es factible, False en caso contrario.
        """
        # Verificar que cada tarea aparezca exactamente una vez
        if len(job_sequence) != self.num_jobs or set(job_sequence) != set(range(self.num_jobs)):
            return False
            
        # Calcular los tiempos de finalización
        _, completion_times = self.makespan(job_sequence)
        
        # Verificar restricciones de precedencia en cada máquina
        for i in range(1, self.num_jobs):
            for j in range(self.num_machines):
                if completion_times[i][j] < completion_times[i - 1][j] + self.processing_times[job_sequence[i]][j]:
                    return False
        
        return True
    
    def feasible_schedule(self):
        """
        Genera una secuencia factible usando la heurística de menor tiempo de procesamiento primero (SPT).
        :return: Lista con el orden de las tareas en una secuencia factible.
        """
        job_sequence = list(np.argsort(np.sum(self.processing_times, axis=1)))
        return job_sequence
    
    def make_feasible(self, job_sequence):
        """
        Convierte una secuencia no factible en factible realizando los ajustes necesarios.
        :param job_sequence: Lista con el orden de las tareas (potencialmente no factible).
        :return: Lista con una secuencia factible de tareas.
        """
        # Verificar si la secuencia ya es factible
        if self.is_feasible(job_sequence):
            return job_sequence
        
        # Si no es factible, corregir duplicados o tareas faltantes
        corrected_sequence = list(range(self.num_jobs))
        np.random.shuffle(corrected_sequence)  # Secuencia aleatoria como base
        
        # Intentar preservar el orden de las tareas en la secuencia original si son válidas
        valid_jobs = [job for job in job_sequence if job in range(self.num_jobs)]
        unique_valid_jobs = []
        for job in valid_jobs:
            if job not in unique_valid_jobs:
                unique_valid_jobs.append(job)
        
        # Construir una secuencia factible basada en la secuencia original
        remaining_jobs = [job for job in range(self.num_jobs) if job not in unique_valid_jobs]
        feasible_sequence = unique_valid_jobs + remaining_jobs
        
        # Verificar factibilidad (restricciones de precedencia)
        _, completion_times = self.makespan(feasible_sequence)
        
        # Si aún hay problemas de factibilidad, usar la heurística SPT
        if not self.is_feasible(feasible_sequence):
            return self.feasible_schedule()
        
        return feasible_sequence
    
    def feasibility_planner(self, initial_sequences):
        """
        Planificador de factibilidad que toma una lista de secuencias iniciales 
        y devuelve sus versiones factibles junto con sus makespan.
        :param initial_sequences: Lista de secuencias iniciales a evaluar.
        :return: Lista de tuplas (secuencia_factible, makespan).
        """
        results = []
        
        for sequence in initial_sequences:
            # Hacer la secuencia factible
            feasible_seq = self.make_feasible(sequence)
            
            # Calcular el makespan
            ms, _ = self.makespan(feasible_seq)
            
            results.append((feasible_seq, ms))
        
        # Ordenar resultados por makespan (de menor a mayor)
        results.sort(key=lambda x: x[1])
        
        return results


# Ejemplo de uso del planificador de factibilidad
scheduler = FlowShopScheduler(processing_times)

# Generar automáticamente una secuencia inicial válida
initial_sequence = list(range(scheduler.num_jobs))
print(f"Secuencia inicial: {initial_sequence}")
print(f"Factible: {scheduler.is_feasible(initial_sequence)}")

# Generamos una secuencia factible
feasible_sequence = scheduler.feasible_schedule()
print(f"Secuencia factible recomendada: {feasible_sequence}")
print(f"Makespan: {scheduler.makespan(feasible_sequence)[0]}")

# Probar el planificador de factibilidad con varias secuencias
test_sequences = [
    initial_sequence,                   # Secuencia inicial
    feasible_sequence,                  # Secuencia factible recomendada
    list(reversed(initial_sequence)),   # Secuencia inversa
    # Secuencia con algunos trabajos repetidos (no factible)
    [0, 1, 1, 3, 4, 5, 6, 7, 8, 9] if scheduler.num_jobs >= 10 else [0, 1, 1, 0],
    # Secuencia aleatoria
    list(np.random.permutation(scheduler.num_jobs)) 
]

# Ejecutar el planificador de factibilidad
feasibility_results = scheduler.feasibility_planner(test_sequences)

# Mostrar resultados
print("\nResultados del planificador de factibilidad:")
for i, (sequence, makespan) in enumerate(feasibility_results):
    print(f"Opción {i+1}: Makespan = {makespan}")
    print(f"Secuencia: {sequence}")