from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.cricbuzz.com/live-cricket-scorecard/32052/eng-vs-ind-2nd-test-india-tour-of-england-2021")

soup = BeautifulSoup(page.text,"html.parser")
k = 0
for j in range(0,7):
    if j==2 or j==6:
        tbl = soup.find_all("div",class_="cb-col cb-col-100 cb-ltst-wgt-hdr")
# print(tbl.prettify())

        names = [x.get_text() for x in tbl.find_all("div",class_="cb-col cb-col-27")]
# print(names)
        header=[]
        for i in names:
            header.append(i.upper().strip())
        print(header)

        runs = [x.get_text() for x in tbl.find_all('div', class_="cb-col cb-col-8 text-right text-bold")]
        player_runs = runs[1:]
        #print(player_runs)
        x = input("enter the player name:")
        x = x.upper()
        # print(x)
        for i in range(0, len(names)):
            if x == header[i]:
                print(f"The player name is {names[i]} ")
                print(f"Runs scored in {k + 1} innings :{player_runs[i]}")
                k = k + 1




