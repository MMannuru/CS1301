"""
Georgia Institute of Technology - CS1301
Homework 3 - Iteration

"""
#########################################
"""
Function Name: reviveSecretMessage()
Parameters: corruptedMessage (str)
Returns: revivedMessage (str)
"""


def reviveSecretMessage(corruptedMessage):
    revivedMessage = ""
    for char in corruptedMessage:
        if char not in ('(', '#', '%'):
            revivedMessage += char
    return revivedMessage


#########################################
"""
Function Name: crackCode()
Parameters: code1 (str), code2 (str)
Returns: message (str)
"""


def crackCode(code1, code2):
    message = ""
    reverse1 = (code1[::-1])
    reverse2 = (code2[::-1])

    length = len(code1)

    for i in range(length):
        if reverse1[i] == reverse2[i]:
            message += reverse1[i]
    return message
#########################################
"""
Function Name: calculateDistance()
Parameters: operations (str), initialNumber (int)
Returns: lowerDistance (int)
"""
def calculateDistance(operations, initialNumber):
    distanceLower = initialNumber
    while distanceLower <= 30:
        for char in operations:
            if char == '*':
                distanceLower *= 3
            elif char == '/':
                distanceLower //= 2
            elif char == '+':
                distanceLower += 7
            elif char == '-':
                distanceLower -= 4
        if distanceLower > 30:
            break
    return distanceLower

#########################################
"""
Function Name: escapeThumbs()
Parameters: numberOfThumbs (int), obstacles (str)
Returns: message (str)
"""


def escapeThumbs(numberOfThumbs, obstacles):
    start = 0
    for i in range(len(obstacles)):
        if obstacles[i] == ',' or i == len(obstacles) - 1:
            obstacle_length = i - start + 1 if i == len(obstacles) - 1 else i - start
            numberOfThumbs -= 1
            start = i + 1

        if numberOfThumbs == 0:
            return "Success! You've escaped!"

    if numberOfThumbs > 0:
        return "Mission failed: {} still following!".format(numberOfThumbs)


"""
Function Name: timeLeft()
Parameters: puzzleTimes (str), minutesLeft (int)
Returns: result (str)
"""


def timeLeft(puzzleTimes, minutesLeft):
    total = 0

    for i in range(0, len(puzzleTimes), 2):
        newPuzzleTime = int(puzzleTimes[i:i + 2])
        total = total + newPuzzleTime

    myTime = total * 2

    if myTime <= minutesLeft:
        leftOverMin = minutesLeft - myTime
        return "You have {} minutes left over!".format(leftOverMin)
    else:
        return "London is doomed..."
#########################################
