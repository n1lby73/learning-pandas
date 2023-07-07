import pandas as pd
import numpy as np

values = {
            'eqpkl': [24, 1, np.nan, 17, 88, 56, 75, 37, 61, 72],
            'irmei': [50, 45, 95, 35, 40, 41, 6, 5, 100, 91],
            'qayzr': [89, 90, 14, 39, 77, 57, np.nan, 81, 15, 49],
            'kfpry': [92, 17, np.nan, 73, 22, 62, 67, 36, 67, 15],
            'pqbis': [48, 63, 60, 10, 50, 43, 94, 80, 8, 90]
        }

heading = ['odlcygipnu', 'vjwdnhkabs', 'emvysnflpj', 'qrzlepvksa', 'ofzkbgthxr', 'vyxhlfmiqz', 'bfmreolcjk', 'wmtgaeyvfl', 'dbrplnoezy', 'zfjodvltpu']

data = pd.DataFrame(values, index=heading)

print (data.isnull())