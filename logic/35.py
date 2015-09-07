__author__ = 'kud'
from sys import exit

def gold_room():
    print("This room is fool of gold. How much do you take?")

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a numbers.")

    if how_much < 50:
        print "You win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?"
    bear_moved=False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then pimp slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your crotch off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

def cthulu_room():
    print "Here you see the great evil Cthulu.\nHe whatever stares at you and you go insane.\nDo you flee for life or aet your head?"
    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in the dark room.\nThere is a door to you right and left.\nWhich one do you take?"

    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble aroud the room until you starve.")

start()