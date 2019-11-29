import time

import environment
import inhabitants
import properties

# Test to see if inhabitants can live

world = environment.Environment()

brownEyeProperty = properties.Property(True)
blueEyeProperty = properties.Property(False)

world.inhabitants = []

for i in range(0, 20):
    world.inhabitants.append(inhabitants.Inhabitant([
        properties.PropertyPair(inhabitants.maleGender, inhabitants.femaleGender),
        properties.PropertyPair(blueEyeProperty, blueEyeProperty)
    ]))

while True:
    total = len(world.inhabitants)
    males = 0
    females = 0

    for inhabitant in world.inhabitants:
        if inhabitant.gender == inhabitants.MALE:
            males += 1

        if inhabitant.gender == inhabitants.FEMALE:
            females += 1 

    print("Total:", len(world.inhabitants), "Males:", males, "Females:", females)

    world.tick()

    time.sleep(1)