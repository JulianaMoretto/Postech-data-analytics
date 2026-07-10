# Estrutura e Análise da Jornada Comercial no HubSpot CRM

## Resumo Executivo

Este guia resume como usar as tabelas do HubSpot CRM para análises de negócio. A camada **silver** organiza os dados operacionais por entidade (leads, deals, empresas), enquanto a camada **gold** consolida esses dados em visões prontas para o acompanhamento dos funis Inbound e Outbound.

---

## Como escolher entre Silver e Gold

### Visão do fluxo: Silver → Journey → Gold

> Leia da esquerda para a direita: a **Silver** guarda os dados detalhados, a **Journey** conecta lead, deal e origem, e a **Gold** transforma essa jornada em indicadores prontos para a tomada de decisão.

| Camada / Tabela | O que contém | Quando usar |
|---|---|---|
| **Silver** | **Dados detalhados e tabelas de apoio:** Leads, Deals, Empresas, Owners, Atividades, Atribuição, Check-in/Check-out, Email Events. | Quando precisar investigar o detalhe operacional por trás de um indicador da camada Gold. |
| **Journey** | **Visão conectada:** Lead, Deal e Origem/Atribuição. <br>*(Tabela: `loft-dl-fintech.hubspot_crm.journey`)* | Quando precisar explicar a jornada de conversão (como um lead virou um deal e de onde ele veio). |
| **Gold** | **Indicadores consolidados:** Funil Inbound (Fiança e CRM), Funil Outbound e Email Events. | Como ponto de partida para dashboards, para acompanhar performance, conversão, vendas e contratos de forma consolidada. |

---

## Quando usar Gold

Use as tabelas **Gold** quando a pergunta for sobre performance de funil, conversão, volume de leads, reuniões, SQLs, vendas, contratos ou origem de marketing.

| Tabela | Use quando quiser analisar | Principais respostas |
|:---|:---|:---|
| `loft-dl-fintech.cp_gold.hubspot_funnel_inbound` | Funil Inbound, MQLs, Cadastros, Contratos e origem de marketing. | Quantos leads entraram, quantos avançaram, quantos viraram contrato e quais canais geraram resultado. |
| `loft-dl-fintech.cp_gold.hubspot_funnel_outbound` | Funil Outbound/BDR, Agendas Marcadas, Reuniões, SQLs e Vendas. | Quantos leads foram trabalhados, quantas reuniões ocorreram, quantos SQLs foram criados e quantas vendas aconteceram. |
| `loft-dl-fintech.cp_gold.hubspot_email_events` | Funil de emails de marketing. | Métricas consolidadas por `email_destinatario`: volume, engajamento, datas recentes e último assunto do envio. |

---

## Quando usar Silver

Use as tabelas **Silver** quando precisar de mais detalhe, investigação ou análise de uma entidade específica.

| Tabela Silver | Use para analisar |
|:---|:---|
| `loft-dl-fintech.hubspot_crm.leads` | Entrada, status, qualificação, backlog e atividades de leads. |
| `loft-dl-fintech.hubspot_crm.deals` | Negociações, deals ganhos/perdidos, valor fechado e motivos de perda. |
| `loft-dl-fintech.hubspot_crm.companies` | Imobiliárias/empresas, perfil da conta e recência de atividade. |
| `loft-dl-fintech.hubspot_crm.owners` | Responsáveis comerciais e equipes. |
| `loft-dl-fintech.hubspot_crm.engagements` | Ligações, reuniões, tarefas, notas e produtividade comercial. |
| `loft-dl-fintech.hubspot_crm.attribution` | Canal de origem, mídia paga/não paga, campanhas e UTMs. |
| `loft-dl-fintech.hubspot_crm.checkin_checkout` | Visitas presenciais, NPS da visita, comentários e plano de ação. |
| `loft-dl-fintech.hubspot_crm.journey` | Conexão entre lead, deal e atribuição; útil para explicar diferenças entre Silver e Gold. |
| `loft-dl-fintech.hubspot_crm.email_events` | Eventos por destinatário, tipo e data, com flags de status do email e último envio/assunto. |

---

## Guia Rápido de Escolha

- Para acompanhar **indicadores oficiais de negócio**, comece pela **Gold**.
- Para **investigar detalhes** ou entender a origem de um número, use a **Silver**.
- Para **conectar lead, deal e origem** em uma mesma jornada, use `int_hubspot_crm_journey`.

---

## Principais Métricas Disponíveis

