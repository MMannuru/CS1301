"""
Georgia Institute of Technology - CS1301
Homework 8 - CSV Files/APIs
"""
#########################################
"""
Function Name: newRecruits()
Parameters: movieNum (int)
Returns: winner (str)
"""
import csv

def newRecruits(movieNum):
    midiChloriansScore = 0
    recruits = False

    with open('starWars.csv', 'r') as file:
        reader = csv.DictReader(file)
        for i in reader:
            if int(i['firstAppearance']) == movieNum:
                recruits = True
                midiChloriansScore += int(i['midi-chlorians'])

    if not recruits:
        return "No new recruits!"
    elif midiChloriansScore > 0:
        return "The Jedis have won by {} points!".format(midiChloriansScore)
    else:
        return "Oh no, the Siths are better!"
"""
Function Name: orgByType()
Parameters: minChlorians (float), maxChlorians (float)
Returns: organizedDict (dict)
"""
import csv

def orgByType(minChlorian, maxChlorian):
    organizedDict = {}

    with open('starWars.csv', 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue

            name, midiChloriansScore, type, appearance = row
            midiChloriansScore = float(midiChloriansScore)

            if minChlorian <= midiChloriansScore <= maxChlorian:
                if type not in organizedDict:
                    organizedDict[type] = []
                organizedDict[type].append(name)

    for i in organizedDict:
        organizedDict[i].sort()

    return organizedDict


"""
Function Name: possiblePlanets()
Parameters: favPlanets (list)
Returns: destinationDict (dict)
"""
import requests

def possiblePlanets(favPlanets):
    destinationDict = {}

    for eachPlanet in favPlanets:
        url = "https://swapi.dev/api/planets/?search={}".format(eachPlanet)
        response = requests.get(url)
        allData = response.json()

        if allData['count'] > 0:
            allPlanetData = allData['results'][0]

            if 'name' in allPlanetData and 'climate' in allPlanetData:
                climate = allPlanetData['climate'].lower()
                if 'temperate' in climate:
                    destinationDict[allPlanetData['name']] = climate

    return destinationDict



"""
Function Name: residentHeights()
Parameters: planet (str)
Returns: heights (list)
"""

import requests
def residentHeights(planet_name):
    residents = []

    planetsUrl = "https://swapi.dev/api/planets/"
    while planetsUrl:
        response = requests.get(planetsUrl)
        allData = response.json()

        for eachPlanet in allData['results']:
            if eachPlanet['name'].lower() == planet_name.lower():
                for resident_url in eachPlanet['residents']:
                    resident_response = requests.get(resident_url)
                    resident_data = resident_response.json()
                    resident_height = resident_data['height']
                    resident_name = resident_data['name']

                    try:
                        resident_height = int(resident_height)
                        residents.append((resident_height, resident_name))
                    except ValueError:
                        continue

                residents.sort()
                return residents

        planetsUrl = allData.get('next')

    return []


"""
Function Name: starshipInfo()
Parameters: starships (list)
Returns: None (NoneType)
"""
import requests


def starshipInfo(starship_names):
    header = "Starship Name,Model,Starship Class,Passengers\n"
    starship_data = ""
    api_base_url = "https://swapi.dev/api/starships/?search="

    with open("starships.csv", "w") as outfile:
        for index, starship_name in enumerate(starship_names):
            try:
                formatted_name = starship_name.replace(" ", "%20")
                response = requests.get(api_base_url + formatted_name)
                starship_info = response.json()

                name = starship_info["results"][0]["name"] + ","
                model = starship_info["results"][0]["model"] + ","
                starship_class = starship_info["results"][0]["starship_class"] + ","
                passengers = starship_info["results"][0]["passengers"]

                if index < len(starship_names) - 1:
                    starship_data += name + model + starship_class + passengers + "\n"
                else:
                    starship_data += name + model + starship_class + passengers
            except:
                pass

        if not starship_data:
            header = header.rstrip("\n")

        outfile.write(header + starship_data)
