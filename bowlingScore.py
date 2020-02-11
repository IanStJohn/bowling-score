# Author: Ian St. John
# Date: Feb 6, 2020
#=====================

def bowlingScore(input):
    """ Return the sum of a game of 10 pin bowling, where input is a string of rolls.

    Args:
        input: a string representing rolls in a game of bowling.

    Returns:
        score: the sum of the rolls according to the rules of 10 pin bowling.

    >>> bowlingScore("X-X-X-X-X-X-X-X-X-XXX")
    300
    >>> bowlingScore("45-54-36-27-09-63-81-18-90-72")
    90
    >>> bowlingScore("5/-5/-5/-5/-5/-5/-5/-5/-5/-5/-5")
    150
    """
    def rollScore(index):
        """ Get the numerical representation of the character at the inputted index.
        
        String rolls must be initialized with bowlingScore's input value before running.
        Assumes '/' is never first in the set of rolls.

        Args:
            index: the integer index for the roll to be calculated.

        Returns:
            An integer representing the score for that roll.
        """
        if rolls[index] == 'X': 
            return 10
        elif rolls[index] == '/': 
            return 10 - int(rolls[index - 1])
        else: 
            return int(rolls[index])

    # Process input/filter out unwanted characters.
    rolls = input.replace('-','')

    # Initialize the variables.
    frames = 10
    score = 0

    # Loop through all of the rolls in the input.
    for roll_i, roll in enumerate(rolls):
        # Check if iterated through 10th frame.
        if frames <= 0:
            return score

        # Each roll is half a frame, so decrement by 1/2.
        frames -= .5

        # Check the value of the roll and add up score accordingly.
        if roll == 'X':
            score += 10 + rollScore(roll_i + 1) + rollScore(roll_i + 2)
            frames -= .5 # Strikes are a whole frame, so decrement by another 1/2.
        elif roll == '/': 
            score += rollScore(roll_i) + rollScore(roll_i + 1)
        else: 
            score += int(roll)

    # If exit loop before 10 frames, then input data is too short, return -1 status.
    return score if frames <= 0 else -1

# doctest used to quickly automate testing.
if __name__ == "__main__":
    import doctest
    doctest.testmod()