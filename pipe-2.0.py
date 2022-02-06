import matplotlib.pyplot as plt
import numpy as np
filename = "01-gstest1.txt"
#filename = "testShort.txt"


file = open(filename, "r",encoding='latin-1')
lines = file.readlines()
linenum = len(lines)
print("len: " ,linenum)
maxx = [0,""]
maxy = [0,""]
maxz = [0,""]
minx = [0,""]
miny = [0,""]
minz = [0,""]

for i in range(linenum):

	line = lines[i]
	words = line.split()
	name = words[0]
	startx = float(words[1])
	starty = float(words[2])
	startz = float(words[3])
	endx = float(words[4])
	endy = float(words[5])
	endz = float(words[6])
	radius = words[7]


	if i == 0:
		maxx[0] = startx
		maxx[1] = name
		
		maxy[0] = starty
		maxy[1] = name
		
		maxz[0] = startz
		maxz[1] = name

		minx[0] = startx
		minx[1] = name
		
		miny[0] = starty
		miny[1] = name
		
		minz[0] = startz
		maxz[1] = name

		
	if startx > maxx[0]:
		#print("startx > maxx[0]")
		#print(startx,">",maxx)
		maxx[0] = startx
		maxx[1] = name

		
	if starty > maxy[0]:
		maxy[0] = starty
		maxy[1] = name
	if startz > maxz[0]:
		maxx[0] = startz
		maxx[1] = name

	if endx > maxx[0]:
		maxx[0] = endx
		maxx[1] = name
		#print("endx > maxx[0]")
	if endy > maxy[0]:
		maxy[0] = endy
		maxy[1] = name
	if endz > maxz[0]:
		maxz[0] = endz
		maxz[1] = name
	
	if startx < minx[0]:
		minx[0] = startx
		minx[1] = name
	if starty < miny[0]:
		miny[0] = starty
		miny[1] = name
	if startz < minz[0]:
		minz[0] = startz
		minz[1] = name

	if endx < minx[0]:
		minx[0] = endx
		minx[1] = name
	if endy < miny[0]:
		miny[0] = endy
		miny[1] = name
	if endz < minz[0]:
		minz[0] = endz
		minz[1] = name



print("maxx: ",maxx)
print("maxy: ",maxy)
print("maxz: ",maxz)

print("minx: ",minx)
print("miny: ",miny)
print("minz: ",minz)
print("")

intervalx = maxx[0]-minx[0]
intervaly = maxy[0]-miny[0]

percellx = intervalx/10
percelly = intervaly/10

grid = []

for x in range(10):
	grid.append([])
	for y in range(10):
		grid[x].append([])
		grid[x][y].append([])
		grid[x][y].append([])
		grid[x][y].append([])


for x in range(10):
	for y in range(10):
		grid[x][y][0]=x*percellx+minx[0]
		grid[x][y][1]=y*percelly+miny[0]
		grid[x][y][2]=0




for i in range(linenum):
	line = lines[i]

	words = line.split()
	name = words[0]
	startx = float(words[1])
	starty = float(words[2])
	startz = float(words[3])
	endx = float(words[4])
	endy = float(words[5])
	endz = float(words[6])
	radius = float(words[7])

	#startx = (startx-minx[0])/intervalx
	#starty = (starty-miny[0])/intervaly

	#endx = (endx-minx[0])/intervalx
	#endy = (endy-miny[0])/intervaly

	words[1] = startx
	words[2] = starty
	words[4] = endx
	words[5] = endy

	for x in range(10):
		for y in range(10):
			# x边界
			if (x==9 and y!=9):
				if ((startx >= grid[x][y][0] and startx <= grid[x][y][0]+percellx) and
					(starty >= grid[x][y][1] and starty < grid[x][y][1]+percelly)):
					grid[x][y][2]+=1
					continue
			# y边界
			if (x!=9 and y==9):
				if ((startx >= grid[x][y][0] and startx < grid[x][y][0]+percellx) and
					(starty >= grid[x][y][1] and starty <= grid[x][y][1]+percelly)):
					grid[x][y][2]+=1
					continue
			# xy边界
			if (x==9 and y==9):
				if ((startx >= grid[x][y][0] and startx <= grid[x][y][0]+percellx) and
					(starty >= grid[x][y][1] and starty <= grid[x][y][1]+percelly)):
					grid[x][y][2]+=1
					continue

			if ((startx >= grid[x][y][0] and startx < grid[x][y][0]+percellx) and
				(starty >= grid[x][y][1] and starty < grid[x][y][1]+percelly)):
				grid[x][y][2]+=1

# for x in range(10):
# 	print()
# 	for y in range(10):
# 		print(grid[x][y])


fig = plt.figure()
ax1 = fig.add_subplot(111, projection="3d")

xpos = []
ypos = []
zpos = []

for x in range(10):
	xpos.append(grid[x][0][0])
for y in range(10):
	ypos.append(grid[0][y][1])

for x in range(10):
	for y in range(10):
		zpos.append(grid[x][y][2])


ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

for x in range(10):
	for y in range(10):
		ax1.bar3d(grid[x][y][0],grid[x][y][1],0,percellx,percelly,grid[x][y][2])

#ax1.bar3d(xpos,ypos,zpos,dx,dy,dz)
plt.show()