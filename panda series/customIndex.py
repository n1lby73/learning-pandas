import pandas as pd

createSeries = []

index = []

#loop to create custom index

for i in range(1,34):

    index.append(i)

#loop to create random data as a list

for i in range(1,34):

    createSeries.append("EMY-c"+ str(i))

print (pd.Series(createSeries, index=index))
