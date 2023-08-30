"""
Georgia Institute of Technology - CS1301
Homework 01 - Functions & Expressions
"""
#########################################
"""
Function Name: ratsNightTrivia()
Parameters: N/A
Returns: None
"""
def ratsNightTrivia():
        x = input("What is the name of Georgia Tech's fight song? ")
        y = "Ramblin' Wreck from Georgia Tech"
        userResponse = "You answered: {}" .format(x)
        print(userResponse)
        print("The right answer is: {}".format(y))

        print("")

        goodword = input("What's the good word? ")
        correct_goodword = "To hell with georgia"
        userResponse2 = "You answered: {}".format(goodword)
        print(userResponse2)
        print("The right answer is: {}".format(correct_goodword))

########################################
"""
Function Name: rockRambleRoll()
Parameters: N/A
Returns: None
"""
def rockRambleRoll():
    pizza = int(input("How many pizzas do you want at Campus Crust? "))
    sandwiches = int(input("How many sandwiches do you want at 5th Street Deli? "))
    sushi = int(input("How many sushi rolls do you want at Bento Sushi? "))
    tacos = int(input("How many tacos do you want at Twisted Taco? "))

    total = (pizza * 9.00) + (sandwiches * 5.50) + (sushi * 8.00) + (tacos * 2.25)
    print("You need to spend ${} at Rock, Ramble, and Roll.".format(total))

#########################################
"""
Function Name: houseParty()
Parameters: N/A
Returns: None
"""
def houseParty():
    autograph = int(input("How many autographs will you get? "))
    castle = int(input("How many times will you visit the bouncy castle? "))
    video = int(input("How many video game contests will you participate in? "))
    locker = int(input("How many times will you walk through the locker rooms? "))


    total_time = (autograph * 10) + (castle * 20) + (video * 45) + (locker * 15)
    hours = total_time // 60
    minutes = total_time % 60
    print("You will spend {} hour(s) and {} minutes at the house party.".format(hours, minutes))

#########################################
"""
Function Name: budget()
Parameters: N/A
Returns: None
"""
def budget():
    income = float(input("What is your monthly income?"))
    percent = float(input("What percentage of your monthly income do you want to save?"))
    save = income * (percent / 100)

    afterSave = income - save

    afterSave = afterSave - 900
    afterSave = str(afterSave)
    save = str(save)

    print("You can save ${} and spend ${} this month.".format(save, afterSave))
#########################################
"""
Function Name: spareTime()
Parameters: N/A
Returns: None
"""



def spareTime():
    credits = float(input("How many credit hours are you taking? "))
    activity = float(input("How many hours will you devote to extracurricular activities each day? "))

    outsideStudy = credits * 4
    activityTime = activity* 7

    totalTime = (outsideStudy + activityTime)

    minTotal = ((totalTime*60)/7)
    minutes = (960 - minTotal)

    hours = int(minutes//60)

    min2 = minutes % 60
    roundMin = round(min2, 1)

    print("You have {} hour(s) and {} minutes per day to spare.".format(hours, roundMin))

# Test the function

#########################################

