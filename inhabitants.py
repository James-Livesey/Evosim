import random

import properties

maleGender = properties.Property(False)
femaleGender = properties.Property(False)

MALE = 0
FEMALE = 1

class Inhabitant:
    def __init__(self, passedPropertyPairs):
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
        self.decay = random.randint(0, 100)

    def reproduce(self, malePartner):
        if self.gender == FEMALE:
            # Only females can make offspring

            if random.randint(0, 4) == 0:
                # The inhabitant must consent in order to reproduce

                if malePartner.fertility > 0:
                    # The male partner must also be fertile

                    self.fertility -= 1
                    malePartner.fertility -= 1

                    passedPropertyPairs = []

                    for propertyID in range(0, len(self.propertyPairs)):
                        if random.randint(0, 1) == 1:
                            passedPropertyPairs.append(properties.PropertyPair(
                                self.propertyPairs[propertyID].firstProperty,
                                malePartner.propertyPairs[propertyID].secondProperty
                            ))
                        else:
                            passedPropertyPairs.append(properties.PropertyPair(
                                self.propertyPairs[propertyID].secondProperty,
                                malePartner.propertyPairs[propertyID].firstProperty
                            ))

                    return Inhabitant(passedPropertyPairs)
                else:
                    return None
            else:
                return None
        else:
            return None