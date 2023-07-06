import pandas as pd

createSeries = []

newSeries = []

index = []

newIndex = []

#loop to create custom index

for i in range(65,91):

    index.append(chr(i))

for i in range(97,104):

    index.append(chr(i))

#loop to create random data as a list

for i in range(1,34):

    if i <= 9:

        createSeries.append("EMY-c0"+ str(i))

    else:

        createSeries.append("EMY-c"+ str(i))


for i in range(1,12):

    if i <= 9:

        newSeries.append("ETY-c0"+ str(i))

    else:

        newSeries.append("ETY-c"+ str(i))


emyData = pd.Series(createSeries, index=index)
etyData = pd.Series(newSeries)

#appending data

data = emyData._append(etyData)

print(data)