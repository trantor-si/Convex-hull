#! /usr/bin/python

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import hull

fig = plt.figure() # For plotting
ax = fig.add_subplot(111, projection='3d')

for point in hull.final_vertices:
	ax.scatter(point.x, point.y, point.z, c='b', marker='o')

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

ax.set_xlabel('Cortante (kN)')
ax.set_ylabel('Momento (kN.m)')
ax.set_zlabel('Tração (kN)')

plt.savefig('image-new.jpg', bbox_inches='tight')
plt.show()
