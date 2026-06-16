import random

inside_points = 0
trials = int(input("Enter the number of trials : "))
total_points = trials

for trial in range(trials):
    x = random.uniform(0,1)
    y = random.uniform(0,1)

    if x**2 + y**2 < 1:
        inside_points = inside_points + 1

print(4*inside_points/total_points)