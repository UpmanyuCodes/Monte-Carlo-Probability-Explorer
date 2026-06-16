import random
import math

crossing_needle = 0
trials = int(input("enter the number of trials : "))

total_needle = trials
d = 1
L = 1
for trial in range(trials):

    x = random.uniform(0,d/2)
    theta = random.uniform(0, math.pi/2)

    if L/2*math.sin(theta)>=x:
        crossing_needle = crossing_needle + 1

print(2*total_needle/crossing_needle)





