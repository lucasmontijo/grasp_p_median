from ctypes.wintypes import tagRECT
from math import sqrt
from pickletools import TAKEN_FROM_ARGUMENT1
import numpy as np
import time

def fun_obj(instance, distance_matrix, medians):
    min_distances = []
    for point in instance:
        distances = []
        if not(point in medians):
            for j in medians:
                distances.append(distance_matrix[point[0], j[0]])
            min_distances.append(min(distances))
    res = sum(min_distances)
    return res

def teitz_and_bart(medians: list, instance: list, distance_matrix):
    start_time = time.perf_counter()
    z = fun_obj(instance, distance_matrix, medians)

    print("Solucao inicial - Z: " + str(z) + "P-Medianas: " + str(medians))

    rejected_medians = np.array([])
    k = 0
    end = False
    while not end and k < 1000:
        savings = {}
        max_val = -1
        cont_negative = 0
        for j in instance:
            if not (j in medians) and not (j in rejected_medians):
                cont = 0
                for element in medians:
                    copy_medians = medians.copy()
                    index = get_index(copy_medians, element)
                    copy_medians[index] = j
                    actual_z = fun_obj(instance, distance_matrix, copy_medians)
                    savings[(element[0], j[0])] = z - actual_z
                    if savings[(element[0], j[0])] < 0:
                        cont_negative = cont_negative + 1
                        cont = cont + 1
                    else:
                        if savings[(element[0], j[0])] > max_val:
                            max_val = savings[(element[0], j[0])]
                            best_z = actual_z
                            best_medians = copy_medians.copy()
                if cont == len(medians):
                    rejected_medians = np.append(rejected_medians, j)

        if cont_negative != len(savings):
            medians = best_medians.copy()
            z = best_z
            k = k + 1
        else:
            print("Melhor solucao encontrada" + str(k-1) + " => Z: " + str(z) + " P-Medianas: " + str(medians))
            end_time = time.perf_counter() - start_time
            print("Tempo levado para busca local: " + str(round(end_time, 2)) + "s")
            end = True
    return z, medians, (end_time)

def get_index(arr, target_element):
    for i in range(0, len(arr)):
        if (np.all(arr[i]==target_element)):
            return i
    return -1