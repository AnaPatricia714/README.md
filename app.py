import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos (suponiendo que tienes el archivo 'vehicles_us.csv' en tu directorio)
car_data = pd.read_csv('vehicles_us.csv')

# Agregar un encabezado
st.header('Análisis de Vehículos de Estados Unidos')

# Crear los botones para generar gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Acción para el histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma con Plotly Express
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma del Odometer de los Vehículos")
    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# Acción para el gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para los vehículos')
    # Crear un gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="make", title="Gráfico de Dispersión de Odómetro vs Precio")
    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)

