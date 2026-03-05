import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Web Scraper")

link = st.text_area("Enter the link to fetch data")

if st.button('Scrape'):
            
            content = requests.get(link)
            response = content.text
            soup = BeautifulSoup(response, 'html.parser')
            data = soup.find_all('tr')
            for i in data:
                    st.write(i.get_text())
        
     
