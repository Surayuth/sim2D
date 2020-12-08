import numpy as np


def gen_point(layer, n):
    length = layer.length
    lv = layer.lv
    bv = layer.bv
    pl = []
    pb = []
    for i in range(-n, n+1, 1):
        for j in range(-n, n+1, 1):
            l = i*length*lv[0] + j*length*lv[1]
            pl.append(l)
            for b in bv:
                pb.append(l + b*length)
    pl = np.array(pl)
    pb = np.array(pb)
    points = [pl, pb]
    return points


def shift(points, v):
    v = np.array(v)
    pl, pb = points
    pl = pl + v
    pb = pb + v
    points = [pl, pb]
    return points


def rotate(points, rad):
    rot = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
    pl, pb = points
    pl = np.matmul(pl, rot.transpose())
    pb = np.matmul(pb, rot.transpose())
    points = [pl, pb]
    return points
