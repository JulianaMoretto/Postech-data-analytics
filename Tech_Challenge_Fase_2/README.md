# Tech Challenge – Previsão de Tendência do IBOVESPA

Projeto desenvolvido no contexto da **Pós-Graduação em Data Analytics**, com foco em **modelagem de séries temporais e classificação supervisionada aplicada ao mercado financeiro**.

O desafio consiste em prever a **tendência do IBOVESPA no pregão seguinte** (alta ou baixa), utilizando exclusivamente dados históricos do próprio índice.

## Apresentação do Projeto

O vídeo abaixo apresenta o contexto do desafio, abordagem metodológica, modelos utilizados e principais resultados obtidos.

Assista à apresentação (Drive) [https://link-drive](https://drive.google.com/file/d/17y2Jteft3pNSABpY9eRd3u-5kvWdW8eA/view?usp=drive_link)
(Youtube) [https://link-youtube][(https://www.youtube.com/watch?v=mDkHY1w59uw)](https://www.youtube.com/watch?v=mDkHY1w59uw)

---

## Grupo

- Ariany  
- Érica  
- João Vitor  
- Juliana  
- Willer  

---

## Objetivo do Projeto

Construir um **modelo de classificação binária** capaz de prever se o índice IBOVESPA fechará em **alta (↑)** ou **baixa (↓)** no dia seguinte, atendendo aos critérios estabelecidos no desafio.

O modelo deve:
- Alcançar **acurácia mínima de 75%**
- Utilizar como conjunto de teste os **últimos 30 pregões disponíveis**
- Ser treinado a partir de uma série histórica de aproximadamente **20 anos** contendo dados de:
  - Abertura
  - Fechamento
  - Máxima
  - Mínima
  - Volume
  - Variação

### Definição do Target

- **1 (Alta)**: se `Close(t+1) > Close(t)`
- **0 (Baixa)**: caso contrário

---

## Dados Utilizados

- **Fonte**: Investing.com  
- **Índice**: IBOVESPA  
- **Periodicidade**: Diária  
- **Horizonte temporal**: ~20 anos de histórico  
- **Formato**: CSV  

Link: https://br.investing.com/indices/bovespa-historical-data

### Divisão dos Dados

- **Base de treino**: histórico completo, exceto o período final  
- **Base de teste**: últimos **30 pregões**

---

## Metodologia

O projeto segue um pipeline completo de análise de séries temporais e Machine Learning:

### 1. Análise Exploratória
- Visualização da evolução histórica do IBOVESPA
- Avaliação de tendência, volatilidade e regimes de mercado
- Análise de médias móveis e desvio padrão móvel

### 2. Estacionariedade
- Teste de Dickey-Fuller Aumentado (ADF)
- Identificação de não estacionariedade na série original
- Aplicação de diferenciação para estabilização estatística

### 3. Feature Engineering

As seguintes *features* foram criadas:

**- Preços defasados** - Fechamento, Máxima, Mínima e Abertura que representam o estado do mercado no último pregão, sendo colocados defasados para representar a memória do mercado.
**- Médias móveis** -	*lags* de 1, 5, 20 e 60 dias, indicador extremamente utilizados em séries financeiras.
**- Distância até a média** - Normalização do preço em relação à tendência, importante para verificar se o preço está esticado ou revertendo.
**- Retornos defasados** -	*lags* de 1, 5, 10 e 20 dias, capturando a inércia do mercado.
**- Volatilidade intradiária** - Abertura vs Fechamento defasados, medindo a força do movimento dentro do pregão e também se o mercado está calmo ou estressado.
**- Range diário** - Mede a incerteza e extremos de preço.

**Target**

1 = alta no dia seguinte  
0 = queda no dia seguinte

**Train/Test Split**

- Treino: todos os dados históricos
- Teste: últimos 30 dias
- Divisão não aleatória, respeitando a ordem temporal.

### 4. Modelagem
Foram avaliados múltiplos modelos de classificação:

- Regressão Logística  
- Random Forest  
- XGBoost  
- Gradient Boosting Classifier  

Os modelos foram comparados considerando desempenho, robustez e impacto do desbalanceamento das classes.

## Estrutura do Repositório
Tech_Challenge_Fase2
│
├── Grupo126_TechChallenge_Fase2_SeriesTemporais.ipynb   # Notebook principal
├── Dados Históricos - Ibovespa.csv                      # Base de dados
└── README.md                                            ← link do vídeo
---

## Métricas de Avaliação

- **Acurácia** (métrica principal – critério mínimo: ≥ 75%)
- **F1-score**
- **Precision e Recall**
- **Matriz de Confusão**
- **Classification Report**

---

## Resultados

- O **Gradient Boosting Classifier** apresentou o melhor desempenho geral.
- O modelo atingiu **acurácia de aproximadamente 80%** no conjunto de teste.
- Apesar do viés para a classe majoritária, apresentou **boa capacidade direcional**.

**Resultado final**:
- **24 acertos em 30 previsões** nos últimos pregões, indicando corretamente a tendência do fechamento em *t+1*.

---

## Conclusões

- Modelos baseados em **boosting** foram mais eficazes na captura de não linearidades e ruído típicos de séries financeiras.
- O tratamento da estacionariedade foi essencial para garantir consistência estatística.
- O desbalanceamento das classes impactou métricas como F1-score, reforçando a necessidade de análise além da acurácia.
- O projeto demonstra a aplicação prática de Machine Learning na **previsão direcional de índices financeiros** em contexto acadêmico.

---

## Tecnologias Utilizadas

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- XGBoost  
- Statsmodels  

---

## Possíveis melhorias e trabalhos futuros
Como próximos passos, o modelo pode ser aprimorado com a inclusão de novas features de regime e momentum, além de indicadores macroeconômicos e de volume. Também é recomendável testar janelas maiores de validação temporal e técnicas de balanceamento mais robustas. Pode-se aplicar também ajustes de threshold e otimização bayesiana de hiperparâmetros que possam vir a elevar o F1-Score. Por fim, a adoção de modelos híbridos (clássicos + deep learning) como ARIMA, Prophet, LSTM/GRU, por exemplo, pode vir a capturar padrões não lineares mais complexos.

---

## Apresentação do Projeto

O vídeo abaixo apresenta o contexto do desafio, abordagem metodológica, modelos utilizados e principais resultados obtidos.

Assista à apresentação:
[https://link-do-video](https://drive.google.com/file/d/17y2Jteft3pNSABpY9eRd3u-5kvWdW8eA/view?usp=drive_link)

---

## Observação

Este projeto foi desenvolvido **exclusivamente para fins acadêmicos**, não constituindo recomendação de investimento.
