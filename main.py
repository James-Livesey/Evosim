import time
import os
import json

import scripting
import environment
import inhabitants
import properties

TTY_SEPERATOR = "-" * 80

world = environment.Environment()
propertySet = [inhabitants.maleGender, inhabitants.femaleGender]

worldInhabitantHistory = []

commandRepetition = 0

def runInput(message):
    if len(scripting.inputsToProcess) > 0:
        print(message + scripting.inputsToProcess[0])

        return scripting.inputsToProcess.pop(0)
    else:
        return input(message)

try:
    while True:
        if commandRepetition == 0:
            command = runInput("Evosim > ").lower().strip()

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

            newHistoryEntry = {
                "total": totalInhabitants,
                "properties": {}
            }

            for propertyObject in propertySet:
                newHistoryEntry["properties"][propertyObject.label] = {
                    "adoption": 0,
                    "expression": 0
                }

                for inhabitant in world.inhabitants:
                    hasAdoption = False

                    for propertyPair in inhabitant.propertyPairs:
                        if propertyPair.firstProperty == propertyObject or propertyPair.secondProperty == propertyObject:
                            hasAdoption = True
                        
                    if propertyObject in inhabitant.expressedProperties:
                        hasAdoption = True
                        newHistoryEntry["properties"][propertyObject.label]["expression"] += 1

                    if hasAdoption:
                        newHistoryEntry["properties"][propertyObject.label]["adoption"] += 1
            
            worldInhabitantHistory.append(newHistoryEntry)
        elif command == "exit":
            # Exit Evosim

            print("Goodbye")
            
            exit()
        elif command == "help":
            # Display help information

            helpfile = open("README.md", "r")

            print(helpfile.read())

            helpfile.close()
        elif command == "run script":
            # Run a script

            filename = runInput("Filename of script to run? (Leave blank to cancel) > ")

            if filename != "":
                try:
                    scripting.processScript("scripts/" + filename)

                    print("Loaded script")
                except IOError:
                    print("Could not run script (filename may be incorrect)!")
        elif command == "repeat":
            # Repeat command

            try:
                command = runInput("Command to repeat? (Type '#' to cancel) > ")

                if command != "#":
                    commandRepetition = int(runInput("Number of times to repeat command? (Leave blank to cancel) > ")) + 1
            except:
                pass
        elif command == "new property":
            # New property

            propertyLabel = runInput("New property's label? (Leave blank to generate) > ")
            propertyIsDominant = runInput("Is property dominant? [y/N] > ").lower() == "y"

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

            inhabitantLabel = runInput("New inhabitant's label? (Leave blank to generate) > ")

            inhabitantPropertyPairs = []
            firstPropertyLabel = "-"
            secondPropertyLabel = "-"

            while firstPropertyLabel != "":
                firstPropertyLabel = runInput("First property label in property pair? (Leave blank to exit listing) > ")

                if firstPropertyLabel != "":
                    secondPropertyLabel = runInput("Second property label in property pair? > ")

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
                firstPropertyLabel = runInput("First property label in property pair? (Leave blank to exit listing) > ")

                if firstPropertyLabel != "":
                    secondPropertyLabel = runInput("Second property label in property pair? > ")

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
                for i in range(0, int(runInput("Number of inhabitants to create? (Leave blank to cancel) > "))):
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

            inhabitantLabel = runInput("Label of inhabitant to inspect? (Leave blank to cancel) > ")

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

            conditionLabel = runInput("New condition's label? (Leave blank to generate) > ")
            affectingPropertyLabel = runInput("Affecting property's label? (Leave blank to cancel) > ")

            try:
                decay = int(runInput("Decay length? (Leave blank for 5) > "))
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

            propertyLabel = runInput("Property label to use in calculation? (Leave blank to cancel) > ")

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
        elif command == "export inhabitant history to json":
            # Export the world's inhabitant history to a JSON file

            filename = runInput("Filename to export to? (Leave blank to cancel) > ")

            if filename != "":
                try:
                    if not os.path.exists("exports"):
                            os.makedirs("exports")
                    
                    file = open(os.path.join("exports", *filename.split("/")), "w")
                        
                    file.write(json.dumps({"data": worldInhabitantHistory}))
                    file.close()

                    print("Written export to exports/" + str(filename))
                except:
                    print("Could not write export!")
        elif command == "graph inhabitant history":
            # Graph the world's inhabitant history to a file

            filename = runInput("Filename to graph to? (Leave blank to cancel) > ")

            if filename != "":
                try:
                    width = 1

                    try:
                        width = int(runInput("Width condensation of graph data? (Leave blank for 1) > "))
                    except:
                        pass

                    graphHeading = []
                    graphData = []

                    for tickcount in range(0, len(worldInhabitantHistory)):
                        graphX = list((" " * (worldInhabitantHistory[tickcount]["total"] // width)) + "  ")

                        if len(graphHeading) < ((worldInhabitantHistory[tickcount]["total"] // width) + 10):
                            graphHeading = list((" " * (worldInhabitantHistory[tickcount]["total"] // width)) + "          ")

                        for propertyLabel in worldInhabitantHistory[tickcount]["properties"]:
                            propertyRepresentation = propertyLabel[0]

                            graphX[(worldInhabitantHistory[tickcount]["properties"][propertyLabel]["adoption"]) // width] = propertyRepresentation
                            graphX[(worldInhabitantHistory[tickcount]["properties"][propertyLabel]["adoption"] + 1) // width] = "'"
                            graphX[(worldInhabitantHistory[tickcount]["properties"][propertyLabel]["expression"]) // width] = propertyRepresentation

                        graphX[(worldInhabitantHistory[tickcount]["total"]) // width] = "*"

                        for tally in range(0, worldInhabitantHistory[tickcount]["total"]):
                            if tally % (10 * width) == 0:
                                for letter in range(0, len(str(tally))):
                                    graphHeading[(tally // width) + letter] = str(tally)[letter]

                        graphData.append("".join(graphX)[1:])

                    if not os.path.exists("graphs"):
                        os.makedirs("graphs")
                    
                    file = open(os.path.join("graphs", *filename.split("/")), "w")
                    
                    file.write(("".join(graphHeading[1:])) + "\n" + ("\n".join(graphData)))
                    file.close()

                    print("Written graph to graphs/" + str(filename))
                except:
                    print("Could not write graph!")
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