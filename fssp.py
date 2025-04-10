import numpy as np
import re

class FlowShopGreedyScheduler:
    def __init__(self, processing_times):
        self.processing_times = np.array(processing_times)
        self.num_jobs, self.num_machines = self.processing_times.shape

    def makespan(self, job_sequence):
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
        return completion_times[-1][-1]

    def greedy_heuristic(self):
        remaining_jobs = set(range(self.num_jobs))
        sequence = []
        while remaining_jobs:
            job_times = {job: sum(self.processing_times[job]) for job in remaining_jobs}
            next_job = min(job_times, key=job_times.get)
            sequence.append(next_job)
            remaining_jobs.remove(next_job)
        return sequence

    def run(self):
        sequence = self.greedy_heuristic()
        total_makespan = self.makespan(sequence)
        return sequence, total_makespan

def leer_instancias_txt(ruta_archivo):
    instancias = []
    with open(ruta_archivo, 'r') as f:
        lineas = f.readlines()

    i = 0
    while i < len(lineas):
        linea = lineas[i].strip()
        if re.match(r'^\d+\s+\d+$', linea):  # Línea con "n_jobs n_machines"
            num_jobs, num_machines = map(int, linea.split())
            i += 1
            matriz = []
            for _ in range(num_jobs):
                while i < len(lineas) and not re.search(r'\d', lineas[i]):
                    i += 1  # Saltar líneas vacías o decorativas
                partes = list(map(int, lineas[i].strip().split()))
                tiempos = [partes[j] for j in range(1, len(partes), 2)]
                matriz.append(tiempos)
                i += 1
            instancias.append(np.array(matriz))
        else:
            i += 1
    return instancias

# Leer y ejecutar
ruta = '15 instancias.txt'
instancias = leer_instancias_txt(ruta)

for idx, tiempos in enumerate(instancias):
    print(f"\n--- Instancia {idx + 1} ---")
    scheduler = FlowShopGreedyScheduler(tiempos)
    secuencia, makespan = scheduler.run()
    print(f"Secuencia: {secuencia}")
    print(f"Makespan: {makespan}")