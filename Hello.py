import streamlit as st
import requests
import numpy as np
from bs4 import BeautifulSoup

# 获取北京数据的函数
def get_bjnews_data():
    url = "https://jwc.cuc.edu.cn/6364/list.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    bj_list = soup.find("ul", class_="news_list list2").find_all("li")
    bj_news = []
    for list in bj_list[0:]:
        news_date = list.find('span', class_='news_meta').get_text()
        news_name = list.find('span', class_='news_title').get_text()
        news_link = list.find('span', class_='news_title').find('a').get('href')
        bj_news.append((news_date, news_name,news_link))
    return bj_news

# 获取海南数据的函数
def get_hnnews_data():
    url = "https://hainan.cuc.edu.cn/main.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    hn_list = soup.find("div", class_="post post1 post-21 mbox").find_all("li")
    hn_news = []
    for list in hn_list[0:]: 
        news_date = list.find('span', class_='news_meta').get_text()
        news_name = list.find('span', class_='news_title').get_text()
        news_link = list.find('span', class_='news_title').find('a').get('href')
        hn_news.append((news_date, news_name,news_link))
    return hn_news

# 获取下载数据的函数
def get_dlnews_data():
    url = "https://jwc.cuc.edu.cn/6366/list1.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    dl_list = soup.find("ul", class_="news_list list2").find_all("li")
    dl_news = []
    for list in dl_list[0:]: 
        news_date = list.find('span', class_='news_meta').get_text()
        news_name = list.find('span', class_='news_title').get_text()
        news_link = list.find('span', class_='news_title').find('a').get('href')
        dl_news.append((news_date, news_name,news_link))
    return dl_news
# 获取下载数据的函数2
def get_dl2news_data():
    url = "https://jwc.cuc.edu.cn/6366/list2.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    dl2_list = soup.find("ul", class_="news_list list2").find_all("li")
    dl2_news = []
    for list in dl2_list[0:]: 
        news_date = list.find('span', class_='news_meta').get_text()
        news_name = list.find('span', class_='news_title').get_text()
        news_link = list.find('span', class_='news_title').find('a').get('href')
        dl2_news.append((news_date, news_name,news_link))
    return dl2_news
# 获取下载数据的函数3
def get_dl3news_data():
    url = "https://jwc.cuc.edu.cn/6366/list3.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    dl3_list = soup.find("ul", class_="news_list list2").find_all("li")
    dl3_news = []
    for list in dl3_list[0:]: 
        news_date = list.find('span', class_='news_meta').get_text()
        news_name = list.find('span', class_='news_title').get_text()
        news_link = list.find('span', class_='news_title').find('a').get('href')
        dl3_news.append((news_date, news_name,news_link))
    return dl3_news

# 将北京数据显示在网站上的函数
def display_bjnews_data(bj_news):
    for i in range(len(bj_news)):
        st.write(f"<li>{bj_news[i][0]}<a href='https://jwc.cuc.edu.cn/{bj_news[i][2]}'>{bj_news[i][1]}</a></li>", unsafe_allow_html=True)

# 将海南数据显示在网站上的函数
def display_hnnews_data(bj_news):
    for i in range(len(bj_news)):
        st.write(f"<li>{bj_news[i][0]}<a href='https://hainan.cuc.edu.cn{bj_news[i][2]}'>{bj_news[i][1]}</a></li>", unsafe_allow_html=True)

# 将下载数据显示在网站上的函数
def display_dlnews_data(dl_news):
    for i in range(len(dl_news)):
        st.write(f"<li>{dl_news[i][0]}<a href='https://hainan.cuc.edu.cn{dl_news[i][2]}'>{dl_news[i][1]}</a></li>", unsafe_allow_html=True)
# 将下载数据显示在网站上的函数2
def display_dl2news_data(dl2_news):
    for i in range(len(dl2_news)):
        st.write(f"<li>{dl2_news[i][0]}<a href='https://hainan.cuc.edu.cn{dl2_news[i][2]}'>{dl2_news[i][1]}</a></li>", unsafe_allow_html=True)
# 将下载数据显示在网站上的函数3
def display_dl3news_data(dl3_news):
    for i in range(len(dl3_news)):
        st.write(f"<li>{dl3_news[i][0]}<a href='https://hainan.cuc.edu.cn{dl3_news[i][2]}'>{dl3_news[i][1]}</a></li>", unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config="Hello"
    st.write("# Welcome to Phoebe\' CUC")

    with st.sidebar:
        st.write('## Coming soon!')
        st.write('_Please expecting!_')
        # message = st.chat_message("user")
        # message.write("Hello human")
        # message.bar_chart(np.random.randn(30, 3))
    st.markdown(
         """
    _Where there is a will, there is a way._ 🎈i

    ### Official Website
    - Communication University of China [Beijing](http://www.cuc.edu.cn/)
    - Hainan International College of CUC [Hainan](https://hainan.cuc.edu.cn/)
    - Coventry University [UK](https://www.coventry.ac.uk/)
    ### Common System Links
    - Query grades [Unify Identity Authentication System](https://sso.cuc.edu.cn/authserver/login)
    - Course selection [Course selection system](https://xsxk.cuc.edu.cn/xsxkapp/sys/xsxkapp/*default/index.do)
    - Online classroom [TronClass](http://courses.cuc.edu.cn/public-course)
"""
    )
    col1,col2=st.columns(2)
    with col1:
        st.write("## Beijing")
        bj_news = get_bjnews_data()
        display_bjnews_data(bj_news)
    with col2:
        st.write("## International")
        hn_news = get_hnnews_data()
        display_hnnews_data(hn_news)
    
    st.write("## Download")
    col1,col2,col3=st.columns(3)
    with col1:
        dl_news = get_dlnews_data()
        display_dlnews_data(dl_news)
    with col2:
        dl2_news = get_dl2news_data()
        display_dl2news_data(dl2_news)
    with col3:
        dl3_news = get_dl3news_data()
        display_dl3news_data(dl3_news)
