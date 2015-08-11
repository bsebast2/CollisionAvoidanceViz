
#THIS CODE ANIMATES THE FIRST PARTICLE. I EXPORTED THE TIME DATA,
#REMODELLED THE MATRIX MANUALLY, AND THEN SAVED IT TO
#"particle1_timedat.csv".

#For every subequent particle, I ran this code after changing the variable positions to point at a new .dat file. For example I would change the file name to "../../particle201data.dat" if I wanted to animate the 201st particle. 
#(I had data stored for about 5000 particles in this way, as .dat files. There are ways to improve the efficiency of this program)
import bpy
import csv
import numpy as np

#Call data from one particle for all timeframes(received from Matlab)
positions=csv.reader(open("/home/bsebast2/Documents/Swarmflight/swarmflight/swarmflight/particle200data.dat", newline=''),delimiter=',')                                                                      

#TWO classes for assigning materials: makeMaterial and setMaterial
def makeMaterial(name, diffuse, specular, alpha):
mat = bpy.data.materials.new(name)
mat.diffuse_color = diffuse
mat.diffuse_shader = 'LAMBERT'
mat.diffuse_intensity = 1.0
mat.specular_color = specular
mat.specular_shader = 'COOKTORR'
mat.specular_intensity = 0.5
mat.alpha = alpha
mat.ambient = 1
return mat

def setMaterial(ob, mat):
me = ob.data
me.materials.append(mat)

#use the two material classes to make red and blue colors
red = makeMaterial('Red', (1,0,0), (1,1,1), 1)
blue = makeMaterial('BlueSemi', (0,0,1), (0.5,0.5,0), 0.5)

#set original source point
start_pos = (0,0,0)
#positions=list(map(int,positions))
#positions=[int(i) for i in positions]
#positions1=np.array(positions)

#create a sphere to represent nano-satellite
bpy.ops.mesh.primitive_uv_sphere_add(segments=32, size=0.3, location=start_pos)
bpy.ops.object.shade_smooth()
ob = bpy.context.active_object
setMaterial(bpy.context.object, red)#set colour of sphere to red
frame_num=0# set frame number to 0 at start of program

#START OF LOOP
#loop along one particle for all times,ie i is row number, position is the all the elemants on the
row.

for i,position in enumerate(positions):#i is row number, position is the all the elemants on the row.
	if i<20:                                             #i represents the number of timeframes of the animation
		print(position)
		curRow=position
		x_def=float(curRow[0])                                     #x_def= x-position at specific timeframe 
		y_def=float(curRow[1])									   #y_def= y-position at specific timeframe 

		origin=(x_def ,y_def ,0)
		ob.location=origin
		ob.keyframe_insert(data_path="location", frame=frame_num) #insert keyframe at current time frame, with the current position of a particle
		print(x_def)                                               # print x values for debugging purposes
		print(type(position))									   # print position for debugging purposes
		print(origin)                                              # print origin values 
		frame_num += 10
		print(frame_num)