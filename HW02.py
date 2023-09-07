"""
Georgia Institute of Technology - CS1301
Homework 2 - Conditionals
"""
#########################################
"""
Function Name: chickenAndEggs()
Parameters: numDays (int), numEggs (int), numChicken (int),
mealsOutside (int)
Returns: isExpired (bool)
"""
def chickenAndEggs(numDays, numEggs, numChicken, mealsOutside):
    totalEgg = numEggs * 4
    totalChicken = numChicken * 2

    totalMeals = (numDays * 3) - mealsOutside

    if totalMeals >= totalEgg + totalChicken:
        return True
    else:
        return False
#########################################
"""
Function Name: enterTheCave()
Parameters: phrase (str), code (int)
Returns: None (NoneType)
"""
def enterTheCave(phrase, code):
    if phrase == "Open Sesame" and (code >= 0 and code <= 25):
        print("You have opened the door")
    elif phrase == "Hello World" and (code >= 75 and code <= 100):
        print("You have opened the door")
    elif phrase == "Python Enjoyer" and (code == 50):
        print("You have closed the door")
    else:
        print("INTRUDER ALERT")
"""
Function Name: jackAndJill()
Parameters: jackHeight (int), jillHeight (int), jamesHeight (int),
direction (str)
Returns: personInFront (str)
"""
def jackAndJill(jackHeight, jillHeight, jamesHeight, direction):
    if direction == "downhill":
        if jackHeight > jillHeight and jackHeight > jamesHeight:
            return "Jack needs to be in front."
        elif jillHeight >  jackHeight and jillHeight > jamesHeight:
            return "Jill needs to be in front."
        else:
            return "James needs to be in front."
    else:
        if jackHeight < jillHeight and jackHeight < jamesHeight:
            return "Jack needs to be in front."
        elif jillHeight <  jackHeight and jillHeight < jamesHeight:
            return "Jill needs to be in front."
        else:
            return "James needs to be in front."
#########################################
"""
Function Name: closestShip()
Parameters: currentPosition (int)
Returns: None (NoneType)
"""
def closestShip(currentPosition):
    Dutchman = 175
    Peng = 320
    Pearl = 515

    position = abs(currentPosition)

    if position < Dutchman:
        print("The Flying Dutchman")
    elif position < Peng:
        print("Hai Peng")
    else:
        print("The Black Pearl")






#########################################
"""
Function Name: wizardOfOz()
Parameters: maxDistance (int), maxHostility (float)
Returns: locationToVisit (str)
"""
def wizardOfOz(maxDistance, maxHostility):
    desert = 200
    Munchkin = 600
    Winkie = 1000
    City = 1500

    if maxDistance >= desert and maxHostility >= 9.0:
        return "Deadly Desert"
    elif maxDistance >= Munchkin and maxHostility >= 7.0:
        return "Munchkin Country"
    elif maxDistance >= Winkie and maxHostility >= 5.0:
        return "Winkie Country"
    elif maxDistance >= City and maxHostility >= 1.0:
        return "Emerald City"
    else:
        return "Dorothy must go back to Kansas."
#########################################


















