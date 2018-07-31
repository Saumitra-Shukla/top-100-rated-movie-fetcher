from bs4 import BeautifulSoup
from urllib.request import urlopen
print('''Enter any year from 1950 to current year
 and get top 100 movies with ranking according to critics ratings
 ratings are subject to blogs/major critics like imdb metacritic and rotten tomatoes all over the internet
 to get a list of best movies of all time enter 0''')
strr=input("input year : ")
url='https://www.rottentomatoes.com/top/bestofrt/?year='+strr
if str=='0':
    url='https://www.rottentomatoes.com/top/bestofrt/'
client=urlopen(url)
page_html=client.read()
soup=BeautifulSoup(page_html,'html.parser')
client.close()
containe=soup.find('table',class_='table')
movie_names=containe.find_all(class_='unstyled articleLink')
j=0
for i in movie_names:
    j=j+1
    k=str(j)
    print(k+".)"+i.string,end=' ')
    print("")
