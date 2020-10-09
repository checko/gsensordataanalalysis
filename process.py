import math
import matplotlib.pyplot as pp
import sys

if (len(sys.argv) < 2):
	print('no data file\n')
	exit()
fp = open(sys.argv[1],'r')
line = fp.readline(); # skip one line
gdata = []
line = fp.readline().strip();
while line:
	values = line.split(',')
	x = float(values[0]);
	y = float(values[1]);
	z = float(values[2]);
	g = math.sqrt(x**2 + y**2 + z**2)
	gdata.append(g)
	print(x,y,z,round(g,2))
	line = fp.readline().strip();
print(gdata)
if(len(sys.argv)==4):
	start = int(sys.argv[2])
	end = int(sys.argv[3])
	pp.plot(gdata[start:end])
else:
	start = 0
	end = len(gdata)
pp.plot(gdata[start:end])
pp.ylim((4,16))
pp.show()
