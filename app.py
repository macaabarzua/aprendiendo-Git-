import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

datos = pd.read_csv('./megaline_users.csv')

print(datos.head())

datos['churn_date'].fillna(0, inplace=True)
#print(datos.info())

fig = px.histogram(datos, 'reg_date')
fig.show()

st.plotly_chart(fig)