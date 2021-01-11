import math
import sys
import numpy as np

if(len(sys.argv) < 2):
    print('no data file\n')
    exit()

fp = open(sys.argv[1],'r')
vdata = []
xdata = []
ydata = []
zdata = []
line = fp.readline()
while(line):
    value = line.split(',')
    xdata.append(float(value[0]))
    ydata.append(float(value[1]))
    zdata.append(float(value[2]))
    vdata.append(float(value[4]))
    line = fp.readline()

averno=10
xave = []
yave = []
zave = []
for i in range(averno,len(vdata)):
    xave.append(np.average(xdata[i-averno:i]))
    yave.append(np.average(ydata[i-averno:i]))
    zave.append(np.average(zdata[i-averno:i]))

for i in range(len(zave)):
    print xave[i],',',yave[i],',',zave[i],', 0.0 ,',vdata[i+averno]
