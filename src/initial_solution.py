import pandas as pd
import numpy as np
import random as rd


def get_initial_solution(instance: list, medians: int):
    if medians <= 0 or medians > len(instance):
        print("Erro no tamanho de medianas")
        return None
    else:
        return np.array(rd.choices(instance, k=medians))

