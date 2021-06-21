# missing one face on the top of the cuboid, couldn't be bothered to add it

import bpy
import math

v_all = list()
f_all = [(0,1,2,3)]

#Topright, Topleft, Bottomleft, Bottomright  Ytop, Zcentre, Xright

for i in range(5):
    TR = (1,1,i)
    TL = (1,-1,i)
    BL = (-1,-1,i)
    BR = (-1,1,i)
    v_all.extend([TR,TL,BL,BR])
    c = 4*i
    F1 = (5+c,4+c,0+c,1+c)
    F2 = (6+c,5+c,1+c,2+c)
    F3 = (7+c,6+c,2+c,3+c)
    F4 = (4+c,7+c,3+c,0+c)
    f_all.extend([F1,F2,F3,F4])
del f_all[(len(f_all)-4):] #code produces 4 faces too many, so delete the last 4 faces

verts = v_all
faces = f_all

mesh = bpy.data.meshes.new("Plane")
object = bpy.data.objects.new("Plane", mesh)
bpy.context.collection.objects.link(object)
object.location = (0,0,0)
mesh.from_pydata(verts, [], faces)
mesh.update(calc_edges=True)

    
