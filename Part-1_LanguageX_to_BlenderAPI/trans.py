f = open("code.x")
wr = open("output.py", "w")
wr.write("import bpy\nfrom random import randint\n\n")

skin = ""

i = 0
for x in f:

	if x == "\n":
		continue
	i+=1
	
	determine = x.split(':')[0]
	determine = determine.split(' ')[0]
	determine = determine.split('\n')[0]

	#Case: 1 If detecting an entity
	if determine == "<entity>":
		print("Entity detected")
		wr.write("#Object Definition\n")
	if determine == "$skin":
		print("skin detected")
		a = x.split(':')[1].split(';')[0][1:-1]
		wr.write("bpy.ops.mesh.primitive_" + a + "_add(location=(0,0,0))\n")
		if a == "cube":
			skin = "Cube"
		if a == "cone":
			skin = "Cone"
		if a == "uv_sphere":
			skin = "Sphere"
	if determine == "$scale":
		print("scale detected")
		a = x.split(':')[1].split(';')[0].split(' ')[0].split(',')
		print(a)
		wr.write("bpy.context.object.scale[0] = "+a[0]+"\n")
		wr.write("bpy.context.object.scale[1] = "+a[1]+"\n")
		wr.write("bpy.context.object.scale[2] = "+a[2]+"\n")
	if determine == "$init":
		print("Intitial Position detected")
		a = x.split(':')[1].split(';')[0].split(' ')[0].split(',')
		print(a)
		wr.write("bpy.ops.transform.translate(value=("+a[0]+","+a[1]+","+a[2]+"))\n")
	if determine == "$rotate":
		print("Intitial Rotation detected")
		a = x.split(':')[1].split(';')[0].split(' ')[0].split(',')
		print(a)
		wr.write("bpy.ops.transform.trackball(value=("+a[0]+","+a[1]+"))\n")
	if determine == "</entity>":
		print("Entity Ended")
		wr.write("#Object Definition Complete\n\n")
	if determine == "@move":
		print("Move Function detected")
		a = x.split(':')[1].split(',')
		print(a)
		ini_key = a[0]
		fin_key = a[1]
		b = x.split(':')[2].split(";")[0].split(',')
		print(b)
		wr.write("bpy.data.objects['"+skin+"'].keyframe_insert(data_path='location', frame="+str(ini_key)+")\nbpy.ops.transform.translate(value=("+b[0]+","+b[1]+","+b[2]+"))\nbpy.data.objects['"+skin+"'].keyframe_insert(data_path='location', frame="+str(fin_key)+")")



	print(str(i)+" "+determine)

	
f.close()
wr.close()