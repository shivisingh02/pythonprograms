
from bs4 import BeautifulSoup
import requests
import lxml
import streamlit as st

def get_charts_page():
    URL = ('https://www.billboard.com/charts/india-songs-hotw/')
    r = requests.get(URL)
    return  BeautifulSoup(r.content, 'lxml')

def get_news_page():
    url = "https://www.billboard.com/c/culture/"
    r = requests.get(url)
    return  BeautifulSoup(r.content, 'lxml')


def collect_data(doc):

    data = []
    songs = doc.find_all('div', class_='o-chart-results-list-row-container')
    f = open('Billboard_Hot_100.txt', 'w+')
    f.write('BILLBOARD HOT 100\n')
    for i,item in enumerate(songs):
        title = item.find('h3').text.strip()
        singer =item.find('span', class_='c-label').text
        data.append({
            'title':f'{i}. {title}',
            'singer':singer
        })
        f.write(f'{i}. {title}\n')
    f.close()
    return data
    
def collect_news(doc2):
    data = []
    news = doc2.find_all('div', class_="story")
    
    for i,item in enumerate(news):
        title = item.find('h3').text.strip()
        try:
            link = item.find('h3').find('a').attrs.get('href')
            # st.write(link)
        except: link='https://www.billboard.com/c/culture/'
        data.append({
            'title':f'{i}. {title}', 
            'link': link
        })
    # st.write(data)
    return data


st.image('https://upload.wikimedia.org/wikipedia/commons/2/2b/Billboard_Hot_100_logo.jpg')
st.title("Billboard Scraper")
st.sidebar.image("https://i.scdn.co/image/ab67616d0000b273c08202c50371e234d20caf62")
btn = st.sidebar.button("collect songs")
btn2 = st.sidebar.button("collect news")
if btn:
    st.info("Top Indian Songs on Billboard")
    doc = get_charts_page()
    out = collect_data(doc)
    for s in out:
        st.markdown(f'''
        🎵{s.get('title')} 
        ''', unsafe_allow_html=True)
if btn2:
    st.info("Latest news from billboard")
    doc2 = get_news_page()
    out = collect_news(doc2)
    for s in out:
        st.markdown(f'''
        ##### 📰- {s.get('title')} 
        <a href="{s.get('link')}" target="blank">Read</a>
        ''', unsafe_allow_html=True)
    


# streamlit run billboard.py