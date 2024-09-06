import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

import data_wrangling

def main():
    datos = pd.read_csv('./megaline_users.csv')
    
    datos = data_wrangling.clean(datos)

    #print(datos.info())

    boton_histograma = st.button('Click aquí para dibujar el histograma')

    if boton_histograma:
        fig = px.histogram(datos, 'reg_date')
        fig.show()

        st.plotly_chart(fig)

if __name__ == '__main__':
    main()