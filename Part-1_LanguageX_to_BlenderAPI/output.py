import bpy
from random import randint

#Object Definition
loc = r'D:\blender\models\FinalBaseMesh.obj'
imported_object = bpy.ops.import_scene.obj(filepath=loc)
obj_object = bpy.context.selected_objects[0]
bpy.ops.transform.translate(value=(-22,544,0))
bpy.ops.transform.trackball(value=(0,0))
bpy.data.objects[obj_object.name].keyframe_insert(data_path='location', frame=0)
bpy.ops.transform.translate(value=(-22,-545,1))
bpy.data.objects[obj_object.name].keyframe_insert(data_path='location', frame=250)#Object Definition Complete

#Object Definition
bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
bpy.context.object.scale[0] = 1.5
bpy.context.object.scale[1] = 1.2
bpy.context.object.scale[2] = 1.3
bpy.ops.transform.translate(value=(2,-3,0))
bpy.ops.transform.trackball(value=(-0.38,1.06))
bpy.data.objects['Cube'].keyframe_insert(data_path='location', frame=0)
bpy.ops.transform.translate(value=(-30,5,1))
bpy.data.objects['Cube'].keyframe_insert(data_path='location', frame=250)#Object Definition Complete

#Object Definition
bpy.ops.mesh.primitive_cone_add(location=(0,0,0))
bpy.context.object.scale[0] = 2
bpy.context.object.scale[1] = 2
bpy.context.object.scale[2] = 2
bpy.ops.transform.translate(value=(20,0.7,0))
bpy.ops.transform.trackball(value=(0.38,-1.06))
#Object Definition Complete

#Object Definition
bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
bpy.context.object.scale[0] = 2
bpy.context.object.scale[1] = 2
bpy.context.object.scale[2] = 2
bpy.ops.transform.translate(value=(0,-20.4419,0))
bpy.data.objects['Sphere'].keyframe_insert(data_path='location', frame=0)
bpy.ops.transform.translate(value=(0,40,-5))
bpy.data.objects['Sphere'].keyframe_insert(data_path='location', frame=250)#Object Definition Complete

