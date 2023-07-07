import pandas as pd

user1 = int(input("where do you want to start viewing from(0 to start from the very first): "))

user2 = int(input("what's your setpoint: "))


values = {
            'eqpkl': [24, 1, 47, 17, 88, 56, 75, 37, 61, 72],
            'irmei': [50, 45, 95, 35, 40, 41, 6, 5, 100, 91],
            'qayzr': [89, 90, 14, 39, 77, 57, 46, 81, 15, 49],
            'kfpry': [92, 17, 46, 73, 22, 62, 67, 36, 67, 15],
            'pqbis': [48, 63, 60, 10, 50, 43, 94, 80, 8, 90]
        }

heading = ['odlcygipnu', 'vjwdnhkabs', 'emvysnflpj', 'qrzlepvksa', 'ofzkbgthxr', 'vyxhlfmiqz', 'bfmreolcjk', 'wmtgaeyvfl', 'dbrplnoezy', 'zfjodvltpu']

data = pd.DataFrame(values, index=heading)

print(data[user1:user2])

print('\n----------------------combined sort and slicing----------------------------\n')

print(data.sort_values(by="eqpkl")[user1:user2])