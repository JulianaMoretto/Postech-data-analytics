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
