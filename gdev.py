import math
import matplotlib.pyplot as plt
import sys
import numpy as np

if (len(sys.argv) < 2):
    print('no data file\n')
    exit()

fp = open(sys.argv[1],'r')
vdata = []
xdata = []
ydata = []
zdata = []
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
    ydata.append(y)
    zdata.append(z)
    line = fp.readline()

xdev = [];
for i in range(5,len(vdata)):
    xdev.append(np.std(np.array(xdata[i-5:i]),ddof=1))

start=0
end=len(xdev)
if(len(sys.argv)==4):
    start = int(sys.argv[2])
    end = int(sys.argv[3])


fig, ax1 = plt.subplots(1,1)
ax2 = ax1.twinx()

ax1.set_ylim([-5,80])
ax1.plot(vdata[start+5:end+5],color='r',alpha=0.6)

ax2.plot(xdev[start:end],color='b',alpha=0.6)

plt.show()

