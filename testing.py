# Author: Ian St. John
# Date: Feb 6, 2020
#=====================

from random import randrange
from bowlingScore import bowlingScore

def gen():
    """ Returns a string that represents a 12 frame game of bowling with random rolls.
    Used to quickly generate test cases for bowlingScore.py

    Returns:
        A string representation of rolls in a game of bowling.
    """

    output = ""
    frame = 12
    prior = 0
    second = 0

    while frame > 0:
        frame -= .5
        roll = randrange(11 - prior)

        # If strike is rolled:
        if roll == 10:
            output += "X"
            frame -= .5
            prior = 0
            second = 0

        # If spare is rolled:
        elif second == 1 and roll + prior == 10:
            output += "/"
            prior = 0
            second = 0

        # If not strike or spare:
        else:
            output += str(roll)
            prior = roll
            second = 1 - second

        # Deliminate frames:
        if second == 0:
            output += "-"

    return output[:-1]


input = gen()                                       # Generate the input.
print(input + " = " + str(bowlingScore(input)))     # Print input and output to later hand verify.