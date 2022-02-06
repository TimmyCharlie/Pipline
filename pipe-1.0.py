from turtle import *
import tkinter as tk
from tkinter import filedialog


def main(filename):

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


	screensize(1024,768,'white')
	pensize(2)
	penup()
	hideturtle()
	speed(0)

	renderinterval = int((linenum+1)/1800)
	if linenum < 1800:
		renderinterval = 1
	print("renderinterval:",renderinterval)
	
	for i in range(linenum):
		line = lines[i]

		if i%renderinterval == 0:

			words = line.split()
			name = words[0]
			startx = float(words[1])
			starty = float(words[2])
			startz = float(words[3])
			endx = float(words[4])
			endy = float(words[5])
			endz = float(words[6])
			radius = float(words[7])

			startx = (startx-minx[0])/intervalx
			starty = (starty-miny[0])/intervaly

			endx = (endx-minx[0])/intervalx
			endy = (endy-miny[0])/intervaly

			words[1] = startx
			words[2] = starty
			words[4] = endx
			words[5] = endy


			#print(words[1],words[2],words[4],words[5])
			if radius <= 300:
				pencolor("blue")
			elif radius > 300 and radius < 500:
				pencolor("red")
			else:
				pencolor("yellow")
			print(i+1,"/",linenum)
			goto((words[1]-0.5)*768,(words[2]-0.5)*768)
			pendown()
			goto((words[4]-0.5)*768,(words[5]-0.5)*768)
			penup()



		pencolor("black")

	goto(-600,350)
	write("maxx: ")
	goto(-570,350)
	write(maxx)

	goto(-600,330)
	write("maxy: ")
	goto(-570,330)
	write(maxy)
	

	goto(-600,310)
	write("maxz: ")
	goto(-570,310)
	write(maxz)

	goto(-600,290)
	write("minx: ")
	goto(-570,290)
	write(minx)

	goto(-600,270)
	write("miny: ")
	goto(-570,270)
	write(miny)

	goto(-600,250)
	write("minz: ")
	goto(-570,250)
	write(minz)
	
	done()		
	



#main("01-gstest1.txt")
#main("天然气管线C3.txt")
root = tk.Tk()
root.withdraw()
filepath = filedialog.askopenfilename()
main(filepath)
	
