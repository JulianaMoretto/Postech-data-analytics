# ObesityAI — Sistema Preditivo de Obesidade

Projeto desenvolvido no contexto da **Pós-Graduação em Data Analytics (FIAP POSTECH)**, com foco em **modelagem preditiva, feature engineering e deploy de aplicações de Machine Learning** aplicados à área da saúde.

O desafio consiste em prever o **nível de obesidade de um indivíduo** — em 7 categorias — a partir exclusivamente de **hábitos alimentares e de estilo de vida**, sem utilizar peso ou altura diretamente (para evitar data leakage via IMC).

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/<ericabugni>/<tech_challenge_4_obesity_analysis>.git
cd <tech_challenge_4_obesity_analysis>
```

### 2. Criar e ativar um ambiente virtual (recomendado)

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Garantir a estrutura de pastas

Certifique-se de que os arquivos estão organizados conforme abaixo antes de executar:

```text
tech_challenge_4_obesity_analysis/
├── data/
│   └── Obesity.csv                 # Dataset UCI
├── model_artifacts/
│   ├── best_model.b64              # Pipeline serializado (Base64)
│   ├── label_encoder.b64           # LabelEncoder serializado (Base64)
│   └── model_meta.json             # Metadados, métricas e resultados
├── obesity_ml_pipeline.ipynb       # Notebook de modelagem completo
├── app.py                          # Aplicação Streamlit principal
├── README.md
└── requirements.txt
```

### 5. Executar o notebook de modelagem (opcional)

Se quiser reproduzir o treinamento e gerar os artefatos do modelo, abra e execute o arquivo:

```
obesity_ml_pipeline.ipynb
```

> Os artefatos gerados (`best_model.b64`, `label_encoder.b64`, `model_meta.json`) devem ser movidos para a pasta `model_artifacts/`.

### 6. Executar a aplicação Streamlit

```bash
streamlit run app.py
```
---

## Objetivo do Projeto

Construir um **sistema preditivo multiclasse** capaz de classificar o nível de obesidade de um indivíduo em uma das 7 categorias abaixo, com base exclusivamente em seus hábitos de vida:

| Classe | Descrição |
|---|---|
| `Insufficient_Weight` | Peso Insuficiente |
| `Normal_Weight` | Peso Normal |
| `Overweight_Level_I` | Sobrepeso I |
| `Overweight_Level_II` | Sobrepeso II |
| `Obesity_Type_I` | Obesidade Tipo I |
| `Obesity_Type_II` | Obesidade Tipo II |
| `Obesity_Type_III` | Obesidade Tipo III |

O modelo deve ser capaz de identificar **perfis de risco comportamental**, permitindo intervenção preventiva mesmo antes que a obesidade se instale.

---

## Dados Utilizados

- **Fonte**: UCI Machine Learning Repository
- **Dataset**: Estimation of Obesity Levels Based On Eating Habits and Physical Condition
- **Periodicidade**: Registro único por indivíduo
- **Total de registros**: 2.111 (sendo ~65% sintéticos gerados por SMOTE)
- **Formato**: CSV

### Nota sobre dados sintéticos

O dataset já foi distribuído pelos autores com dados sintéticos incorporados via **SMOTE** (Synthetic Minority Oversampling Technique), aplicado para balancear as classes antes da publicação. A separação entre dados originais e sintéticos é feita por heurística (registros com idade não-inteira tendem a ser gerados por interpolação). No dashboard da aplicação é possível filtrar apenas os dados classificados como originais.

### Divisão dos Dados

- **Treino**: 80% dos registros, com estratificação por classe
- **Teste**: 20% dos registros, mantidos separados durante todo o treinamento

---

## Metodologia

O projeto segue um pipeline completo de análise exploratória, engenharia de features e Machine Learning:

### 1. Análise Exploratória
- Distribuição das variáveis numéricas e categóricas
- Análise de correlações com o target
- Identificação de padrões por classe de obesidade
- Avaliação do balanceamento das classes

### 2. Feature Engineering

As seguintes features foram criadas a partir das variáveis originais:

| Feature | Descrição |
|---|---|
| `age_group` | Faixa etária categórica derivada da idade (adolescente, jovem adulto, adulto, meia-idade, idoso) |
| `healthy_score` | Score 0–10 que combina hidratação, consumo de vegetais e atividade física (positivos) vs. snacking, álcool e alimentos calóricos (negativos) |
| `sedentary` | 1 se FAF = 0 e TUE ≥ 1 (sem exercício e alto uso de telas) |
| `fam_x_favc` | Risco combinado: histórico familiar positivo E consumo frequente de alimentos calóricos |
| `meal_activity_ratio` | Razão entre número de refeições e atividade física — proxy de desequilíbrio calórico |
| `high_alcohol` | 1 se o consumo de álcool for frequente ou constante |
| `CAEC_num` / `CALC_num` | Versão numérica ordinal das variáveis de snacking e álcool |

### 3. Decisão sobre Height e Weight — Data Leakage

Altura e peso foram **intencionalmente removidos** do modelo. O IMC (calculado com base nessas variáveis) é exatamente o critério utilizado para classificar os níveis de obesidade no dataset. Mantê-los tornaria o modelo trivial (~99% de acurácia sem nenhuma utilidade clínica). A remoção força o modelo a aprender com hábitos de vida, tornando a ferramenta genuinamente útil para triagem preventiva.

### 4. Pré-processamento
- Variáveis numéricas: `StandardScaler`
- Variáveis categóricas: `OneHotEncoder`
- Tudo encapsulado em um `Pipeline` do scikit-learn para garantir que as mesmas transformações aplicadas no treino sejam replicadas na inferência

### 5. Modelagem

Quatro algoritmos foram avaliados com **validação cruzada estratificada de 5 folds** (StratifiedKFold):

| Modelo | CV Médio | Acurácia Teste | AUC-ROC | F1-Macro |
|---|---|---|---|---|
| Logistic Regression | 61.1% | 60.3% | 0.8882 | 0.574 |
| Random Forest | 79.3% | 79.0% | 0.9611 | 0.788 |
| Gradient Boosting | 77.6% | 78.3% | 0.9570 | 0.783 |
| **Hist Gradient Boosting** | **78.9%** | **79.2%** | **0.9655** | **0.790** |
| SVM | 76.1% | 76.8% | 0.9454 | 0.764 |

---

## Resultados

- O **Hist Gradient Boosting** apresentou o melhor desempenho geral, sendo selecionado como modelo final.
- O modelo atingiu **79.2% de acurácia** no conjunto de teste, com **AUC-ROC de 0.966**.
- As classes extremas (`Obesity_Type_III`: F1 = 0.98, `Insufficient_Weight`: F1 = 0.85) foram classificadas com alta precisão.
- As classes intermediárias (`Normal_Weight`, `Overweight`) apresentaram maior confusão, o que é esperado dada a similaridade de perfil comportamental entre esses grupos.

---

## Estrutura do Repositório

```text
tech_challenge_4_obesity_analysis/
├── data/
    │── Obesity.csv                 # Dataset UCI
