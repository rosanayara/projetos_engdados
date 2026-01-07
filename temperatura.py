import os
import requests
import pandas as pd
import sqlite3 
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def pipeline_etl(cidade):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    
    try:
        # Extraindo as informações de temperatura da plataforma OpenWeatherMap        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Transformando as informações obtidas em um DataFrame
        dados_limpos = {
            "Cidade": data["name"],
            "Temperatura": data["main"]["temp"],
            "Clima": data["weather"][0]["description"],
            "Umidade": data["main"]["humidity"],
            "Data_Coleta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        df = pd.DataFrame([dados_limpos])

        # Carregado esses dados para o banco SQLite 
        conexao = sqlite3.connect('meu_projeto_etl.db')
        
        df.to_sql('historico_clima', con=conexao, if_exists='append', index=False)
        
        conexao.close() 
        
        print("=" * largura)
        print("INFORMAÇÕES CLIMÁTICAS".center(largura))
        print("=" * largura)
        print()
        print(df)
        print()
        print("=" * largura)
        print("Dados armazenados com sucesso!".center(largura))
        print()
        

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":

    while True:
        largura = 60
        print("=" * largura)
        print("SISTEMA DE MONITORAMENTO CLIMÁTICO".center(largura))
        print("=" * largura)
        print()
        cidade_usuario = input("Digite o nome da cidade em que deseja obter informações ou 'sair' para encerrar: ").strip()
        print()
        if cidade_usuario.lower() == 'sair':  
            print("=" * largura)
            print("Programa encerrado. Volte Sempre!".center(largura))
            print("=" * largura)
            break
        if not cidade_usuario:
            print('Por favor, digite um nome de cidade válido.')
            continue

        pipeline_etl(cidade_usuario)
