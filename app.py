import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import clusterizando, new_customer, valor_aprovado, home, previsao_semana # import your pages here


# deixa a pagina full wide
st.set_page_config(layout="wide")

# Create an instance of the app 
app = MultiPage()

# Title of the main page
#display = Image.open('bootcamp.png')
#display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
#col1, col2 = st.columns(2)
#col1.image(display, width = 300)
#col2.title("Turma 17 IA")

# Add all your application here
app.add_page("Home", home.app)
app.add_page("Desafio 1 - Clusterizando", clusterizando.app)
app.add_page("Desafio 2 - Adicionando novo cliente", new_customer.app)
app.add_page("Desafio 3 - Valor Sugerido", valor_aprovado.app)
app.add_page("Desafio 4 - Previsao de aprovação",previsao_semana.app)

# The main app
app.run()