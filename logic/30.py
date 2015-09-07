__author__ = 'kud'
people = 30
cars = 40
buses = 15

if cars>people:
    print("We should take the cars.")
elif cars<people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses>people:
    print("There are too many buses.")
elif buses<people:
    print("Could take a bus.")
else:
    print("Still can't decide.")

if people>buses:
    print("Just buses.")
else:
    print("Let's stay at home")