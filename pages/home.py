from pandas import read_csv
import streamlit as st
from PIL import  Image
import numpy as np
import os
from multipage import MultiPage
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def app():
    #st.markdown("## Valor Aprovado")
    #set_png_as_page_bg('bootcamp.png')
    #with open("style.css") as f:
    #    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
    # Title of the main page
    display = Image.open('bootcamp.png')
    display = np.array(display)
    # st.image(display, width = 400)
    # st.title("Data Storyteller Application")
    #col1, col2 = st.columns(2)
    #st.title("Turma 17IA")
    #st.subheader("Equipe: Bartira, Vitor Carvalhal, Tiago e Ricardo")
    st.image(display,width=None)
    