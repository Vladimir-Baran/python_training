from geom2d.point import *


l1 = [Point(3,1), Point(0, 0), Point(5,2)]


lw = sorted(l1, key=lambda p: p.distance(Point(0, 0)))
print(l1)
print(lw)