- **Leads:** criados, trabalhados, qualificados, desqualificados e em backlog.
- **Deals:** criados, abertos, ganhos, perdidos, valor fechado e tempo até fechamento.
- **Atividades:** ligações, reuniões, no-show, tarefas e follow-ups.
- **Marketing:** canal de origem, campanha, UTM e classificação paga/não paga.
- **Conversão:** MQL, Cadastro, Contrato, Lead Outbound, Agenda Marcada, Reunião Realizada, SQL e Venda.
- **Email Events:** totais e únicos por status de e-mail, última data de envio e último assunto.

---

## 📖 Definições Importantes

### MQL
Lead do funil Inbound com data de criação preenchida. É usado como marco inicial da jornada Inbound.

### Agendado
Lead Inbound de CRM que chegou na etapa de "Agendado". É usado como marco de avanço dentro do funil Inbound (última etapa do time de SDR no funil).

### Cadastro
Lead Inbound que chegou na etapa de "Qualificação Finalizada" (Fiança) ou "Qualificado" (CRM) e está atualmente em uma dessas etapas. É usado como marco de avanço dentro do funil Inbound.

### Contrato
Deal ganho em funis de Fiança / Financiamento / CRM, com data de fechamento preenchida e etapa final de negócio fechado ou ganho.

### Lead Outbound
Lead criado no pipeline "BDR - Outbound Fiança". É usado como marco inicial da jornada Outbound.

### Agenda Marcada
Lead Outbound com entrada registrada na etapa de "Reunião Agendada".

### Reunião Realizada
Lead Outbound com entrada registrada na etapa de "Reunião Realizada".

### SQL
Deal criado no funil "Negociação - Outbound".

### Venda
Deal do funil "Negociação - Outbound" com entrada registrada na etapa "Ativo".

### Worked Lead
Lead que recebeu pelo menos um *touch* ou atividade comercial registrada.

### Backlog sem Touch
Lead ou empresa sem atividade registrada. Ajuda a identificar oportunidades que precisam de ação comercial.

### Cohort Lead
O campo `cohort_lead` mede o tempo entre a criação e o fechamento do lead. Ajuda a entender quanto tempo um lead leva para concluir sua jornada.

### Cohort Lead Deal
O campo `cohort_lead_deal` mede o tempo entre a criação do lead e o fechamento do deal associado. Ajuda a acompanhar o ciclo completo.

### Cohort Deal
O campo `cohort_deal` mede o tempo entre a criação e o fechamento do deal. Ajuda a entender a duração da negociação.

### Email Events
- **Evento:** Registro de interação do destinatário com um e-mail, identificado por `email_destinatario`, tipo e datas.
- **Tipo de evento:** Status traduzido como: *Processado, Enviado, Entregue, Deferido, Aberto, Descartado, Bounce, Suprimido, Mudança de Status* ou *Clicado*.
- **Métricas totais:** Soma de todas as ocorrências de cada status.
- **Métricas únicas:** Contagem de destinatários únicos por status.
- **Datas:** Campos como `data_criacao_evento`, `data_criacao_envio` e `ultima_data_envio` no fuso `America/Sao_Paulo`.
- **Assunto:** O campo `assunto_email` mostra o assunto do evento, e `ultimo_assunto_envio` o do último envio.

---

## Cuidados de Interpretação

- As tabelas **Gold** são as mais indicadas para consumo executivo e dashboards, pois já aplicam os filtros de funil.
- A tabela `int_hubspot_crm_journey` pode ter mais de uma linha por lead quando há mais de um deal associado.
- A qualidade de indicadores de atividades, reuniões e motivos de perda depende da qualidade dos registros no HubSpot.

---

## Perguntas de Negócio que a Estrutura Responde

### Marketing
- De quais canais vieram os leads?
- Quais canais geraram MQLs, cadastros ou contratos?
- Qual a distribuição entre mídia paga e não paga?
- Quais campanhas aparecem na origem das conversões?
- Quais e-mails tiveram maior abertura ou clique?

### Comercial
- Quantos leads foram trabalhados por owner ou equipe?
- Quantas reuniões foram agendadas e realizadas?
- Quais leads estão em backlog?
- Quantos deals foram ganhos, perdidos ou continuam abertos?

### Liderança
- Como está a conversão do funil Inbound?
- Como está a conversão do funil Outbound/BDR?
- Qual o tempo médio de conversão entre lead e fechamento?
- Quais etapas concentram perda ou backlog?

### Operação
- Quais registros precisam de follow-up?
- Quais empresas nunca foram trabalhadas?
- Quais visitas tiveram baixa avaliação ou pontos de melhoria?
- Quais atividades foram registradas por equipe?
