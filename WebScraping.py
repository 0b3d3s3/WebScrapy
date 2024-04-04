import streamlit as st
from bs4 import BeautifulSoup
import requests

def get_ext(link):
    ext=link.split("/")[-1].split(".")[1].split("?")[0]
    return(ext)
    
    
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
NumIMG= st.number_input(label="URL", value=500)
if URL:
    Links=[]
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    enlaces=[]
    End=True
    while len(enlaces)<NumIMG and End:
        response = requests.get(URL+"&pid={0}".format(len(enlaces)), headers=headers)
        dominio=URL.split(".")[0]+"."+URL.split(".")[1][0:3]
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', class_='image-list')
        if div:
            enlaces = enlaces+div.find_all('a')
        if len(div.find_all('a'))==0:
            End=False
    st.write([len(enlaces)])
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
    X=0
    for i in Links:
        Descarga_IMG = requests.get(i,headers=headers)    
        # Verifica si la solicitud fue exitosa (código de estado 200)
        if Descarga_IMG.status_code == 200:
            # Guarda el contenido de la respuesta en un archivo
            print(i)
            Nombre=str(X)+"."+get_ext(i)
            with open("image/"+Nombre, 'wb') as f:
                f.write(Descarga_IMG.content)
            print("Imagen descargada exitosamente como {0}".format(Nombre))
            X+=1
        else:
            print("Error al descargar la imagen. Código de estado:", response.status_code)
    st.write(Links)
