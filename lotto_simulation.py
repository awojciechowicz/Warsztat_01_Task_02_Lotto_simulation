def give_me_your_numbers():
    your_list_of_numbers = []
    your_number = input("Give me one number: ")
    try:
        your_number = int(your_number)
    except ValueError:
        print("That's not an integer.")
    if your_number in your_list_of_numbers:
        print("You have already this number in your list.")
    if your_number not in range(1,50):
        print("It's out of range")

give_me_your_numbers()