├── model_artifacts/
    ├── best_model.b64              # Pipeline serializado (Base64)
    ├── label_encoder.b64           # LabelEncoder serializado (Base64)
    │── model_meta.json             # Metadados, métricas e resultados
├── obesity_ml_pipeline.ipynb       # Notebook de modelagem completo
├── app.py                          # Aplicação Streamlit principal
├── README.md
└── requirements.txt
```

---

## Sobre a Aplicação Streamlit

A aplicação está organizada em três abas:

### Predição Individual
Formulário completo com todas as variáveis do modelo. O usuário preenche seus hábitos de vida e recebe:
- Classificação do nível de obesidade (7 classes)
- Nível de confiança da predição
- Probabilidade de pertencer a cada classe (gráfico)
- Score de hábitos saudáveis (0–10)
- IMC calculado de forma informativa (não usado no modelo)

### Dashboard Analítico
Painel interativo com filtros dinâmicos (gênero, faixa etária, nível de obesidade, atividade física, histórico familiar e origem dos dados). Inclui:
- KPIs gerais da base filtrada
- Distribuição de pacientes por nível e gênero
- Curvas de distribuição (KDE) de idade, altura e peso
- Seletor interativo de 11 análises gráficas lado a lado
- Análise de features criadas (score de hábitos, sedentarismo, razão refeições/atividade)
- Hábitos alimentares por classe
- Distribuição por faixa etária e meio de transporte
- Composição do dataset (originais vs. SMOTE)
- Métricas de desempenho do modelo
- Insights clínicos e recomendações médicas

### Como Funciona
Explicação acessível de todo o processo: origem dos dados, variáveis utilizadas, decisão sobre data leakage, comparação dos modelos testados, pipeline de deploy e como interpretar os resultados.

---

## Métricas de Avaliação

- **Acurácia** — métrica principal
- **AUC-ROC (OvR)** — avaliação da capacidade discriminativa multiclasse
- **F1-Score Macro** — equilíbrio entre precisão e recall entre todas as classes
- **Classification Report** — precisão, recall e F1 por classe
- **Confusion Matrix** - identificação dos padrões de erro e confusão entre classes do modelo

---

## Conclusões

- O **Hist Gradient Boosting** foi superior na captura de não linearidades típicas de dados comportamentais.
- A **remoção intencional de altura e peso** foi decisiva para garantir a utilidade clínica real da ferramenta.
- As variáveis criadas na etapa de **feature engineering** apareceram entre as features mais relevantes: `healthy_score`, `sedentary` e `meal_activity_ratio`.
- O desbalanceamento entre classes intermediárias (Sobrepeso I e II, Obesidade I) representa o principal desafio do modelo.
- O uso de **SMOTE no dataset original** contribui para acurácias mais altas, mas pode superestimar o desempenho real em populações não representadas.

---

## Possíveis Melhorias e Trabalhos Futuros

- Inclusão outros indicadores clínicos adicionais (exemplo: pressão arterial, glicemia, histórico de doenças metabólicas).
- Otimização de hiperparâmetros dos modelos via Optuna ou GridSearchCV.
- Técnicas de balanceamento mais robustas (ADASYN, class_weight) nas classes intermediárias.
- Avaliação com dados de populações de outras regiões geográficas para reduzir viés.
- Explainabilidade com SHAP Values para interpretação clínica individualizada.
- Ajuste de threshold por classe para otimizar recall em casos de risco elevado.

---

## Tecnologias Utilizadas

- Python 3.11
- Streamlit
- scikit-learn
- pandas
- NumPy
- Matplotlib
- Seaborn
- joblib

---

## Observação

Este projeto foi desenvolvido **exclusivamente para fins acadêmicos**, não constituindo recomendação médica ou diagnóstico clínico. A ferramenta é um auxílio à decisão e não substitui avaliação profissional de saúde.

---

## Grupo

- Ariany
- Érica
- João Vitor
- Juliana
- Willer
