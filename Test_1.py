Farmernumber = 5
distances = (4,7, 1, 14, 15)
totalDistance = []
smallerDistance = 0
for house1 in range(Farmernumber):
    for house2 in range (Farmernumber):
        if house2 != house1:
            for checkingHouse in range (Farmernumber):
                if checkingHouse!=house1 and checkingHouse!=house2:
                    smallerDistance += (min(max(distances[house1],distances[checkingHouse])-min(distances[house1],distances[checkingHouse]),max(distances[house2],distances[checkingHouse])-min(distances[house2],distances[checkingHouse])))*2
            totalDistance.append(smallerDistance)
            smallerDistance = 0          
print(totalDistance)
print(min(totalDistance))