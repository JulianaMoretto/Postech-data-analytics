📘 Aula 01 – Modelos Supervisionados de Classificação com Python

Este projeto faz parte do meu estudo em Machine Learning com Python, com foco na compreensão de problemas de classificação supervisionada e nos primeiros passos práticos para preparação de dados e estruturação de modelos.

Nesta aula, o objetivo foi entender quando um problema é de classificação, como os algoritmos aprendem a partir de dados rotulados e quais cuidados são necessários antes do treinamento de um modelo.

Conteúdos abordados

Diferença entre:

Regressão (previsão de valores numéricos)

Classificação (previsão de classes ou categorias)

Conceito de modelo supervisionado

Exemplo prático: classificação de e-mails em spam e não spam

Papel das features (variáveis explicativas) no processo de aprendizado

Importância do pré-processamento dos dados

Conversão de variáveis categóricas para formato numérico

Cuidados com representação de categorias

Separação da base em treino e teste

Uso do train_test_split

Parâmetros:

test_size

random_state

stratify para balanceamento das classes

Bibliotecas apresentadas

Pandas – manipulação e preparação de dados

NumPy – operações matemáticas e vetoriais

Scikit-learn – estruturação de modelos supervisionados

Atividade prática (Hands-on)

Identificação de um problema de classificação

Separação correta entre variáveis explicativas (X) e variável alvo (y)

Criação de bases de treino e teste

Primeiros experimentos com modelos classificadores

Objetivo do projeto

Aprender a estruturar corretamente um problema de classificação supervisionada, preparando os dados e criando a base necessária para aplicação e comparação de algoritmos nas aulas seguintes.

📘 Aula 02 – Modelos Supervisionados de Classificação: KNN e SVM

Este projeto aprofunda o estudo de modelos supervisionados de classificação, com foco nos algoritmos K-Nearest Neighbors (KNN) e Support Vector Machines (SVM).

O objetivo foi compreender o funcionamento matemático e geométrico desses modelos, além de aplicar ajustes de hiperparâmetros e interpretar seus resultados.

Conteúdos abordados

Algoritmo KNN:

Classificação baseada em proximidade

Métricas de distância (Euclidiana e Manhattan)

Impacto do número de vizinhos (k)

Importância do escalonamento dos dados

Algoritmo SVM:

Margem de separação entre classes

Hiperparâmetro C e regularização

Sensibilidade à escala dos dados

Classificação linear e não linear

Uso de kernels (polinomial e RBF)

Comparação entre modelos supervisionados

Bibliotecas apresentadas

Scikit-learn – KNN, SVM e pipelines

NumPy – manipulação de dados

Pandas – estruturação dos datasets

Atividade prática (Hands-on)

Implementação de KNN e SVM em Python

Testes com diferentes valores de k e C

Comparação de desempenho entre modelos

Análise do impacto do pré-processamento

Objetivo do projeto

Entender como funcionam algoritmos clássicos de classificação supervisionada e aprender a ajustar seus hiperparâmetros de forma consciente.

📘 Aula 03 – Aprendizado Não Supervisionado: K-Means e DBSCAN

Este projeto introduz o aprendizado não supervisionado, com foco em técnicas de clusterização aplicadas a dados sem rótulos.

O objetivo foi aprender a segmentar dados, interpretar agrupamentos e avaliar a qualidade dos clusters.

Conteúdos abordados

Conceito de aprendizado não supervisionado

Algoritmo K-Means:

Funcionamento baseado em centroides

Escolha do número de clusters

Método Elbow

Algoritmo DBSCAN:

Agrupamento por densidade

Identificação de outliers

Métricas de validação de clusters:

Silhouette Score

Adjusted Rand Index

Comparação entre K-Means e DBSCAN

Desafios do aprendizado de máquina

Bibliotecas apresentadas

Scikit-learn – K-Means, DBSCAN e métricas

Matplotlib – visualização de clusters

Pandas – análise exploratória dos dados

Atividade prática (Hands-on)

Aplicação de K-Means e DBSCAN

Avaliação da qualidade dos clusters

Análise visual dos agrupamentos

Comparação entre diferentes técnicas

Objetivo do projeto

Aprender a trabalhar com dados não rotulados e escolher a técnica de clusterização mais adequada conforme o comportamento dos dados.

📘 Aula 04 – Consolidação de Modelagem e Boas Práticas

Este projeto tem como foco a consolidação dos conceitos de modelagem em Machine Learning, reforçando boas práticas e visão crítica sobre resultados.

Conteúdos abordados

Organização do pipeline de Machine Learning

Qualidade dos dados e impacto nos modelos

Feature engineering

Overfitting e underfitting

Estratégias de regularização

Interpretação crítica de métricas

Bibliotecas apresentadas

Scikit-learn

Pandas

NumPy

Atividade prática (Hands-on)

Revisão de modelos já treinados

Análise de erros

Discussão sobre generalização

Objetivo do projeto

Desenvolver maturidade analítica para avaliar modelos além do resultado numérico, considerando contexto e limitações.

📘 Aula 05 – Validação Cruzada e Seleção de Hiperparâmetros

Este projeto aborda técnicas estatísticas para avaliação robusta de modelos, reduzindo o risco de overfitting.

Conteúdos abordados

Limitações do treino/teste simples

Validação cruzada (K-Fold)

Comparação entre modelos

Seleção de hiperparâmetros

GridSearchCV

Bibliotecas apresentadas

Scikit-learn – KFold, cross_val_score, GridSearchCV

Atividade prática (Hands-on)

Aplicação de K-Fold

Comparação de múltiplos algoritmos

Busca dos melhores hiperparâmetros

Objetivo do projeto

Garantir que os modelos generalizem bem para dados não vistos, aumentando a confiabilidade das análises.

📘 Aula 06 – Métricas de Avaliação para Classificação

Este projeto aprofunda o estudo das métricas de avaliação de modelos classificadores, indo além da acurácia.

Conteúdos abordados

Matriz de confusão

Acurácia

Precisão

Recall

F1-Score

Classification Report

Avaliação por classe

Impacto de dados desbalanceados

Bibliotecas apresentadas

Scikit-learn – métricas de classificação

Matplotlib – visualização da matriz de confusão

Atividade prática (Hands-on)

Avaliação de classificadores

Interpretação de métricas

Comparação entre modelos

Objetivo do projeto

Aprender a escolher métricas alinhadas ao impacto real do erro no problema de negócio.

📘 Aula 07 – Curva ROC e AUC

Este projeto explora métricas baseadas em probabilidade, com foco em Curva ROC e AUC, muito utilizadas em classificação binária.

Conteúdos abordados

Classificadores probabilísticos

Curva ROC (TPR vs FPR)

Interpretação da AUC

Comparação entre modelos

Modelo aleatório vs modelo ideal

Bibliotecas apresentadas

Scikit-learn – ROC Curve e AUC

Matplotlib – visualização da curva ROC

Atividade prática (Hands-on)

Geração da curva ROC

Cálculo da AUC

Análise visual da performance dos modelos

Objetivo do projeto

Avaliar modelos de classificação binária de forma mais completa, considerando diferentes limiares de decisão.
