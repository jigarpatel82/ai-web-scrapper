import streamlit as st
from scraper import scrape_web, clean_html_content
from ai import parse_content_with_ollama

st.title('AI Webscraper')
url = st.text_input('Enter the website URL')

if st.button('Scrape site'):
    # st.write('Scraping the website...')
    raw_data = scrape_web(url)
    clean_data = clean_html_content(raw_data)
    st.session_state['data'] = clean_data
    with st.expander('DOM content'):
        st.write(raw_data)
    st.text_area(label='Content', value=clean_data, height=300)
    print(clean_data)
    
if 'data' in st.session_state:
    parse_description = st.text_area('Enter what would you like to parse from scrapped data:')
    if st.button('Parse content'):
        if parse_description:
            parsed_result = parse_content_with_ollama(dom_content=st.session_state['data'], parse_description=parse_description)
            st.write(parsed_result)