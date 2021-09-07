import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.nfl.com/standings/league/2020/reg/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
print(soup)

table = soup.find('table', {'summary':'Standings - Detailed View'})

headers = []
for i in table.find_all('th'):
     title = i.text.strip()
     headers.append(title)

df = pd.DataFrame(columns = headers)
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data


col = df.columns
print(col)
for i in col:
    for j in df[i]:
        print("original : {0} , Data type : {1}" .format(j,type(j)))










