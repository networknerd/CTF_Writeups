import sys
import math
flaglist = []
for i in range(1, 13):
	f = open("input/" + str(i) + ".txt", "r")
	n = f.readline().strip()
	dist_x_orig = 0
	dist_y_orig = 0
	dist_x_gps = 0
	dist_y_gps = 0
	for line in f.readlines():
		line = line.strip()
		if line == "north":
			dist_y_gps += 1
			dist_y_orig -= 1
		elif line == "south":
			dist_y_gps -= 1
                        dist_y_orig += 1
		elif line == "east":
			dist_x_gps += 1
                        dist_x_orig -= 1
		elif line == "west":
			dist_x_gps -= 1
                        dist_x_orig += 1
		elif line == "northwest":
			dist_x_gps -= 1
                        dist_x_orig += 1
			dist_y_gps += 1
                        dist_y_orig -= 1
		elif line == "northeast":
			dist_x_gps += 1
                        dist_x_orig -= 1
			dist_y_gps += 1
                        dist_y_orig -= 1
		elif line == "southwest":
			dist_x_gps -= 1
                        dist_x_orig += 1
			dist_y_gps -= 1
                        dist_y_orig += 1
		elif line == "southeast":
			dist_x_gps += 1
                        dist_x_orig -= 1
			dist_y_gps -= 1
                        dist_y_orig += 1
		else:
			raise Exception("Unknown Direction")
	print math.sqrt((pow(abs(dist_x_gps - dist_x_orig),2)) + pow(abs(dist_y_gps - dist_y_orig), 2))
	dist = int(round(math.sqrt((pow(abs(dist_x_gps - dist_x_orig),2)) + pow(abs(dist_y_gps - dist_y_orig), 2))))
	flaglist.append((dist) % 26)
	f.close()

print flaglist

ch = "abcdefghijklmnopqrstuvwxyz"

flag = "".join(ch[i] for i in flaglist)
print flag
