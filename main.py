from utils.base import Structure, Layer
import numpy as np
from utils.function import gen_point, shift, rotate


layer = Layer(1, [[np.sqrt(3)/2, -1/2], [np.sqrt(3)/2, 1/2]], [[1/np.sqrt(3), 0]])
s = Structure()
s.add([layer])
s.summary()

#s.summary()
#points = gen_point(s, 2)
#points = shift(points, [0, 0])
#points = rotate(points, np.pi/6)




