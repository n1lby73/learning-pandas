import pandas as pd
import random

createSeries = []

newSeries = []

index = []

newIndex = []

#loop to create custom index

for i in range(65,91):

    index.append(i)

for i in range(97,104):

    index.append(i)

#loop to create random data as a list

for i in range(1,34):
        
    createSeries.append(random.randint(1,34))


for i in range(1,12):

    if i <= 9:

        newSeries.append(random.randint(1,34))

    else:

        newSeries.append(random.randint(1,34))

#adding index results in all output as NaN

emyData = pd.Series(createSeries)
etyData = pd.Series(newSeries)

#multiplying data

data = emyData.mul(etyData)

print(data)