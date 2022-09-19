import sys
sys.path.append('../src/')
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from instance import *
from local_search import *
from initial_solution import *
from data_manipulation import *
from random import randint


def runHeuristic():
    print("Iniciando heuristica")
    
    df = []
    for i in range(0, 46):
        instanceName = "instance_{instance_number:n}.csv".format(instance_number = i)
        instance = load_instance(path="../data/", file_name=instanceName)
        print("Buscando solução para instancia " + str(i))

        instance = instance.to_numpy()

        distance_matrix = generate_distance_matrix(instance)
        g_t = calculate_g_of_t(instance, distance_matrix)
        lrc = generate_lrc(g_t, 0.4, instance)

        for j in range(1, 4):
            initial_solution, end_time_initial_c = greedy_initial_construction(instance, lrc, 10)

            z, result, end_time_local_s = teitz_and_bart(initial_solution, instance, distance_matrix)
            total_time = end_time_initial_c + end_time_local_s

            data = {
                'instance': i,
                'execution': j,
                'initial_construction_time': end_time_initial_c,
                'local_search_time': end_time_local_s,
                'total_time': total_time,
                'z_value': z
            }

            df.append(data)

    pd.DataFrame.from_dict(df, orient='columns').to_csv('../result/result6.csv')

    print("Result csv gerado com sucesso")


def main():
    return True

if __name__ == "__main__":
    runHeuristic()