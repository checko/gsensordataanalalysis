import math

fp = open('./gvalue0.txt','r')
line = fp.readline(); # skip one line
line = fp.readline().strip();
while line:
	values = line.split(',')
	x = float(values[0]);
	y = float(values[1]);
	z = float(values[2]);
	g = math.sqrt(x**2 + y**2 + z**2)
	print(x,y,z,g)
	line = fp.readline().strip();

