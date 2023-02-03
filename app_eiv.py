#______________________________________________________________________________________________________________________

## IMPORTA BIBLIOTECAS PARA O PYTHON ##

import pandas as pd
import re
import streamlit as st
import os
from PIL import Image

#______________________________________________________________________________________________________________________

## INPUTS DA PÁGINA DO STREAMLIT ##

st.set_page_config(
     page_title="PMI - EIV",
     page_icon=('./dados/favicon.png'),
     layout="wide",
 )

#______________________________________________________________________________________________________________________

## SIDEBAR ##

# Input box do aprova
logo_image = ('./dados/logo.png')
st.sidebar.image(logo_image, width=200)
st.sidebar.subheader('Verificação EIV:')
texto_aprova = st.sidebar.text_input('Inscrição Imobiliária:','',key="inputbox1")
