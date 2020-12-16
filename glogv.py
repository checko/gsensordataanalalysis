import math
import matplotlib.pyplot as plt
import sys

if (len(sys.argv) < 2):
    print('no data file\n')
    exit()

fp = open(sys.argv[1],'r')
vdata = []
xdata = []
line = fp.readline()
print(line)
while line:
    value = line.split(',')
    x = float(value[0])
    y = float(value[1])
    z = float(value[2])
    v = float(value[4])
    vdata.append(v)
    xdata.append(x)
    line = fp.readline()
fig, ax1 = plt.subplots(1,1)
ax2 = ax1.twinx()

ax1.plot(vdata,color='r',alpha=0.5)
ax2.plot(xdata,alpha=0.5)

plt.show()
