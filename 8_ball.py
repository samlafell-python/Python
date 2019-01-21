# Magic 8 Ball Program

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is almost certain'
    elif answerNumber == 3:
        return 'It is likely'
    elif answerNumber == 4:
        return 'It is somewhat likely'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'It is unlikely'
    elif answerNumber == 8:
        return 'Outlook not good'
    elif answerNumber == 9:
        return 'Very doubtful'

print('Think of a yes or no question and press enter to see the Magic 8 Ball fortune')
input()

print(getAnswer(random.randint(1,9)))
