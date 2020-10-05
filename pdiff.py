import math
import matplotlib.pyplot as pp
import sys

if (len(sys.argv) < 2):
	print('no data file\n')
	exit()
fp = open(sys.argv[1],'r')
line = fp.readline()
gdiff = []
values = fp.readline().strip().split(',')
xp = float(values[0])
yp = float(values[1])
zp = float(values[2])
line = fp.readline().strip()
while line:
	values = line.split(',')
	x = float(values[0])
	y = float(values[1])
	z = float(values[2])
	gdiff.append([x-xp, y-yp, z-zp])
	if ( (x-xp) != 0 ):
		print(1,round((y-yp)/(x-xp),2), round((z-zp)/(x-xp),2), round(x-xp,2),round(y-yp,2),round(z-zp,2))
	elif ((x-xp)==0 and (y-yp)==0 and (z-zp)==0):
		print(round(x,2),round(y,2),round(z,2))
	else:	
		print(round(x-xp,2), round(y-yp,2), round(z-zp,2))
	xp = x
	yp = y
	zp = z
	line = fp.readline().strip()


