from bs4 import BeautifulSoup
import requests
import pandas as pd

url= "https://imsnsit.org/imsnsit/notifications.php"

page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")

data = soup.find_all("tr")
tableOfTitles = [title.text for title in data]
df = pd.DataFrame(tableOfTitles)
print(df)
for i in df[1:]:
    if i ==['']:
        continue
    else: 
        length=len(df)
        df.loc[length]=tableOfTitles
        df=df.to_csv(r'data.csv')

