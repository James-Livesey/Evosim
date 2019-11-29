import random

import inhabitants

conditionIterator = 0

class Environment:
    def __init__(self):
        self.inhabitants = []
        self.conditions = []

    def tick(self):
        self.useConditions()
        self.decayConditions()

        self.decayInhabitants()
        self.reproduceInhabitants()

    def useConditions(self):
        for condition in self.conditions:
            for inhabitantID in range(0, len(self.inhabitants)):
                if condition.affectingProperty in self.inhabitants[inhabitantID].expressedProperties:
                    # Inhabitant dies due to condition

                    print("Inhabitant " + str(self.inhabitants[inhabitantID].label) + " died due to condition " + condition.label)

                    self.inhabitants[inhabitantID] = None

            self.inhabitants = [inhabitant for inhabitant in self.inhabitants if inhabitant is not None]

    def decayConditions(self):
        for conditionID in range(0, len(self.conditions)):
            self.conditions[conditionID].decay -= 1

            if self.conditions[conditionID].decay == 0:
                # Condition has fully decayed

                print("Condition " + str(self.conditions[conditionID].label) + " decayed")

                self.conditions[conditionID] = None

        self.conditions = [condition for condition in self.conditions if condition is not None]                

    def decayInhabitants(self):
        for inhabitantID in range(0, len(self.inhabitants)):
            self.inhabitants[inhabitantID].decay -= 1

            if self.inhabitants[inhabitantID].decay == 0:
                # Inhabitant dies due to old age

                print("Inhabitant " + str(self.inhabitants[inhabitantID].label) + " decayed")

                self.inhabitants[inhabitantID] = None

        self.inhabitants = [inhabitant for inhabitant in self.inhabitants if inhabitant is not None]        

    def reproduceInhabitants(self):
        # Split the inhabitants into two seperate genders before they reproduce

        maleInhabitants = []
        femaleInhabitants = []

        for inhabitant in self.inhabitants:
            if inhabitant.gender == inhabitants.MALE:
                maleInhabitants.append(inhabitant)

            if inhabitant.gender == inhabitants.FEMALE:
                femaleInhabitants.append(inhabitant)

        # Shuffle inhabitant arrays otherwise oldest inhabitants will be selected first, and they may have low fertility

        random.shuffle(maleInhabitants)
        random.shuffle(femaleInhabitants)

        # Start reproduction

        while len(femaleInhabitants) != 0 and len(maleInhabitants) != 0:
            mother = femaleInhabitants[0]
            father = maleInhabitants[0]

            offspring = mother.reproduce(father)

            maleInhabitants.pop(0)
            femaleInhabitants.pop(0)

            if isinstance(offspring, inhabitants.Inhabitant):
                self.inhabitants.append(offspring)

                print("Inhabitants " + str(mother.label) + " and " + str(father.label) + " reproduced to make new inhabitant " + str(offspring.label))

class Condition:
    def __init__(self, affectingProperty, decay = 5):
        global conditionIterator

        self.affectingProperty = affectingProperty
        self.decay = decay

        self.label = "C_" + str(conditionIterator) + "_" + self.affectingProperty.label
        conditionIterator += 1