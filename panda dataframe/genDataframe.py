import pandas as pd
import numpy as np

column = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

indexed = ['n1l', 'by73', 'emy', 'ety']

array = np.random.randn(4,7) #rows, columns (indexed, column)

data = pd.DataFrame(array, index=indexed, columns=column)

print(data)