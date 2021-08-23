import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
os.getcwd()



url='https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
response = requests.get(url)
soup =BeautifulSoup(response.content,'html.parser')
movie_name=[]
year=[]
time=[]
rating=[]
metascore=[]
votes=[]
gross=[]
movie_data= soup.findAll('div',attrs={'class':'lister-item mode-advanced'})

for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)
    
    year_of_release = store.h3.find('span',class_='lister-item-year text-muted unbold').text.replace('(','').replace(')','')
    year.append(year_of_release)
    
    runtime = store.p.find('span',class_='runtime').text.replace(' min','')
    time.append(runtime)
    
    rate = store.find('div',class_='inline-block ratings-imdb-rating').text.replace('\n','')
    rating.append(rate)

movie_DF = pd.DataFrame({'Name of movie':movie_name,'Year of release': year,'Watchtime': time,'Movie Rating':rating})
print(movie_DF)

df = pd.DataFrame(movie_DF)
df.to_excel('movie.xlsx',sheet_name='movie_rating')
