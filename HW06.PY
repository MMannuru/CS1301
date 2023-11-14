"""
Georgia Institute of Technology - CS1301
Homework 6 - Dictionaries
"""
#########################################
"""
Function Name: stayInSchool()
Parameters: people (list), networth (list), gender (list)
Returns: schoolDict (dict)
"""
def stayInSchool(people, networth, gender):
    schoolDict = {}

    for i in range(len(people)):
        student = people[i]
        net_worth = networth[i]
        gen_var = gender[i]

        if net_worth >= 1:
            if gen_var == "boy":
                school = 'St. Jude'
            elif gen_var == "girl":
                school = 'Constance Billard'
            else:
                continue

            if school not in schoolDict:
                schoolDict[school] = []

            schoolDict[school].append(student)

    for school, students in schoolDict.items():
        students.sort()

    return schoolDict
#########################################
"""
Function Name: pearsonSpecterLitt()
Parameters: candidates (dict)
Returns: report (list)
"""
def pearsonSpecterLitt(candidates):
    applicants = []
    for applicant, (gpa, university) in candidates.items():
        if "Georgia Tech" in university or "Georgia Institute of Technology" in university:
            applicants += [(applicant, gpa)]

    if not applicants:
        print("Somebody find Mike Ross to fix this!")
        return []

    applicants.sort(key=lambda x: (-x[1], x[0]))
    schoolDict = [applicant for applicant, _ in applicants]
    return schoolDict


#########################################
"""
Function Name: showFinder()
Parameters: showPreferences (dict)
Returns: watchDict (dict)
"""
def showFinder(showPreferences):
    watchDict = {}

    for viewer, likedShows in showPreferences.items():
        for show in likedShows:
            if show not in watchDict:
                watchDict[show] = []

            watchDict[show] += [viewer]

    for show, people in watchDict.items():
        people.sort(key=str.lower)

    return watchDict

"""
Function Name: chooseHouse()
Parameters: foodDict (dict)
Returns: venue (str)
"""


def chooseHouse(foodDict):
    thanksgivingList = []

    for family, foods in foodDict.items():
        if "turkey" in foods:
            turkeyVar = foods["turkey"]
        else:
            turkeyVar = 0

        if "gravy" in foods:
            gravyVar = foods["gravy"]
        else:
            gravyVar = 0

        turkeyGravy = turkeyVar + gravyVar

        if turkeyGravy >= 11:
            thanksgivingList.append(family)

    thanksgivingList.sort()

    if not thanksgivingList:
        return "No one has turkey and gravy?!?"
    elif len(thanksgivingList) == 1:
        return "Thanksgiving will be at {}!".format(thanksgivingList[0])
    elif len(thanksgivingList) == 2:
        return "Thanksgiving will be at {} or {}!".format(thanksgivingList[0], thanksgivingList[1])
    else:
        family_names = ", ".join(thanksgivingList[:-1])
        return "Thanksgiving will be at {}, or {}!".format(family_names, thanksgivingList[-1])


"""
Function Name: bananaStand()
Parameters: menu (dict), order (dict)
Returns: revenue (int)
"""
def bananaStand(menu, order):
    revenue = 0

    for item, amount in order.items():
        parts = item.split(" - ")
        name = parts[0]

        if name in menu:
            totalPrice = menu[name]["price"]

            if len(parts) > 1:
                customizations = parts[1].split(", ")
                total_customization_price = 0

                for customization in customizations:
                    if customization in menu[name]:
                        total_customization_price += menu[name][customization]

                totalPrice += total_customization_price

            revenue += totalPrice * amount

    return revenue
