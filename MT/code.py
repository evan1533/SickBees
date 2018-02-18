from scipy.io import wavfile as scp
import numpy
import math
import cmath

index = 40000
[rate,array] = scp.read("c.wav")
temp = [0]*int(rate/20)
for i in range(len(temp)):
	temp[i] = array[index]
	index = index +1
for f in range(10,4096):
	sum = 0
	for t in range(len(temp)):
		sum = sum + array[t]*numpy.real(cmath.exp(-2*math.pi*cmath.sqrt(-1)*(t/rate)*f))

	result = sum/(len(temp))
	print(result," ",f)