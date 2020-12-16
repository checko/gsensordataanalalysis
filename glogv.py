import math
import matplotlib.pyplot as pp
import sys

if (len(sys.argv) < 2):
    print('no data file\n')
    exit()

fp = open(sys.argv[1],'r')
gdata = []
line = fp.readline()
print(line)
while line:
    value = line.split(',')
    x = float(value[0])
    y = float(value[1])
    z = float(value[2])
    v = float(value[4])
    gdata.append(v)
    line = fp.readline()
pp.plot(gdata)
pp.show()
