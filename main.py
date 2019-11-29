import time

import environment
import inhabitants
import properties

TTY_SEPERATOR = "-" * 80

# Test to see if inhabitants can live

# world = environment.Environment()

# brownEyeProperty = properties.Property(True)
# blueEyeProperty = properties.Property(False)

# world.inhabitants = []

# for i in range(0, 20):
#     world.inhabitants.append(inhabitants.Inhabitant([
#         properties.PropertyPair(inhabitants.maleGender, inhabitants.femaleGender),
#         properties.PropertyPair(blueEyeProperty, blueEyeProperty)
#     ]))

# while True:
#     total = len(world.inhabitants)
#     males = 0
#     females = 0

#     for inhabitant in world.inhabitants:
#         if inhabitant.gender == inhabitants.MALE:
#             males += 1

#         if inhabitant.gender == inhabitants.FEMALE:
#             females += 1 

#     print("Total:", len(world.inhabitants), "Males:", males, "Females:", females)

#     world.tick()

#     time.sleep(1)

world = environment.Environment()
propertySet = [inhabitants.maleGender, inhabitants.femaleGender]

while True:
    command = input("Evosim > ")

    if command == "":
        # Tick

        world.tick()

        totalInhabitants = len(world.inhabitants)
        maleInhabitants = 0
        femaleInhabitants = 0

        for inhabitant in world.inhabitants:
            if inhabitant.gender == inhabitants.MALE:
                maleInhabitants += 1
            
            if inhabitant.gender == inhabitants.FEMALE:
                femaleInhabitants += 1

        print(TTY_SEPERATOR)
        print("Total inhabitants: " + str(totalInhabitants) + " (" + str(maleInhabitants) + " male inhabitants, " + str(femaleInhabitants) + " female inhabitants)")
        print(TTY_SEPERATOR)
    elif command == "new property":
        # New property

        propertyLabel = input("New property's label? (Leave blank to generate) > ")
        propertyIsDominant = input("Is property dominant? [y/N] > ").lower() == "y"

        newProperty = properties.Property(propertyIsDominant)

        if propertyLabel != "":
            newProperty.label = propertyLabel

        propertySet.append(newProperty)

        print("New property " + str(newProperty.label) + " created")
    elif command == "list properties":
        # List properties

        for propertyID in range(0, len(propertySet)):
            print("[" + str(propertyID) + "] " + str(propertySet[propertyID].label) + " (dominant: " + str(propertySet[propertyID].isDominant) + ")")
    elif command == "new inhabitant":
        # New inhabitant

        inhabitantLabel = input("New inhabitant's label? (Leave blank to generate) > ")

        inhabitantPropertyPairs = []
        firstPropertyID = "-"
        secondPropertyID = "-"

        while firstPropertyID != "":
            firstPropertyID = input("First property ID in property pair? (Leave blank to exit listing) > ")

            if firstPropertyID != "":
                secondPropertyID = input("Second property ID in property pair? > ")

            if firstPropertyID != "" and secondPropertyID != "":
                firstProperty = None
                secondProperty = None

                for propertyObject in propertySet:
                    if propertyObject.label == firstPropertyID:
                        firstProperty = propertyObject
                    
                    if propertyObject.label == secondPropertyID:
                        secondProperty = propertyObject

                if firstProperty == None:
                    print("First property ID not found in property set!")

                if secondProperty == None:
                    print("Second property ID not found in property set!")
                
                if firstProperty == None or secondProperty == None:
                    print("Property pair could not be made!")
                else:
                    inhabitantPropertyPairs.append(properties.PropertyPair(firstProperty, secondProperty))
            else:
                print("Exited listing")

        newInhabitant = inhabitants.Inhabitant(inhabitantPropertyPairs)

        if inhabitantLabel != "":
            newInhabitant.label = inhabitantLabel

        world.inhabitants.append(newInhabitant)

        print("New inhabitant " + str(newInhabitant.label) + " created")
    elif command == "list inhabitants":
        # List inhabitants

        for inhabitantID in range(0, len(world.inhabitants)):
            if world.inhabitants[inhabitantID].gender == inhabitants.MALE:
                print("[" + str(inhabitantID) + "] " + str(world.inhabitants[inhabitantID].label) + " (gender: male, fertility: " + str(world.inhabitants[inhabitantID].fertility) + ", decay: " + str(world.inhabitants[inhabitantID].decay) + ")")
            elif world.inhabitants[inhabitantID].gender == inhabitants.FEMALE:
                print("[" + str(inhabitantID) + "] " + str(world.inhabitants[inhabitantID].label) + " (gender: female, fertility: " + str(world.inhabitants[inhabitantID].fertility) + ", decay: " + str(world.inhabitants[inhabitantID].decay) + ")")
            else:
                print("[" + str(inhabitantID) + "] " + str(world.inhabitants[inhabitantID].label) + " (gender: (unknown), fertility: " + str(world.inhabitants[inhabitantID].fertility) + ", decay: " + str(world.inhabitants[inhabitantID].decay) + ")")