import inhabitants

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

                    self.inhabitants[inhabitantID] = None

            self.inhabitants = [inhabitant for inhabitant in self.inhabitants if inhabitant is not None]

    def decayConditions(self):
        for conditionID in range(0, len(self.conditions)):
            self.conditions[conditionID].decay -= 1

            if self.conditions[conditionID].decay == 0:
                # Condition has fully decayed

                self.conditions[conditionID] = None

        self.conditions = [condition for condition in self.conditions if condition is not None]                

    def decayInhabitants(self):
        for inhabitantID in range(0, len(self.inhabitants)):
            self.inhabitants[inhabitantID].decay -= 1

            if self.inhabitants[inhabitantID].decay == 0:
                # Inhabitant dies due to old age

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

        # Start reproduction

        while len(femaleInhabitants) != 0 and len(maleInhabitants) != 0:
            offspring = femaleInhabitants[0].reproduce(maleInhabitants[0])

            maleInhabitants.pop(0)
            femaleInhabitants.pop(0)

            if isinstance(offspring, inhabitants.Inhabitant):
                self.inhabitants.append(offspring)

class Condition:
    def __init__(self, affectingProperty, decay = 5):
        self.affectingProperty = affectingProperty
        self.decay = decay