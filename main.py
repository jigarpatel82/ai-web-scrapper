import requests
import selenium
import streamlit as st
from scraper import scrape_web, clean_html_content

st.title('AI Webscraper')
url = st.text_input('Enter the website URL')

if st.button('Scrape site'):
    # st.write('Scraping the website...')
    result = scrape_web(url)
    new_result = clean_html_content(result)
    st.expander('DOM content')
    st.text_area(label='Content', value=new_result, height=300)
    print(new_result)