# Análise de Séries Temporais – ADF

Este projeto apresenta uma **análise exploratória e estatística de uma série temporal mensal de produção elétrica**, com foco em **estacionariedade**, **tendência**, **sazonalidade** e **preparação para modelagem ARIMA**.

O notebook documenta, passo a passo, o processo clássico de análise de séries temporais, desde a leitura dos dados até a inspeção de autocorrelações.

---

## Base de dados

- **Fonte**: Electric Production (produção elétrica mensal)
- **Frequência**: Mensal
- **Variável principal**: `Value` (nível de produção)
- **Índice temporal**: coluna `DATE`, convertida para `datetime` e definida como índice do DataFrame

---

## Estrutura da análise

### 1. Leitura e preparação dos dados
- Leitura do CSV com `parse_dates`
- Definição da coluna de data como índice temporal
- Validação da estrutura (`head`, `info`, `describe`)

---

### 2. Visualização da série original
- Plot da série ao longo do tempo
- Análise visual inicial de:
  - tendência
  - variação
  - possível sazonalidade

---

### 3. Decomposição sazonal
Aplicação de `seasonal_decompose` para separar a série em:
- **Observed** (série original)
- **Trend** (tendência)
- **Seasonal** (sazonalidade)
- **Residual** (ruído)

Objetivo: entender a estrutura interna da série.

---

### 4. Teste de estacionariedade (ADF)
Aplicação do **Augmented Dickey-Fuller Test (ADF)** para verificar a presença de raiz unitária:

- Estatística do teste
- p-value
- Valores críticos (1%, 5%, 10%)

Critério:
- `p-value ≤ 0.05` → rejeita hipótese nula → série estacionária

---

### 5. Média móvel (12 períodos)
- Cálculo da média móvel de 12 meses
- Comparação entre série original e tendência suavizada

Objetivo:
- Reduzir ruído
- Evidenciar tendência e sazonalidade

---

### 6. Transformação logarítmica
Aplicação de `log(Value)` para:
- Estabilizar a variância
- Reduzir heterocedasticidade
- Tornar o crescimento mais linear

A média móvel é recalculada após o log para nova inspeção visual.

---

### 7. Remoção de tendência (detrending)
- Subtração da média móvel da série em log:
- série_detrendida = log(Value) − média_móvel_12
- Avaliação de:
- média móvel da série detrendida
- desvio padrão móvel

Objetivo: verificar se média e variância permanecem constantes ao longo do tempo.

---

### 8. Teste ADF na série detrendida
- O teste ADF é reaplicado após log + remoção de tendência
- Resultado:
- Estatística do teste menor que os valores críticos
- p-value muito baixo

Conclusão: **a série transformada é estacionária**.

---

### 9. Diferenciação (diff)
- Aplicação da primeira diferença na série detrendida
- Análise visual de média e variância móvel
- Novo teste ADF

Observação:
- A diferenciação é exploratória; a série já apresentava estacionariedade antes desse passo.

---

### 10. ACF e PACF
Cálculo e visualização de:
- **ACF (Autocorrelation Function)**
- **PACF (Partial Autocorrelation Function)**

Com bandas de confiança de 95%: ± 1.96 / √N
Objetivo:
- Identificar lags estatisticamente significativos
- Auxiliar na escolha de parâmetros `p` e `q` para modelos ARIMA

---

## Conclusões

- A série original apresenta tendência e não é estacionária
- A transformação logarítmica estabiliza a variância
- A remoção de tendência via média móvel torna a série estacionária
- O teste ADF confirma estacionariedade após as transformações
- ACF e PACF fornecem subsídios para modelagem ARIMA

---

## Objetivo do projeto

Demonstrar domínio do **pipeline clássico de análise de séries temporais**, com foco em:
- diagnóstico estatístico
- interpretação econômica/temporal
- preparação adequada para modelos de previsão

