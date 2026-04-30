import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Projeto 5')

car_data = pd.read_csv('vehicles.csv')  # lendo os dados

if st.checkbox('Mostrar os 10 Modelos Mais Anunciados'):
    model_counts = car_data['model'].value_counts().head(10)

    fig = px.bar(
        x=model_counts.index,
        y=model_counts.values,
        labels={'x': 'Modelo', 'y': 'Quantidade'},
        title='Top 10 Modelos Mais Anunciados'
    )

    fig.update_layout(xaxis_tickangle=-45)

    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção do histograma
build_histogram = st.checkbox('Criar histograma')
# criar uma caixa de seleção do gráfico
build_scatterplot = st.checkbox('Criar gráfico de dispersão')

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
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
