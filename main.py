# list of functions to be used

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")

        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid Input! Please try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range! Please try again!")


racers = get_number_of_racers()
