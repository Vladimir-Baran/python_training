from geom2d.point import *


l = list(map(lambda i: Point(i, i*i), range(-5,6)))

l2 = list(filter(lambda p: p.y % 2 == 0, l))


print(l)
print(l2)