import pandas as pd

banks = pd.read_csv('banking.csv')
age = banks.loc[:, 'age']
trueage = age > 50
palash_age_banks = banks[trueage]

print(palash_age_banks)
