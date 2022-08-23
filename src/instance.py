import pandas as pd
import numpy as np
from random import randint


def create_instance(num_points: int, min: int, max: int):
    final = []
    for step in range(num_points):
        verif = False
        while verif == False:
            element = [randint(min, max), randint(min, max)]
            if element not in final:
                final.append(element)
                verif = True
    return np.array(final)


def save_instance(instance, path: str, file_name: str):
    instance.to_csv(path + file_name, sep="\t", index=False)


def load_instance(path: str, file_name: str):
    return pd.read_csv(path + file_name, sep="\t")
