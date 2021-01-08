import numpy as np


def entropy(p):
    ent = 0
    for p_i in p:
        if p_i == 0:
            continue
        ent -= p_i * np.log2(p_i)
    return ent


def gini(p):
    g = 1
    for p_i in p:
        g -= p_i * p_i
    return g
