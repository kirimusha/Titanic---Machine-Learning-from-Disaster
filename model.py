import pandas as pd

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train.head(10)

# train.info()

train.isnull().sum()

train.describe()
