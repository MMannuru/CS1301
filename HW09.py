
def decodeMessage(message):
    if not message:
        return ""

    firstDashIndex = message.find('-')

    if firstDashIndex == -1:
        return message[::-1]

    part1 = message[:firstDashIndex]
    part2 = message[firstDashIndex + 1:]

    decoded1 = decodeMessage(part1)
    decoded2 = decodeMessage(part2)

    return decoded2 + decoded1

def gradeCount(studentList):
    if len(studentList) == 0:
        return 0

    student = studentList[0]

    if student[1] < 0 or student[1] > 100:
        print("{} has incorrect marks recorded.".format(student[0]))

    return student[1] + gradeCount(studentList[1:])

def cafeJosh(menuItems):
    if len(menuItems) == 0:
        return ""

    coffeeOrder = ""

    for i in menuItems:
        if type(i) == list:
            coffeeOrder += cafeJosh(i)
        else:
            coffeeOrder += i

    return coffeeOrder

def midtownPlanner(restaurantChoices):
    def favRestaurant(dict, TAname, restaurant):
        if restaurant in dict:
            dict[restaurant].append(TAname)
            dict[restaurant].sort()
        else:
            dict[restaurant] = [TAname]
        return dict

    if len(restaurantChoices) == 0:
        return {}

    select = restaurantChoices[0]
    return favRestaurant(midtownPlanner(restaurantChoices[1:]), select[0], select[1])


def cookieCounter(numCookies):
    if numCookies == 0:
        return 1
    elif numCookies < 0:
        return 0
    else:
        oneTaken = cookieCounter(numCookies - 1)
        twoTaken = cookieCounter(numCookies - 2)
        threeTaken = cookieCounter(numCookies - 3)
        return oneTaken + twoTaken + threeTaken
