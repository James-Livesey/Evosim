import random

propertyIterator = 0

class Property:
    def __init__(self, isDominant = False):
        global propertyIterator

        self.isDominant = isDominant

        self.label = "P_" + str(propertyIterator)
        propertyIterator += 1

class PropertyPair:
    def __init__(self, firstProperty, secondProperty):
        self.firstProperty = firstProperty
        self.secondProperty = secondProperty

        if self.firstProperty.isDominant:
            self.dominantProperty = self.firstProperty
        elif self.secondProperty.isDominant:
            self.dominantProperty = self.secondProperty
        elif self.firstProperty == self.secondProperty:
            self.dominantProperty = self.firstProperty
        else:
            if random.randint(0, 1) == 1:
                self.dominantProperty = self.secondProperty
            else:
                self.dominantProperty = self.firstProperty