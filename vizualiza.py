import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico():
    print("🔄 Conectando ao banco de dados...")
    conexao = sqlite3.connect('meu_projeto_etl.db')
    
    # Vamos listar o que tem no banco para ter certeza
    df = pd.read_sql('SELECT * FROM historico_clima', conexao)
    conexao.close()

    if df.empty:
        print("❌ O banco de dados está vazio! Rode o 'temperatura.py' e cadastre cidades primeiro.")
        return

    print(f"✅ Dados encontrados! Gerando gráfico para {len(df)} registros...")
    
    plt.figure(figsize=(10, 6))
    plt.bar(df['Cidade'], df['Temperatura'], color='skyblue')
    plt.title('Comparativo de Temperatura')
    plt.ylabel('Graus Celsius (°C)')
    
    # Esta linha salva a imagem na sua pasta para você ver depois
    plt.savefig('meu_grafico.png')
    print("💾 Imagem salva como 'meu_grafico.png' na pasta do projeto.")
    
    plt.show() # Tenta abrir a janela visual

if __name__ == "__main__":
    gerar_grafico()