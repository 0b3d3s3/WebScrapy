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
    dominio=URL.split(".")[0]+"."+URL.split(".")[1][0:3]
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', class_='image-list')
    if div:
        enlaces = div.find_all('a')
    
    # Imprimir los enlaces
    for enlace in enlaces:
        URL_IMG=dominio+enlace.get('href')
        responseIMG = requests.get(URL_IMG, headers=headers)
        soupIMG = BeautifulSoup(responseIMG.text, 'html.parser')
        divIMG = soupIMG.find('div', class_='flexi')
        if divIMG:
            enlacesIMG = divIMG.findAll('img')
        for link in enlacesIMG:
            Links.append(link.get("src"))
    for i in Links:
        st.image(i, caption='Imagen',use_column_width=False,width=360)
    st.write(Links)
