#Import csv dataset from github
import requests
import pandas as pd

url = 'https://raw.githubusercontent.com/adaltas/dsti-mlops-2022-autumn/main/10.monitoring/lab-resources/train.csv'
res = requests.get(url, allow_redirects=True)
with open('train.csv', 'wb') as file:
    file.write(res.content)
train = pd.read_csv('train.csv')