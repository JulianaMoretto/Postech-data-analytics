# Tech Challenge – Previsão de Tendência do IBOVESPA

Projeto desenvolvido no contexto da **Pós-Graduação em Data Analytics**, com foco em **modelagem de séries temporais e classificação supervisionada aplicada ao mercado financeiro**.

O desafio consiste em prever a **tendência do IBOVESPA no pregão seguinte** (alta ou baixa), utilizando exclusivamente dados históricos do próprio índice.

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

### 3. Engenharia de Variáveis
- Retornos logarítmicos
- Lags temporais
- Médias móveis
- Volatilidade histórica
- Features derivadas exclusivamente da própria série temporal

### 4. Modelagem
Foram avaliados múltiplos modelos de classificação:

- Regressão Logística  
- Random Forest  
- XGBoost  
- Gradient Boosting Classifier  

Os modelos foram comparados considerando desempenho, robustez e impacto do desbalanceamento das classes.

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

## Observação

Este projeto foi desenvolvido **exclusivamente para fins acadêmicos**, não constituindo recomendação de investimento.
