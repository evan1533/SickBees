from scipy.io import wavfile as scp
import numpy
import math
import cmath


[rate,array] = scp.read("Moonlight.wav")
temp = [0]*int(rate/10)
index = int(rate/10);
for i in range(len(temp)):
	temp[i] = array[index]
	index = index +1
results = []
for f in range(10,1201):
	sum = 0
	for t in range(len(temp)):
		sum = sum + temp[t]*numpy.real(cmath.exp(-2*math.pi*cmath.sqrt(-1)*(t/rate)*f))

	results.append([math.fabs(sum)/(len(temp)),f])
	
for num in results:
    spacestr = "";
    #if num[0]>0.5:
     #   spacestr = "      "
    #spacestr = " "*int(num[0]/2)
    print(spacestr,num[0]," ",num[1])

print(max(results))
