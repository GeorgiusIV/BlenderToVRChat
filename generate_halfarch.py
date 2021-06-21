import bpy
import math

v_all = list()
f_all = [(0,1,2,3)] # creates the bottom face

#Topright, Topleft, Bottomleft, Bottomright  Ytop, Zcentre, Xright

k = 6 # k is used to maintain the height when swapping from pillar to curve

# straight pillar
for i in range(k):
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
del f_all[-4:] # removes the excess four faces

# logarithm curve
for i in range(6): # to smooth the curve we need to iterate through some float inputs in log
    TR = (i+1,1,(k-1)+math.log(i+1))
    TL = (i+1,-1,(k-1)+math.log(i+1))
    BL = (-1,-1,(k-1)+math.log(i+1))
    BR = (-1,1,(k-1)+math.log(i+1))
    v_all.extend([TR,TL,BL,BR])
    c = 4*(i+k)
    F1 = (5+c,4+c,0+c,1+c)
    F2 = (6+c,5+c,1+c,2+c)
    F3 = (7+c,6+c,2+c,3+c)
    F4 = (4+c,7+c,3+c,0+c)
    f_all.extend([F1,F2,F3,F4])
del f_all[-4:] # removes the excess four faces

f_all.append([f_all[-i][1] for i in range(1,5)]) # creates the top face

verts = v_all
faces = f_all
mesh = bpy.data.meshes.new("Plane")
object = bpy.data.objects.new("Plane", mesh)

bpy.context.collection.objects.link(object)
object.location = (0,0,0)

mesh.from_pydata(verts, [], faces)

mesh.update(calc_edges=True)

    
