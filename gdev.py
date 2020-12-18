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

drang=8

xdev = []
ydev = []
zdev = []
sdev = []
for i in range(drang,len(vdata)):
    xdev.append(np.std(np.array(xdata[i-drang:i]),ddof=1))
    ydev.append(np.std(np.array(ydata[i-drang:i]),ddof=1))
    zdev.append(np.std(np.array(zdata[i-drang:i]),ddof=1))


sdev = xdev + ydev + zdev

start=0
end=len(xdev)
if(len(sys.argv)==4):
    start = int(sys.argv[2])
    end = int(sys.argv[3])


fig, ax1 = plt.subplots(1,1)
ax2 = ax1.twinx()

ax1.set_ylim([-5,80])
ax1.plot(vdata[start+drang:end+drang],color='r',alpha=0.7)

ax2.plot(sdev[start:end],color='b',alpha=0.5)

plt.show()

