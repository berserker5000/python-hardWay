import random

__author__ = 'kud'
'''
A quest game. With guessing random numbers.
Generate different number of rooms, and several ways to pass a game.
'''


class Room(object):
    def __init__(self):
        self.number = random.randint(1, 7)

    def room_numbers(self):
        if self.number % 2 == 0:
            exits = 2
        else:
            exits = 1
        return "You have %d exits. Try not to die." % exits

    def die(self):
        lives = int(round(self.number / 2))
        die_text = ["Unfortunately you have died.",
                    "You are f*king looser. You DIED!",
                    "Take your ass out from here.Looser!"]
        rand_die = random.choice(die_text)
        return rand_die

def quest_text():
    qtext = ["You're standing near a bear. The only thing you have is a wood plank. You need to pass through. "
            "What should you do?",
            "You see a huuge monkey in this room. She jumps all around the room, but you can't cross it."
            "You have a banana and and a cake. So, what would you do now?",
            "You are on a boat. Here you see plenty of zombies. You have a gun, but there is no bullets."
            "What would you do?"]
    rand_question = random.choice(qtext)
    return rand_question

def quest_answers():
    qanswers1 = ("Don't touch a bear, and just pass it through.",
                "Slap a bear with a plank and run.")

    qanswers2 = ("Give banana to monkey.",
                "Give cake to monkey.",
                "Give all to monkey.",
                "Just run to the door.")

    qanswers3 = ("Run Forest, run!",
                "Through your gun to a zombie.")

    #rand_answer1 = random.choice(qanswers1)
    #rand_answer2 = random.choice(qanswers2)
    #rand_answer3 = random.choice(qanswers3)
    i = 1
    q = quest_text()
    print q
    if str(q) == "You're standing near a bear. The only thing you have is a wood plank. You need to pass through. What should you do?":
        for el in qanswers1:
            print i, el
            i+=1
    elif str(q) == "You see a huuge monkey in this room. She jumps all around the room, but you can't cross it.You have a banana and and a cake. So, what would you do now?":
        for el in qanswers2:
            print i, el
            i+=1
    elif str(q) == "You are on a boat. Here you see plenty of zombies. You have a gun, but there is no bullets.What would you do?":
        for el in qanswers3:
            print i, el
            i+=1

quest_answers()