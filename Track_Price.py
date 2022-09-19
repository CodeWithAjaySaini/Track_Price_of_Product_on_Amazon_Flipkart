#  Track_Price.py

import requests
from bs4 import BeautifulSoup

def find_price(URL):
    r=requests.get(URL,headers={'User-Agent':'Defined'})
    soup= BeautifulSoup(r.content,'html.parser')
    try:
        if 'amazon' in URL:
            item1=soup.find(class_='a-offscreen') #Price of Product
            item2=soup.find(id='productDetails_techSpec_section_1') #Product details
            price=[item1,item2]
            return price
            
            
        elif 'flipkart' in URL:
            item1=soup.find(class_='_30jeq3 _16Jk6d')#Price of Product
            item2=soup.find(class_='_1UhVsV') #Product details
            price=[item1,item2]
            
            return price
    
    except:
        return

URL= input("Enter The URL: ")
price= find_price(URL)

if price == None:
    price("Invalid")
else:
    for item in price:
        
        print(item.get_text())     

 