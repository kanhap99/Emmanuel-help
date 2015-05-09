import pandas as pd
import re

df = pd.read_csv('originalData.csv')  
pos = 0
 
for i in range(len(df)):
  book = df.Title[i] #current book
  pattern = bool(re.search(r'\ -\ c\d',book[-5:])) #duplicate pattern search for last five characters of book title 
  if not pattern:
    pos = i
  elif pattern: 
    df.Item[pos] += df.Item[i] #add item header to original book title
    df = df[df.Title != book] #filter the df so that it doesnt contain the current book
 
df.to_csv('bibs.csv') #upload df results to another csv file

