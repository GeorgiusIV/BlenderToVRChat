import bpy 


def generate_pyramids():
    
    for i in range(5):

        verts = [(1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0),(0,0,1)]
        faces = [(0,1,2,3),(0,4,1),(1,4,2),(2,4,3),(3,4,0)]

        mesh = bpy.data.meshes.new("Plane")
        object = bpy.data.objects.new("Plane", mesh)

        bpy.context.collection.objects.link(object)

        #makes copy
        object.location = (0,1,i)

        mesh.from_pydata(verts, [], faces)

        mesh.update(calc_edges=True)


generate_pyramids()
