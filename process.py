fp = open('./gvalue0.txt','r')
line = fp.readline(); # skip one line
line = fp.readline().strip();
while line:
	values = line.split(',')
	x = float(values[0]);
	y = float(values[1]);
	z = float(values[2]);
	print(x,y,z)
	line = fp.readline().strip();

