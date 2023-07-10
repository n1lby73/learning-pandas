import pandas as pd

efile = pd.read_excel('students.xlsx')

print(efile[1:])