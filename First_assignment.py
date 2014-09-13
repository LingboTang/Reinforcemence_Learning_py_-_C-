#This is the for the first question

#target_list = [1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0]
value = 0
counter = 2
stepsize = 1.5
target =1
while counter <= 100:
    '''if counter <= 6:
        target = 1
    elif (counter >= 7) and (counter < 12):
        target = 0
    elif counter >= 13:
        if target == 0:
            target = target + 1
        else:
            target = target - 1'''
    
    #target = target_list[counter-1]
    #print(counter,"--",target)    
    value = value+stepsize*(target-value)
    print(counter,"--",value)
    counter += 1
    