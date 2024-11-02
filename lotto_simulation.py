import random

def give_me_your_numbers():
    your_list_of_numbers = []
    while len(your_list_of_numbers) < 6:
        your_number = input("Give me one number: ")
        try:
            your_number = int(your_number)
        except ValueError:
            print("That's not a number.")
            continue
        if your_number in your_list_of_numbers:
            print("You have already this number in your list.")
            continue
        if your_number not in range(1,50):
            print("It's out of range")
            continue
        your_list_of_numbers.append(your_number)
    your_list_of_numbers.sort()
    print(", ".join(str(number) for number in your_list_of_numbers))
    return your_list_of_numbers

def draw_the_numbers():
    drawned_numbers = [i for i in range(1,49)]
    random.shuffle(drawned_numbers)
    return drawned_numbers[:6]

def check_wins():
    hits = 0
    wins_list = draw_the_numbers()
    my_list = give_me_your_numbers()
    for number in my_list:
        if number in wins_list:
            hits += 1
    return hits


print(f"Your hits: {check_wins()}")