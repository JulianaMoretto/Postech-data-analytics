# Tech Challenge FIAP – Fase 3 | COVID-19 PNAD

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte do Tech Challenge – Fase 3 da FIAP e tem como objetivo aplicar técnicas de Data Analytics em dados de saúde para gerar insights estratégicos voltados à gestão hospitalar durante a pandemia de COVID-19.

A análise utiliza a base PNAD COVID-19 do IBGE, com foco em identificar:

* Perfis com maior risco de agravamento
* Pressão potencial sobre a rede hospitalar
* Barreiras de acesso ao atendimento
* Comportamentos associados ao aumento de casos
* Recomendações para planejamento hospitalar em cenários de surto

O projeto foi estruturado seguindo uma arquitetura em camadas (Medallion Architecture), utilizando AWS e Google Colab.

---

## 👥 Integrantes

* Ariany Bertoncello
* Érica Bugni
* João Vitor Braga
* Juliana Moretto
* Willer Stern

---

## 🏗️ Arquitetura do Projeto

O pipeline de dados foi construído em 4 camadas principais:

```text
CSV IBGE → Bronze (Raw) → Silver (Tratamento) → Gold (Features) → Athena / Colab
```

### Fluxo resumido

1. Extração dos arquivos CSV da PNAD COVID-19
2. Conversão para Parquet
3. Tratamento e padronização dos dados
4. Criação de indicadores de saúde e risco
5. Disponibilização via AWS Athena
6. Consumo final em Google Colab para análise exploratória

---

## 📂 Estrutura dos Arquivos

```text
├── covid-pnad-ETL-job-csv-to-raw.ipynb
├── covid-pnad-notebook-ETL-job-raw-to-gold.ipynb
├── covid_pnad_data_exploration.ipynb
├── Tech Challenge FIAP_Fase 3_COVID_PNAD.pptx.pdf
└── README.md
```

### Descrição dos arquivos

#### `covid-pnad-ETL-job-csv-to-raw.ipynb`

Notebook responsável pela primeira etapa do pipeline:

* Leitura dos arquivos CSV da PNAD COVID-19
* Upload para AWS S3
* Conversão dos dados para formato Parquet
* Organização na camada Bronze/Raw

#### `covid-pnad-notebook-ETL-job-raw-to-gold.ipynb`

Notebook responsável pelas transformações e enriquecimento:

* Limpeza e padronização dos dados
* Ajuste de tipos
* Tradução e padronização de respostas
* Criação de features e indicadores
* Geração da camada Gold

Exemplos de variáveis derivadas:

* `qtd_sintomas`
* `nivel_severidade`
* `caso_grave`
* `possui_comorbidade`
* `score_isolamento`
* `perfil_risco_comportamental`
* `kit_prevencao`

#### `covid_pnad_data_exploration.ipynb`

Notebook final de análise exploratória e geração de insights.

Inclui:

* Distribuição demográfica
* Sintomas e testes positivos
* Análise de severidade e gravidade
* Comorbidades
* Funil assistencial
* Pressão hospitalar
* Heatmap de correlação
* Perfil comportamental
* Análise por atividade econômica

#### `Tech Challenge FIAP_Fase 3_COVID_PNAD.pptx.pdf`

Apresentação executiva com os principais resultados, insights e recomendações para gestão hospitalar.
https://docs.google.com/presentation/d/1Iwoz6eKLs-6XBFQ8CZMFAyjibqmeuJeR/edit?slide=id.p12#slide=id.p12

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* PySpark
* AWS S3
* AWS Glue
* AWS Glue Data Catalog
* Amazon Athena
* Google Colab
* Jupyter Notebook
* Matplotlib
* Seaborn

---

## 🧪 Pipeline de Dados

### 1. Camada Bronze

* Armazena os dados brutos da PNAD COVID-19
* Mantém os arquivos originais preservados
* Conversão de CSV para Parquet

### 2. Camada Silver

* Limpeza e transformação dos dados
* Tratamento de valores ausentes
* Tradução de categorias
* Padronização dos tipos

### 3. Camada Gold

Criação de indicadores para análise hospitalar, como:

* Índice de risco
* Gravidade do caso
* Probabilidade de internação
* Score de isolamento
* Presença de comorbidades
* Perfil de risco comportamental

---

## 📊 Principais Insights

* Os sintomas mais frequentes foram dor de cabeça, nariz entupido e tosse
* A gravidade está concentrada em pacientes idosos e/ou com comorbidades
* O número de sintomas é um forte indicador de necessidade de internação
* Existe grande perda entre “ter sintomas” e “buscar atendimento”
* A maior pressão hospitalar ocorre no atendimento inicial, e não necessariamente na internação
* O risco comportamental ajuda a antecipar movimentos de aumento da positividade
* Pacientes com 5 ou mais sintomas apresentam maior probabilidade de evolução grave

---

## 🏥 Recomendações Geradas

Com base na análise, as principais recomendações para hospitais são:

* Reforçar a triagem utilizando idade, sintomas e comorbidades
* Priorizar o monitoramento de grupos vulneráveis
* Reservar leitos específicos para idosos
* Acompanhar indicadores de internação e ventilação
* Planejar capacidade hospitalar de forma preditiva
* Direcionar campanhas de conscientização conforme o perfil de risco regional

---

## 📚 Fonte dos Dados

Os dados utilizados neste projeto são provenientes da PNAD COVID-19, disponibilizada pelo IBGE.

* Base: PNAD COVID-19
* Período analisado: julho a setembro de 2020
* Fonte oficial: [https://www.ibge.gov.br/](https://www.ibge.gov.br/)

