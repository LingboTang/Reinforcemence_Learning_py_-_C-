#Pseudocode for Greedy N-armed Bandit Algorithms

import random

Action = [0,1,2,3,4,5,6,7,8,9,10]
number_of_activate = [1,1,1,1,1,1,1,1,1,1]
Total_target = [0,0,0,0,0,0,0,0,0,0]
Average_target = [0,0,0,0,0,0,0,0,0,0]

#select e// In the original post
e = 0

def bandit(a):
    reward = a + random.uniform(-1,1)
    return reward


while True:
    x = random.uniform(0,1)
    if x < 0:
        m = random.randint(0,10)
        Old_estimate = Action[m]
        Target = bandit(old_estimate)
        number_of_activate[m]+=1
        Total_target[m] += Target
        print(Total_target)
        print(Average_target)
    else:
        for m in range(0,10):
            Average_target[m] = Total_target[m]/number_of_activate[m]
        best_estimate = max(Average_target)
        Target = bandit(best_estimate)
        index_of_best = Average_target.index(best_estimate)
        number_of_activate[index_of_best] += 1
        Total_target[index_of_best] += Target
        print(Total_target)
        print(Average_target)
