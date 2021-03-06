import math
import matplotlib.pyplot as plt
import sys

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

start = 0
end = len(vdata)
if(len(sys.argv)==4):
    start = int(sys.argv[2])
    end = int(sys.argv[3])

fig, ax1 = plt.subplots(1,1)
ax2 = ax1.twinx()

ax1.set_ylim([-5,80])
ax1.plot(vdata[start:end],color='r',alpha=0.5)
ax2.plot(xdata[start:end],alpha=0.5)
ax2.plot(ydata[start:end],color='b',alpha=0.5)
ax2.plot(zdata[start:end],color='g',alpha=0.5)

plt.show()
