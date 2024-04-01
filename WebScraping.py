import streamlit as st
from bs4 import BeautifulSoup
import requests


st.set_page_config(
    page_title = 'Wscraping',
    layout = 'wide'
)

st.title('Wscraping')
st.markdown(
    '''
    Descarga imagenes
    '''
)


URL= st.text_input(label="URL", value="data_input")
if URL:
    Links=[]
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', class_='image-list')
    if div:
        enlaces = div.find_all('a')
    HTML=[str(soup)]
    # Imprimir los enlaces
    for enlace in enlaces:
        Links.append(enlace.get('href'))
    st.write(Links)
    st.write(HTML)