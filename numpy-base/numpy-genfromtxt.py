import numpy

world_txt = numpy.genfromtxt('world.txt', delimiter=',', dtype=str)

print(type(world_txt))
print(world_txt)

print(world_txt[0, 0], world_txt[1, 0])

