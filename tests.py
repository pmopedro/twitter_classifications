import twint
import pandas as pd 

politicians = pd.read_csv('politicians.csv')

print(politicians['twitter_acount'])

for account in politicians.twitter_acount:
    c = twint.Config()

    c.Username = account
    c.Store_csv = True
    c.Output = "politician/"

    twint.run.Search(c)