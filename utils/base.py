import numpy as np


class Structure:
    def __init__(self):
        self.layer = []

    def __getitem__(self, i):
        return self.layer[i]

    def add(self, layer):
        assert isinstance(layer, list)
        for i in layer:
            self.layer.append(i)

    def summary(self):
        print('--------------------------------------')
        for i, l in enumerate(self.layer):
            print('layer: {}'.format(i+1))
            l.summary()

    def gen_band(self):
        pass


class Layer:
    def __init__(self, length, lv, bv):
        self.length = length
        self.lv = np.array(lv)
        self.bv = np.array(bv)
        self.l = ''
        self.b = ''

    def describe(self, dict_atom):
        self.l = dict_atom['lattice']
        self.b = dict_atom['basis']

    def tunneling(self, tun_ll, tun_lb, tun_bb):
        pass

    def summary(self):
        print('--------------------------------------')
        print('length: {}'.format(self.length))
        if len(self.l) > 0:
            print('atom lattice')
        print('lattice: {0}'.format(self.lv.tolist()))
        print('basis: {}'.format(self.bv.tolist()))
        print('--------------------------------------')