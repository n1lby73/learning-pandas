import pandas as pd

createSeries = []

index = []

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

emyData = pd.Series(createSeries, index=index)

#drop data

data = emyData.drop('A')

print(data)