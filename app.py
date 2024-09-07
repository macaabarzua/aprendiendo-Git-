import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

from data_wrangling import Limpiador

def main():
    datos_raw = pd.read_csv('./megaline_users.csv')
    
    limpiador = Limpiador('limpiador de películas', datos_raw)

    print(datos_raw.isna().sum())

    datos_clean = limpiador.clean()

    print(datos_clean.isna().sum())

    #print(datos.info())

    #boton_histograma = st.button('Click aquí para dibujar el histograma')

    #if boton_histograma:
        #fig = px.histogram(datos, 'reg_date')
        #fig.show()

        #st.plotly_chart(fig)

if __name__ == '__main__':
    main()