import pandas as pd
df = pd.DataFrame({
     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
     'population': [17.04, 143.5, 9.5, 45.5],
     'square': [2724902, 17125191, 207600, 603628]
 }, index=['KZ', 'RU', 'BY', 'UA'])
df['destiny'] = df['population'] / df['square'] * 1000000

#----
dataf = pd.read_csv('test.csv',sep=',')


print(
    dataf.groupby(['city','section'])[['hitId']].count()
      )

#-----
dataf = pd.read_csv('result.csv',sep=',')
pvt = dataf.pivot_table(index = ['section'], columns=['city'], values='hitId',aggfunc='count')

print(
    pvt.loc['biznes']
      )