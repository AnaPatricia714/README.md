import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Título y encabezado de la aplicación
st.title('Análisis de Datos de Vehículos')
st.header('Exploración de los anuncios de venta de vehículos')

# Botón para crear un histograma
hist_button = st.button('Construir histograma')

if hist_button:
    # Mensaje al usuario
    st.write('Creando un histograma para la columna "odometer" del conjunto de datos.')
    
    # Crear un histograma usando Plotly Express
    fig_histogram = px.histogram(car_data, x='odometer', title="Histograma de Odometer")
    
    # Mostrar el gráfico de histograma
    st.plotly_chart(fig_histogram, use_container_width=True)

# Botón para crear un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Mensaje al usuario
    st.write('Creando un gráfico de dispersión para "price" vs "odometer".')
    
    # Crear el gráfico de dispersión usando Plotly Express
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title="Gráfico de Dispersión: Odometer vs Price")
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)
