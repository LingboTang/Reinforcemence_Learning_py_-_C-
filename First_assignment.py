#This is the for the first question

import numpy
from pylab import *
import matplotlib.pyplot as plt

#target_list = [1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0]
value = 0
counter = 1
stepsize = 0.5
target =1
counterList = []
counterList.append(counter)
valueList = []
valueList.append(value)
while counter <= 100:
    
    if counter <= 6:
        target = 1
    elif (counter > 6) and (counter < 12):
        target = 0
    elif counter > 12:
        if target == 0:
            target = target + 1
        else:
            target = target - 1
    
    #target = target_list[counter-1]
    #print(counter,"--",target)    
    value = value+stepsize*(target-value)
    print(counter,"--",value)
    counter += 1
    counterList.append(counter)
    valueList.append(value)
    
    
plt.plot(valueList)
plt.show()
