import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
# criar uma caixa de seleção do histograma
build_histogram = st.checkbox('Criar histograma')
# criar uma caixa de seleção do gráfico
build_scatterplot = st.checkbox('Criar gráfico de dispersão')

st.header('Projeto 5')

if build_histogram:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if build_scatterplot:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
