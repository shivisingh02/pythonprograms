import requests 
from bs4 import BeautifulSoup
import os
import pandas as pd 
import datetime

def get_soup(url):
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text)
    return None

def get_products(soup):
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text)
    return None

def get_products(soup):
    target = soup.find('div' , class_ = '_1YokD2 _3Mn1Gg')
    if target is not None:
        items = target.find_all('div' , class_ = '_1AtVbE col-12-12')
        print(f'found {len(items)} items')
        return items
     
def extract_one(item):
    data = {}
    title = item.find('div' , class_ = "_4rR01T")
    sell_price = item.find('div' , class_ = '_30jeq3 _1_WHN1')
    orig_price = item.find('div' , class_ = '_3I9_wc _27UcVY')
    rating = item.find('div' , class_= '_3LWZlK')
    num_ratings = item.find('div' , class_ ='_2_R_DZ')
    if title:
        data['title'] =title.text.strip()
    if orig_price:
        data['orig_price'] = orig_price.text.strip()
    if sell_price:
        data[sell_price] = sell_price.text.strip()
    if rating:
        data[rating] =rating.text.strip()
    if num_ratings:
        data[num_ratings] = num_ratings.text.strip()
    return data

def main(query = 'tv'):
    base_url = 'https://www.flipkart.com/search'
    pos = 1 
    all_products = []
    while True:
        url = f'{base_url}?q ={query}&page ={pos}'
        print(url)
        soup = get_soup(url)
        if soup is None:
            print('no data found')
            break
        items = get_products(soup)
        if len(items) == 0:
            break 
        for item in items:
            data = extract_one(item)
            all_products.append(data)
        pos += 1 
    if len(all_products) > 0 :
        time = datetime.datetime.now().strftime("%Y%m%d_%H%S")
        pd.DataFrame(all_products).to_csv(f'flipkart_{query}_{time}.csv', index = False)
        
if __name__ == '__main__':
    main("tv")




