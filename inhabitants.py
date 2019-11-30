import random

import properties

inhabitantIterator = 0

maleGender = properties.Property(False)
femaleGender = properties.Property(False)

maleGender.label = "male"
femaleGender.label = "female"

MALE = 0
FEMALE = 1

class Inhabitant:
    def __init__(self, birthtick, passedPropertyPairs):
        global inhabitantIterator

        self.birthtick = birthtick

        self.propertyPairs = passedPropertyPairs
        self.expressedProperties = []
        
        for propertyPair in self.propertyPairs:
            self.expressedProperties.append(propertyPair.dominantProperty)

        self.gender = None

        for propertyObject in self.expressedProperties:
            if propertyObject is maleGender:
                self.gender = MALE
            
            if propertyObject is femaleGender:
                self.gender = FEMALE

        self.fertility = random.randint(0, 5)
        self.decay = random.randint(1, 100)

        if self.gender == MALE:
            self.label = "I_" + str(inhabitantIterator) + "_M"
        elif self.gender == FEMALE:
            self.label = "I_" + str(inhabitantIterator) + "_F"
        else:
            self.label = "I_" + str(inhabitantIterator)

        inhabitantIterator += 1

    def reproduce(self, malePartner, birthtick):
        if self.gender == FEMALE:
            # Only females can make offspring

            if random.randint(0, 4) == 0:
                # The inhabitant must give consent in order to reproduce

                if malePartner.fertility > 0 and self.fertility > 0:
                    # The male and female partners must be fertile

                    self.fertility -= 1
                    malePartner.fertility -= 1

                    passedPropertyPairs = []

                    for propertyID in range(0, min(len(self.propertyPairs), len(malePartner.propertyPairs))):
                        firstProperty = None
                        secondProperty = None

                        if random.randint(0, 1) == 1:
                            firstProperty = self.propertyPairs[propertyID].firstProperty
                        else:
                            firstProperty = self.propertyPairs[propertyID].secondProperty

                        if random.randint(0, 1) == 1:
                            secondProperty = malePartner.propertyPairs[propertyID].firstProperty
                        else:
                            secondProperty = malePartner.propertyPairs[propertyID].secondProperty

                        passedPropertyPairs.append(properties.PropertyPair(firstProperty, secondProperty))

                    return Inhabitant(birthtick, passedPropertyPairs)
                else:
                    return None
            else:
                return None
        else:
            return None