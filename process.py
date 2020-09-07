fp = open('./gvalue0.txt','r')
line = fp.readline()
while line:
	print(line.strip())
	line = fp.readline()

