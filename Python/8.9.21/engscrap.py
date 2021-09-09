from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.cricbuzz.com/live-cricket-scorecard/32052/eng-vs-ind-2nd-test-india-tour-of-england-2021")

soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())
k = 0
for j in range(0,7):
    if j==0 or j==4:
       tbl = soup.find_all("div",class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[j]
# print(tbl.prettify())

       names = [x.get_text() for x in tbl.find_all('div',class_="cb-col cb-col-27")]
# print(names)
       players=[]
       for i in names:
           players.append(i.upper().strip())
       print(players)

       runs = [x.get_text() for x in tbl.find_all('div', class_="cb-col cb-col-8 text-right text-bold")]
       player_runs = runs[1:]
       # print(player_runs)
       x = input("Enter the Player Name:")
       x = x.upper()
       # print(x)
       for i in range(0, len(names)):
           if x == players[i]:
               print(f"\nThe player name is {names[i]}\n")
               print(f"Runs scored in  innings {k + 1} is : {player_runs[i]}")
               k = k + 1