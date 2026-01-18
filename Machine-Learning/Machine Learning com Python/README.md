## 📘 Aula 01 – Introdução ao Machine Learning com Python

Este projeto faz parte do meu estudo em **Machine Learning com Python**, com foco na compreensão dos conceitos fundamentais da área e no primeiro contato com as principais bibliotecas utilizadas no desenvolvimento de modelos de ML.

Nesta aula, o objetivo foi construir uma **base conceitual sólida**, entendendo o que é Machine Learning, suas aplicações no mercado e como os dados são preparados ao longo de um pipeline analítico até a construção e avaliação de modelos.

---

### Conteúdos abordados

- Conceito de Machine Learning e sua relação com Inteligência Artificial
- Principais aplicações práticas:
  - Detecção de fraudes
  - Mercado financeiro
  - Vendas e retenção de clientes
  - Sistemas de recomendação
- Tipos de aprendizado:
  - Aprendizado supervisionado
  - Aprendizado não supervisionado
- Visão geral do pipeline de Machine Learning:
  - Entendimento do problema de negócio
  - Coleta de dados
  - Exploração e visualização
  - Feature engineering
  - Treinamento de modelos
  - Validação e monitoramento

---

### Bibliotecas apresentadas

- NumPy – manipulação de arrays e operações matemáticas
- Pandas – análise e preparação de dados
- Matplotlib – visualização de dados
- Scikit-learn – algoritmos clássicos de Machine Learning
- TensorFlow – redes neurais e Deep Learning
- PyTorch – Deep Learning com foco em desempenho e GPU

---

### Atividade prática (Hands-on)

- Importação de dados com Python
- Exploração inicial dos dados
- Uso da documentação oficial das bibliotecas
- Estímulo à autonomia na análise de dados

---

### Objetivo do projeto

Registrar e consolidar os aprendizados iniciais em Machine Learning, servindo como base para projetos mais avançados e compondo um portfólio técnico em Python e Data Science.

---


## 📘 Aula 02 – Análise Exploratória de Dados (EDA) com Python

Este projeto faz parte do meu estudo em **Machine Learning com Python**, com foco na **Análise Exploratória de Dados (EDA)**, etapa essencial para compreender a base de dados, gerar insights e preparar informações para a construção de modelos de Machine Learning.

Nesta aula, foram exploradas técnicas práticas de EDA utilizando Python, com o objetivo de entender a estrutura dos dados, identificar padrões, detectar problemas (como valores nulos e duplicados) e analisar relações entre variáveis.

---

### Conteúdos abordados

- Introdução à Análise Exploratória de Dados (EDA)
- Importância da EDA para entendimento do problema de negócio
- Etapas do processo de análise de dados:
  - Importação do dataset
  - Entendimento da estrutura da base
  - Preparação dos dados
  - Análise estatística descritiva
  - Compreensão das variáveis
  - Estudo das relações entre variáveis
  - Geração de insights

---

### Dataset utilizado

- Base de dados do **Spotify**, contendo informações sobre músicas, artistas e características musicais
- Dataset utilizado para prática de exploração e visualização de dados

---

### Técnicas e funções aplicadas

- Leitura e exploração inicial de dados:
  - `pd.read_csv`
  - `head()` e `tail()`
  - `shape`
  - `info()`
- Análise estatística:
  - `describe()` e `describe().T`
- Qualidade dos dados:
  - Identificação de dados duplicados (`duplicated`, `duplicated().sum()`)
  - Identificação de valores nulos (`isnull`, `isnull().sum()`)
- Análise de variáveis:
  - Frequência de categorias com `value_counts()`
  - Distribuição de variáveis numéricas com `hist()`
- Análise de relações entre variáveis:
  - Pairplot
  - Boxplot
  - Mapa de calor (correlação)

---

### Visualizações desenvolvidas

- Histogramas para análise de distribuição
- Gráficos de barras para variáveis categóricas
- Boxplots para comparação entre variáveis numéricas e categóricas
- Pairplot para análise inicial de correlações
- Heatmap para identificação de correlações fortes entre variáveis

---

### Objetivo do projeto

