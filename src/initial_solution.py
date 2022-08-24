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

def calculate_distance(point_a_x: int, point_a_y: int, point_b_x: int, point_b_y: int):
    square_x = (point_a_x - point_b_x) ^ 2
    square_y = (point_a_y - point_b_y) ^ 2 
    return sqrt(square_x + square_y)


def distance_matrix_generator(instance):
    distance_matrix = {}
    for point_a in instance:
        for point_b in instance:
            if (point_a[0] != point_b[0]) or (point_a[1] != point_b[1]):
                distance_matrix[(instance.index(point_a), instance.index(point_b))] = calculate_distance(point_a[0], point_a[1], point_b[0], point_b[1])
            else:
                distance_matrix[(instance.index(point_a), instance.index(point_b))] = 0.0
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