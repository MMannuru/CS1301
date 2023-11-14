def inventoryManager(fileName):
    organizedDict = {}

    try:
        with open(fileName, 'r') as file:
            fileLines = file.readlines()
            fileLines = fileLines[1:]
            strippedLines = [line.strip() for line in fileLines]
            nonemptyLines = [line for line in strippedLines if line]

            for i in range(0, len(nonemptyLines), 4):
                costume = nonemptyLines[i]
                price = float(nonemptyLines[i + 1])
                quantity = int(nonemptyLines[i + 2])
                location = nonemptyLines[i + 3]
                organizedDict[costume] = [price, quantity, location]

    except FileNotFoundError:
        return {}

    return organizedDict

def savvyShopper(fileName, shoppingMethod):
    if shoppingMethod not in ['Online', 'In-store']:
        return ('', 0)

    try:
        with open(fileName, 'r') as file:
            fileLines = file.readlines()
            fileLines = fileLines[1:]
            strippedLines = [line.strip() for line in fileLines]
            nonemptyLines = [line for line in strippedLines if line]

            costumes = {}
            for i in range(0, len(nonemptyLines), 4):
                cosName = nonemptyLines[i]
                cosPrice = float(nonemptyLines[i + 1])
                cosLocation = nonemptyLines[i + 3]

                if cosLocation == shoppingMethod:
                    costumes[cosName] = cosPrice

            if not costumes:
                return ('', 0)

            cheapestName = min(costumes, key=costumes.get)
            cheapestPrice = costumes[cheapestName]
            return cheapestName, cheapestPrice

    except FileNotFoundError:
        return ('', 0)


def costumePairs(totalBudget, shoppingMethod):
    costumes = []

    with open("costumeStore1.txt", 'r') as infile:
        lines = infile.readlines()[2:]
        for i in range(0, len(lines), 5):
            customer = lines[i].strip()
            cost = float(lines[i + 1].strip())
            availability = lines[i + 3].strip()
            if availability == shoppingMethod:
                costumes.append((customer, cost))

    possiblePairs = []
    for i in range(len(costumes)):
        for j in range(i + 1, len(costumes)):
            customer1, cost1 = costumes[i]
            customer2, cost2 = costumes[j]
            if cost1 + cost2 <= totalBudget:
                pair = tuple(sorted([customer1, customer2]))
                possiblePairs.append(pair)

    if not possiblePairs:
        return "No pairs of costumes can be purchased at this time."

    return sorted(possiblePairs)


def logCandies(candyDict):
    totalCan = sum(candyDict.values())

    with open("candylog.txt", "w") as file:
        file.write("Candy Log\n\n")

        for candy, quant in candyDict.items():
            file.write(candy + "\n" + str(quant) + "\n\n")

        file.write("Total Collected: " + str(totalCan))


def sortCostumes(fname):
    with open(fname, 'r') as file:
        char1 = file.read(1)
        if not char1:
            raise ValueError("An empty file was given. There is nothing to sort.")

    inventDict = inventoryManager(fname)
    sortedDict = dict(sorted(inventDict.items(), key=lambda x: (x[1][0], x[0])))

    with open(fname, 'r') as infile:
        header = infile.readline().strip()

    with open("sortedCostumeStore.txt", "w") as outfile:
        outfile.write(header + "\n\n")

        items = list(sortedDict.items())
        for i, (key, value) in enumerate(items):
            outfile.write(str(key) + "\n")
            outfile.write(str(value[0]) + "\n")
            outfile.write(str(value[1]) + "\n")

            if i < len(items) - 1:
                outfile.write(str(value[2]) + "\n\n")
            else:
                outfile.write(str(value[2]))
