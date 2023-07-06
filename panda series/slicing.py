import pandas as pd

createSeries = []

index = []

user = int(input("\nHow many values do you want to slice: "))

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


data = pd.Series(createSeries, index=index)

#Slicing

print("\nFirst {} values of the data:\n".format(user))

print (data[:user])

print("\nOmiting last {} values of the data:\n".format(user))

print (data[:-user])

print("\nFirst {} values of the data from behind:\n".format(user))

print (data[-user:])