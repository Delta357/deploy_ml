import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Carregar o modelo treinado e outros pré-processamentos necessários
model = RandomForestClassifier()
model = joblib.load('G:\Meu Drive\AI_data_lab\deploy\diabetes_ml\modelo_treinado.pkl')  # Substitua pelo caminho correto do seu modelo treinado

# Função para fazer as previsões
def fazer_previsao(dados):
    # Pré-processar os dados, se necessário
    # Fazer as previsões usando o modelo treinado
    # Retornar as previsões
    # # Interface do usuário
    st.title('Aplicativo de Previsão de Diabetes')

    # Entrada dos dados
    st.write('Insira os dados para fazer a previsão de diabetes:')
    col1, col2, col3 = st.beta_columns(3)
    gravidez = col1.number_input('Gravidez', min_value=0, max_value=10, value=0)
    glicose = col2.number_input('Glicose', min_value=0, max_value=200, value=0)
    pressao_sanguinea = col3.number_input('Pressão Sanguínea', min_value=0, max_value=150, value=0)

    # Botão para fazer a previsão
    if st.button('Fazer Previsão'):
        # Criar um dataframe com os dados inseridos
        dados = pd.DataFrame({'Gravidez': [gravidez],
                              'Glicose': [glicose],
                              'Pressão Sanguínea': [pressao_sanguinea]})
    
    # Fazer a previsão usando o modelo treinado
    resultado = fazer_previsao(dados)
    
    # Exibir o resultado
    st.write('Resultado da Previsão:')
    st.write(resultado)
