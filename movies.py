from bs4 import BeautifulSoup
from urllib.request import urlopen
print('''Enter any year from 1950 to current year
 and get top 100 movies with ranking according to critics ratings
 ratings are subject to blogs/major critics like imdb metacritic and rotten tomatoes all over the internet
 to get a list of best movies of all time enter 0''')
strr=input("input year : ")
url='https://www.rottentomatoes.com/top/bestofrt/?year='+strr
if strr=='0':
    url='https://www.rottentomatoes.com/top/bestofrt/'
client=urlopen(url)
page_html=client.read()
soup=BeautifulSoup(page_html,'html.parser')
client.close()
containe=soup.find('table',class_='table')
movie_names=containe.find_all(class_='unstyled articleLink')
j=0
movie_ratings=containe.find_all('span',class_='tMeterScore')
filename="movies_"+strr+".csv"
f=open(filename,'w')
f.write("S.No, Name , Ratings\n")
for i in range(0,100):

    f.write(str((i+1))+","+movie_names[i].string.strip()+","+movie_ratings[i].string+"\n")
    print('''
    
    
    ''')
    print(str((i+1))+".)"+"Name : "+movie_names[i].string.strip())
    print('')
    print(" Ratings : "+movie_ratings[i].string+"/100",end=' ')

f.close()