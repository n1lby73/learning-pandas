import pandas as pd

createSeries = []

indexValue = []

newIndex = []

letters = 97 #ASCII value for lowercase alphabet starts from 97 while uppercase starts from 65

#Loop for old custom indexValue format

for i in range(1,34):

    indexValue.append(i)

#loop to create new custom indexValue

for i in range(1,34):

    if i <= 7:

        newIndex.append(i)

    else:

        newIndex.append(chr(letters))
        letters += 1

    #Uncomment line 30 - 39 to tilt the indexValue output

    # while letters <= 122:

    #     indexValue.append(chr(letters))
    #     letters += 1

    # if i <= 7:

    #     indexValue.append(i)

#loop to create random data as a list

for i in range(1,34):

    if i <= 9:

        createSeries.append("EMY-c0"+ str(i))

    else:

        createSeries.append("EMY-c"+ str(i))

print ("\n----------------------------------------OLD indexValue--------------------------------------------------\n")
print (pd.Series(createSeries, index=indexValue))

print ("\n----------------------------------------------New indexValue--------------------------------------------------\n")

#modification of indexValue

new = pd.Series(createSeries, index=indexValue)

new.index = newIndex

print (new)