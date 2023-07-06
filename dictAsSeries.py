import pandas as pd

createSeries = {}

key = 1

classNumber = 1

#loop to create dynamic dictionary

while key <= 33:

    createSeries[key]= "EMY-c"+ str(classNumber)

    key += 1
    classNumber += 1

print (pd.Series(createSeries))
