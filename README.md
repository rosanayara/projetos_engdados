# Pipeline ETL de Monitoramento Climático

Este projeto implementa conhecimentos adquiridos sobre pipeline de dados, onde é extraído informações climáticas em tempo real utilizando uma API externa da OpenWeatherMap, transformando os dados brutos obtidos em um DataFrame e logo em seguida os armazena de forma estruturada no banco de dados SQLite.

# Como executar
1. Clone este repositório.
2. Crie um arquivo .env baseado no .env.example e insira sua chave da API.
3. Execute o script:
   ```bash
   python temperatura.py
