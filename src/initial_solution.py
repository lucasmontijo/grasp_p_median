import pandas as pd
import numpy as np
import random as rd
from math import sqrt
import time

def calculate_distance(point_a, point_b):
    x = (point_a[1] - point_b[1])
    y = (point_a[2] - point_b[2])^2
    square_x = pow(x, 2)
    square_y = pow(y, 2)
    
    return sqrt(square_x + square_y)

def generate_distance_matrix(instance):
    distance_matrix = {}
    for point_a in instance:
        for point_b in instance:
            if (instance.item(point_a[0]) != instance.item(point_b[0])):
                distance_matrix[(point_a[0], point_b[0])] = calculate_distance(point_a, point_b)
            else:
                distance_matrix[(point_a[0], point_b[0])] = 0.0
    return distance_matrix

def calculate_g_of_t(instance, distance_matrix):
    g_table = []
    for i in range(0, instance.shape[0]):
        g_table.append(0)
        for j in range(0, instance.shape[1]):
            g_table[i] = g_table[i] + (distance_matrix[(j, i)])
    return g_table

def generate_lrc(g_table, alpha, instance):
    arg_max = max(g_table)
    arg_min = min(g_table)
    lrc = []
    for i in range(0, instance.shape[0]):
        if (g_table[i] <= arg_min + alpha *(arg_max - arg_min)):
            lrc.append(i)
    return lrc

def greedy_initial_construction(instance, lrc, p):
    start_time = time.perf_counter()
    medians_pos = []
    medians = np.zeros((p, 3), dtype=int)
    if p <= 0 or p > len(instance):
        print("Erro no tamanho de medianas")
        return None

    while len(medians_pos) < p:
        candidate = rd.randint(0, instance.shape[0])
        if((candidate in lrc) and (candidate not in medians_pos)):
            medians_pos.append(candidate)
    for i in range(0, len(medians_pos)):
        medians[i][0], medians[i][1], medians[i][2] = instance.item(medians_pos[i], 0), instance.item(medians_pos[i], 1), instance.item(medians_pos[i], 2)
    end_time = time.perf_counter()
    print("Tempo levado para construcao inicial: " + str(round(end_time - start_time, 2)) + "s")
    return medians

