import time

import environment
import inhabitants
import properties

TTY_SEPERATOR = "-" * 80

world = environment.Environment()
propertySet = [inhabitants.maleGender, inhabitants.femaleGender]

commandRepetition = 0

try:
    while True:
        if commandRepetition == 0:
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
        elif command == "exit":
            # Exit Evosim

            print("Goodbye")
            
            exit()
        elif command == "repeat":
            # Repeat command

            try:
                command = input("Command to repeat? (Type '#' to cancel) > ")

                if command != "#":
                    commandRepetition = int(input("Number of times to repeat command? (Leave blank to cancel) > ")) + 1
            except:
                pass
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
            firstPropertyLabel = "-"
            secondPropertyLabel = "-"

            while firstPropertyLabel != "":
                firstPropertyLabel = input("First property label in property pair? (Leave blank to exit listing) > ")

                if firstPropertyLabel != "":
                    secondPropertyLabel = input("Second property label in property pair? > ")

                if firstPropertyLabel != "" and secondPropertyLabel != "":
                    firstProperty = None
                    secondProperty = None

                    for propertyObject in propertySet:
                        if propertyObject.label == firstPropertyLabel:
                            firstProperty = propertyObject
                        
                        if propertyObject.label == secondPropertyLabel:
                            secondProperty = propertyObject

                    if firstProperty == None:
                        print("First property label not found in property set!")

                    if secondProperty == None:
                        print("Second property label not found in property set!")
                    
                    if firstProperty == None or secondProperty == None:
                        print("Property pair could not be made!")
                    else:
                        inhabitantPropertyPairs.append(properties.PropertyPair(firstProperty, secondProperty))
                else:
                    print("Exited listing")

            newInhabitant = inhabitants.Inhabitant(world.tickcount, inhabitantPropertyPairs)

            if inhabitantLabel != "":
                newInhabitant.label = inhabitantLabel

            world.inhabitants.append(newInhabitant)

            print("New inhabitant " + str(newInhabitant.label) + " created")
        elif command == "new inhabitant batch":
            # New batch creation of inhabitants

            inhabitantPropertyPairs = []
            firstPropertyLabel = "-"
            secondPropertyLabel = "-"

            while firstPropertyLabel != "":
                firstPropertyLabel = input("First property label in property pair? (Leave blank to exit listing) > ")

                if firstPropertyLabel != "":
                    secondPropertyLabel = input("Second property label in property pair? > ")

                if firstPropertyLabel != "" and secondPropertyLabel != "":
                    firstProperty = None
                    secondProperty = None

                    for propertyObject in propertySet:
                        if propertyObject.label == firstPropertyLabel:
                            firstProperty = propertyObject
                        
                        if propertyObject.label == secondPropertyLabel:
                            secondProperty = propertyObject

                    if firstProperty == None:
                        print("First property label not found in property set!")

                    if secondProperty == None:
                        print("Second property label not found in property set!")
                    
                    if firstProperty == None or secondProperty == None:
                        print("Property pair could not be made!")
                    else:
                        inhabitantPropertyPairs.append(properties.PropertyPair(firstProperty, secondProperty))
                else:
                    print("Exited listing")

            try:
                for i in range(0, int(input("Number of inhabitants to create? (Leave blank to cancel) > "))):
                    for propertyPair in inhabitantPropertyPairs:
                        propertyPair.selectDominantProperty()

                    newInhabitant = inhabitants.Inhabitant(world.tickcount, inhabitantPropertyPairs)

                    world.inhabitants.append(newInhabitant)

                    print("New inhabitant " + str(newInhabitant.label) + " created")
            except:
                pass
        elif command == "list inhabitants":
            # List inhabitants

            for inhabitantID in range(0, len(world.inhabitants)):
                if world.inhabitants[inhabitantID].gender == inhabitants.MALE:
                    print("[" + str(inhabitantID) + "] " + str(world.inhabitants[inhabitantID].label) + " (birthtick: " + str(world.inhabitants[inhabitantID].birthtick) + ", age: " + str(world.tickcount - world.inhabitants[inhabitantID].birthtick) + ", gender: male, fertility: " + str(world.inhabitants[inhabitantID].fertility) + ", decay: " + str(world.inhabitants[inhabitantID].decay) + ")")
                elif world.inhabitants[inhabitantID].gender == inhabitants.FEMALE:
                    print("[" + str(inhabitantID) + "] " + str(world.inhabitants[inhabitantID].label) + " (birthtick: " + str(world.inhabitants[inhabitantID].birthtick) + ", age: " + str(world.tickcount - world.inhabitants[inhabitantID].birthtick) + ", gender: female, fertility: " + str(world.inhabitants[inhabitantID].fertility) + ", decay: " + str(world.inhabitants[inhabitantID].decay) + ")")
                else:
                    print("[" + str(inhabitantID) + "] " + str(world.inhabitants[inhabitantID].label) + " (birthtick: " + str(world.inhabitants[inhabitantID].birthtick) + ", age: " + str(world.tickcount - world.inhabitants[inhabitantID].birthtick) + ", gender: (unknown), fertility: " + str(world.inhabitants[inhabitantID].fertility) + ", decay: " + str(world.inhabitants[inhabitantID].decay) + ")")
        elif command == "inspect inhabitant":
            # Inspect an inhabitant

            inhabitantLabel = input("Label of inhabitant to inspect? (Leave blank to cancel) > ")

            for inhabitant in world.inhabitants:
                if inhabitant.label == inhabitantLabel:
                    if inhabitant.gender == inhabitants.MALE:
                        print("gender: male")
                    elif inhabitant.gender == inhabitants.FEMALE:
                        print("gender: female")
                    else:
                        print("gender: (unknown)")
                
                    print("fertility: " + str(inhabitant.fertility))
                    print("decay: " + str(inhabitant.decay))
                    print("property pairs:")

                    for propertyPair in inhabitant.propertyPairs:
                        print("    - (dominant: " + str(propertyPair.dominantProperty.label) + ")")
                        print("        - " + str(propertyPair.firstProperty.label))
                        print("        - " + str(propertyPair.secondProperty.label))

                    print("expressed properties:")

                    for propertyObject in inhabitant.expressedProperties:
                        print("    - " + str(propertyObject.label))
        elif command == "new condition":
            # New condition

            conditionLabel = input("New condition's label? (Leave blank to generate) > ")
            affectingPropertyLabel = input("Affecting property's label? (Leave blank to cancel) > ")

            try:
                decay = int(input("Decay length? (Leave blank for 5) > "))
            except:
                decay = 5

            try:
                for propertyObject in propertySet:
                    if propertyObject.label == affectingPropertyLabel:
                        affectingProperty = propertyObject

                        newCondition = environment.Condition(world.tickcount, affectingProperty, decay)

                        if conditionLabel != "":
                            newCondition.label = conditionLabel
                        
                        world.conditions.append(newCondition)

                        print("New condition " + str(newCondition.label) + " created")
            except:
                pass
        elif command == "list conditions":
            # List conditions

            for conditionID in range(0, len(world.conditions)):
                print("[" + str(conditionID) + "] " + str(world.conditions[conditionID].label) + " (birthtick: " + str(world.conditions[conditionID].birthtick) + ", age: " + str(world.tickcount - world.conditions[conditionID].birthtick) + ", affecting property: " + str(world.conditions[conditionID].affectingProperty.label) + ", decay: " + str(world.conditions[conditionID].decay) + ")")
        elif command == "calculate property adoption":
            # Calculate a property's adoption rate

            propertyLabel = input("Property label to use in calculation? (Leave blank to cancel) > ")

            totalInhabitants = 0
            totalAdoption = 0
            totalExpression = 0

            for propertyObject in propertySet:
                if propertyObject.label == propertyLabel:
                    totalInhabitants = 0
                    totalAdoption = 0
                    totalExpression = 0

                    for inhabitant in world.inhabitants:
                        totalInhabitants += 1

                        hasAdoption = False

                        for propertyPair in inhabitant.propertyPairs:
                            if propertyPair.firstProperty == propertyObject or propertyPair.secondProperty == propertyObject:
                                hasAdoption = True
                            
                        if propertyObject in inhabitant.expressedProperties:
                            hasAdoption = True
                            totalExpression += 1

                        if hasAdoption:
                            totalAdoption += 1

            if totalInhabitants != 0:
                print("Total adoption: " + str(totalAdoption) + "/" + str(totalInhabitants) + " (" + str((totalAdoption / totalInhabitants) * 100) + "%)")
                print("Total expression: " + str(totalExpression) + "/" + str(totalInhabitants) + " (" + str((totalExpression / totalInhabitants) * 100) + "%)")
            else:
                print("No inhabitants to calculate adoption with!")
        else:
            print("Command not understood!")

        if commandRepetition > 0:
            commandRepetition -= 1

            if commandRepetition > 0:
                print("Repeating command " + str(commandRepetition) + " times")
            else:
                print("Finished repeating command")
except KeyboardInterrupt:
    print("")
    print("*Mutters really quickly before Pythons bite the exception* Goodbye")