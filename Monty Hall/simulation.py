import random

stay_wins = 0
switch_wins = 0

trials = int(input("Enter the number of trials : "))

for timer in range(trials):
    doors = [1,2,3]

    car_choice = random.choice(doors) 

    player_choice = random.choice(doors) 

    host_options = []

    for door in doors:
        if door!=player_choice and door!=car_choice:
            host_options.append(door)

    host_opens = random.choice(host_options)

    for door in doors:
        if door!=player_choice and door!=host_opens:
            switch_door = door 

    if car_choice == switch_door:
        switch_wins = switch_wins+1

    if car_choice == player_choice:
        stay_wins = stay_wins+1

print("stay : ",stay_wins/trials)
print("switch : ",switch_wins/trials)



