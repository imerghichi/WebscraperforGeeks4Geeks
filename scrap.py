from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "http://www.geeksforgeeks.org/"
driver = webdriver.Firefox("/driver/geckodriver")
titles =[] #where to store titles of articles
links = [] #where to store contents of the articles
descriptions = [] #where to store descriptions of the articles
ratings = []

driver.get(BASE_URL)
contenu = driver.page_source
soup = BeautifulSoup(contenu)
for a in soup.findAll('a', href=True, attributs ={ 'class' : 'article'}):
    title = a.find ('h2', attributs = {'class':'entry-title'})
    link = a.find ('div', attributs= {'class': 'divclass'})
    description = a.find('div', attributs = {'class' : 'entry-summary'})
    rating = a.find('span', attributs = {'class' : 'articleRating alignright level-3'})
    titles.append(title.text)
    links.append(link.text)
    descriptions.append(description.text)
    ratings.append(rating.text)

data_to_stock = pd.DataFrame({'Title' : titles, 'Links' : links , 'Descriptions' : descriptions , 'Ratings' : ratings})
data_to_stock.to_excel("data.xls" , encoding= 'utf-8') #to support accents may be, even if the website is in English
