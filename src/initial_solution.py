import pandas as pd
import numpy as np
import random as rd
from math import sqrt


def get_initial_solution(instance: list, medians: int):
    if medians <= 0 or medians > len(instance):
        print("Erro no tamanho de medianas")
        return None
    else:
        return np.array(rd.choices(instance, k=medians))

def calculate_distance(point_a, point_b):
    x = (point_a[1] - point_b[1])
    y = (point_a[2] - point_b[2])^2
    square_x = pow(x, 2)
    square_y = pow(y, 2)
    
    return sqrt(square_x + square_y)
    

def generate_distance_matrix(instance):
    distance_matrix = {}
    sum = 0
    for point_a in instance:
        for point_b in instance:
            if (instance.item(point_a[0]) != instance.item(point_b[0])):
                distance_matrix[(point_a[0], point_b[0])] = calculate_distance(point_a, point_b)
            else:
                sum = sum + 1
                distance_matrix[(point_a[0], point_b[0])] = 0.0
    print(sum)
    return distance_matrix

def fun_obj(instance, distance_matrix, medians):
    min_distances = []
    for point in instance:
        distances = []
        if not(point in medians):
            for j in medians:
                distances.append(distance_matrix[point, j])
            min_distances.append(min(distances))
    res = sum(min_distances)
    return res

def teitz_and_bart(medians: list, instance: list, distance_matrix):

    z = fun_obj(instance, distance_matrix, medians)

    #print("Solucao inicial - Z: " + str(z) + "P-Medianas: " + str(medians))

    rejected_medians = []
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
                    temp = medians.copy()
                    temp[temp.index(element)] = j
                    actual_z = fun_obj(instance, distance_matrix, temp)
                    savings[(element, j)] = z - actual_z
                    if savings[(element, j)] < 0:
                        cont_negative = cont_negative + 1
                        cont = cont + 1
                    else:
                        if savings[(element, j)] > max_val:
                            max_val = savings[(element, j)]
                            best_z = actual_z
                            best_medians = temp.copy()
                if cont == p:
                    rejected_medians.append(j)

        if cont_negative != len(savings):
            medians = best_medians.copy()
            z = best_z
            #print("Solucao " + str(k) + " Z Z: " + str(z) + " P-Medianas: " + str(medians))
            k = k + 1
        else:
            #print("Melhor solucao encontrada" + str(k-1) + " => Z: " + str(z) + " P-Medianas: " + str(medians))
            end = True
    return z, medians