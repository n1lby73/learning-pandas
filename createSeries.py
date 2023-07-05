import pandas as pd

createSeries = []

#loop to create random data as a list

for i in range(1,34):

    createSeries.append("EMY-c"+ str(i))

print (pd.Series(createSeries))
