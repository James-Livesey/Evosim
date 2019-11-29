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
    print(len(world.inhabitants))

    world.tick()

    time.sleep(1)