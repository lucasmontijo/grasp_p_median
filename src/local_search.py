from math import sqrt


def calculate_distance(point_a_x: int, point_a_y: int, point_b_x: int, point_b_y: int):
    square_x = (point_a_x - point_b_x) ^ 2
    square_y = (point_a_y - point_b_y) ^ 2
    return sqrt(square_x + square_y)


def teitz_bart(instance, selected_points):
    return


def get_difference(array_a, array_b):
    return array_a - array_b