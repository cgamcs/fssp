import numpy as np
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('problem_10m_100j.csv', index_col=0)
processing_times = df.to_numpy()

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
            #Calcula el tiempo total de procesamiento de cada trabajo restante
            job_times = {job: sum(self.processing_times[job]) for job in remaining_jobs}
            # Selecciona el trabajo con menor tiempo total
            next_job = min(job_times, key=job_times.get)
            # Actualiza la secuencia y elimina el trabajo ya usado
            sequence.append(next_job)
            remaining_jobs.remove(next_job)

        return sequence

    def run(self):
        sequence = self.greedy_heuristic()
        total_makespan = self.makespan(sequence)
        print(f"\nSecuencia generada:\n{sequence}")
        print(f"\nMakespan total: {total_makespan}")

# Ejecutar
scheduler = FlowShopGreedyScheduler(processing_times)
scheduler.run()