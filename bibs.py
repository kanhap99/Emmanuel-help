import pandas as pd
import re

df = pd.read_csv('originalData.csv')  
pos = 0
 
for i in range(len(df)):
  try:
    pattern = bool(re.search(r'\ -\ c\d',df.Title[i][-5:])) 
    if not pattern:
      pos = i
    elif pattern:
      df.Item[pos] += df.Item[i]
      df = df[df.Title != df.Title[i]] 
  except:
    print i
    continue
df.to_csv('bibs.csv')

