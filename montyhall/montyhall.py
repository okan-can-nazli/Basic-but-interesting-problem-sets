import random

doors = ["1", "2", "3"]
win = 0
experimental_case_number = 100000

for i in range(experimental_case_number):
    car_door = random.choice(doors)
    first_select = random.choice(doors)

    open_door = random.choice([x for x in doors if x != car_door and x != first_select])

    final_select = [x for x in doors if x not in (first_select, open_door)][0]

    if final_select == car_door:
        win += 1

    print("%",win / experimental_case_number * 100)