Aplicar técnicas de Análise Exploratória de Dados para compreender profundamente um dataset real, gerar insights relevantes e preparar os dados para etapas futuras de modelagem em Machine Learning.

---

## 📘 Aula 03 – Feature Engineering com Python

Este projeto faz parte do meu estudo em **Machine Learning com Python**, com foco na etapa de **Feature Engineering**, responsável por preparar e transformar os dados para que modelos de Machine Learning consigam aprender padrões de forma eficiente.

Nesta aula, o foco foi trabalhar com uma **base real do IBGE (PNAD-COVID)**, aplicando técnicas de limpeza, organização e transformação de dados, etapa fundamental após a Análise Exploratória de Dados (EDA).

---

### Conteúdos abordados

- Introdução ao conceito de Feature Engineering
- Importância da preparação dos dados para modelos de ML
- Trabalho com bases reais e complexas
- Uso de dicionário de dados para interpretação das variáveis

---

### Dataset utilizado

- **Informações de Cada**
- Base com mais de 4600 linhas e 17 colunas, contendo dados como quantidade de quartos, andares, preço, entre outros

---

### Técnicas aplicadas

- Seleção de variáveis relevantes
- Renomeação de colunas para melhor legibilidade
- Verificação e ajuste de tipos de dados (`dtype`)
- Tratamento de dados ausentes:
  - Remoção de linhas
  - Remoção de colunas
  - Estratégias de imputação
- Normalização e padronização de dados
- Discussão sobre impacto dessas técnicas em diferentes algoritmos

---

### Objetivo do projeto

Preparar uma base de dados real para uso em modelos de Machine Learning, aplicando técnicas de Feature Engineering que garantam qualidade, consistência e melhor desempenho dos algoritmos.

---

## 📘 Aula 04 – Modelos de Regressão em Machine Learning

Este projeto faz parte do meu estudo em **Machine Learning com Python**, com foco em **modelos supervisionados de regressão**, utilizados para prever valores numéricos contínuos.

Nesta aula, foram apresentados os principais algoritmos de regressão, suas aplicações práticas e as métricas utilizadas para avaliar a performance dos modelos.

---

### Conteúdos abordados

- Introdução aos modelos de regressão
- Diferença entre regressão simples e múltipla
- Conceitos de variável preditora e variável alvo (target)
- Avaliação de modelos de regressão

---

### Algoritmos estudados

- Regressão Linear (simples e múltipla)
- Support Vector Regression (SVR)
- Árvores de Regressão
- KNN para regressão
- Random Forest para regressão

---

### Avaliação de modelos

- R² (coeficiente de determinação)
- MAE (Erro Absoluto Médio)
- MSE (Erro Quadrático Médio)
- Validação cruzada
- Análise de underfitting e overfitting
- Comparação entre modelos

---

### Objetivo do projeto

Compreender o funcionamento dos principais algoritmos de regressão, aprender a avaliá-los corretamente e identificar o equilíbrio entre complexidade do modelo e capacidade de generalização.

---

## 📘 Aula 05 – Modelos de Classificação em Machine Learning

Este projeto faz parte do meu estudo em **Machine Learning com Python**, com foco em **modelos supervisionados de classificação**, utilizados para prever categorias ou classes a partir de dados rotulados.

Nesta aula, foram estudados os principais algoritmos de classificação, suas aplicações práticas e as métricas utilizadas para avaliar a qualidade das predições.

---

### Conteúdos abordados

- Introdução aos modelos de classificação
- Diferença entre regressão e classificação
- Conceitos de classes, rótulos e fronteiras de decisão
- Limitações comuns em modelos de classificação

---

### Algoritmos estudados

- Regressão Logística
- Naive Bayes
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Árvores de Decisão

---

### Avaliação de modelos

- Acurácia
- Precisão e Recall
- F1-score
- Matriz de Confusão
- Curva ROC e AUC
- Validação cruzada
- Análise de overfitting e underfitting
- Impacto de dados desbalanceados

---

### Objetivo do projeto

Aplicar e comparar diferentes algoritmos de classificação, entendendo seus pontos fortes, limitações e critérios de avaliação para escolher o modelo mais adequado a cada problema.

---
