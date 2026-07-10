"""
app.py — ObesityAI: Sistema Preditivo de Obesidade
FIAP POSTECH · Data Analytics · Tech Challenge Fase 4

Estrutura de pastas esperada:
    app.py
    data/
        Obesity.csv
    model_artifacts/
        best_model.b64
        label_encoder.b64
        model_meta.json
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import base64
import io
import warnings
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings("ignore")

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURAÇÃO DA PÁGINA
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="ObesityAI — Sistema Preditivo",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
# CSS GLOBAL
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

    .header-box {
        background: linear-gradient(135deg, #0d1b2a 0%, #1b2d45 60%, #1a3a5c 100%);
        padding: 1.8rem 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
        border-left: 5px solid #00c8ff;
    }
    .header-box h1 { margin:0; font-size:1.9rem; font-weight:700; letter-spacing:-0.5px; }
    .header-box p  { margin:0.4rem 0 0; opacity:0.72; font-size:0.9rem; }

    .kpi-card {
        background: white;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.07);
        border-top: 3px solid #00c8ff;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .kpi-card .val { font-size:1.8rem; font-weight:700; color:#0d1b2a; line-height:1.1; }
    .kpi-card .lbl { font-size:0.73rem; color:#888; margin-top:0.25rem; text-transform:uppercase; letter-spacing:.6px; }

    .kpi-card-green  { border-top: 3px solid #43A047 !important; }
    .kpi-card-yellow { border-top: 3px solid #FDD835 !important; }
    .kpi-card-red    { border-top: 3px solid #E53935 !important; }
    .kpi-card-purple { border-top: 3px solid #7B1FA2 !important; }
    .kpi-card-blue   { border-top: 3px solid #1565c0 !important; }
    .kpi-card-teal   { border-top: 3px solid #00838f !important; }

    .result-low    { background:#e8f5e9; color:#2e7d32; border:2px solid #66bb6a;
                     border-radius:12px; padding:1.2rem 1.5rem; font-size:1.15rem; font-weight:600; text-align:center; }
    .result-medium { background:#fff8e1; color:#e65100; border:2px solid #ffa726;
                     border-radius:12px; padding:1.2rem 1.5rem; font-size:1.15rem; font-weight:600; text-align:center; }
    .result-high   { background:#ffebee; color:#b71c1c; border:2px solid #ef5350;
                     border-radius:12px; padding:1.2rem 1.5rem; font-size:1.15rem; font-weight:600; text-align:center; }

    .insight {
        background:#f4f7fb; border-left:3px solid #00c8ff;
        border-radius:8px; padding:.85rem 1.2rem;
        margin-bottom:.55rem; font-size:.9rem; line-height:1.5;
    }
    .insight-warn {
        background:#fff8e1; border-left:3px solid #fb8c00;
        border-radius:8px; padding:.85rem 1.2rem;
        margin-bottom:.55rem; font-size:.9rem; line-height:1.5;
    }
    .insight-alert {
        background:#ffebee; border-left:3px solid #e53935;
        border-radius:8px; padding:.85rem 1.2rem;
        margin-bottom:.55rem; font-size:.9rem; line-height:1.5;
    }
    .insight-success {
        background:#e8f5e9; border-left:3px solid #43a047;
        border-radius:8px; padding:.85rem 1.2rem;
        margin-bottom:.55rem; font-size:.9rem; line-height:1.5;
    }
    .warn-box {
        background:#fff3e0; border-left:4px solid #ff9800;
        border-radius:8px; padding:.8rem 1.1rem; font-size:.88rem; margin-bottom:1rem;
    }
    .section-title {
        font-size:1.05rem; font-weight:700; color:#0d1b2a;
        margin:1.2rem 0 0.6rem; letter-spacing:-0.3px;
    }
    .timeline-step {
        background: white;
        border-radius: 12px;
        padding: 1.1rem 1.4rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        border-left: 4px solid #00c8ff;
        margin-bottom: 0.9rem;
    }
    .timeline-step h4 { margin:0 0 0.3rem; color:#0d1b2a; font-size:1rem; }
    .timeline-step p  { margin:0; color:#444; font-size:0.88rem; line-height:1.55; }
    .tag {
        display:inline-block; background:#e3f2fd; color:#1565c0;
        border-radius:20px; padding:2px 10px; font-size:0.75rem;
        font-weight:600; margin-right:4px; margin-bottom:4px;
    }
    .tag-green  { background:#e8f5e9 !important; color:#2e7d32 !important; }
    .tag-orange { background:#fff3e0 !important; color:#e65100 !important; }
    .tag-purple { background:#f3e5f5 !important; color:#6a1b9a !important; }
    div[data-testid="stForm"] {
        background:#f8fafc; border-radius:14px;
        padding:1.2rem 1.5rem; border:1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] { font-weight:600; font-size:.95rem; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CONSTANTES
# ══════════════════════════════════════════════════════════════════════════════
DATA_PATH    = "data/Obesity.csv"
ARTIFACT_DIR = "model_artifacts"

ORDER_CLS = [
    "Insufficient_Weight", "Normal_Weight",
    "Overweight_Level_I",  "Overweight_Level_II",
    "Obesity_Type_I",      "Obesity_Type_II",      "Obesity_Type_III",
]
LABEL_PT = {
    "Insufficient_Weight": "Peso Insuficiente",
    "Normal_Weight":        "Peso Normal",
    "Overweight_Level_I":   "Sobrepeso I",
    "Overweight_Level_II":  "Sobrepeso II",
    "Obesity_Type_I":       "Obesidade Tipo I",
    "Obesity_Type_II":      "Obesidade Tipo II",
    "Obesity_Type_III":     "Obesidade Tipo III",
}
RISK_MAP = {
    "Insufficient_Weight": ("low",    "⬇️  Peso Insuficiente"),
    "Normal_Weight":        ("low",    "✅  Peso Normal"),
    "Overweight_Level_I":   ("medium", "⚠️  Sobrepeso Nível I"),
    "Overweight_Level_II":  ("medium", "⚠️  Sobrepeso Nível II"),
    "Obesity_Type_I":       ("high",   "🔴  Obesidade Tipo I"),
    "Obesity_Type_II":      ("high",   "🔴  Obesidade Tipo II"),
    "Obesity_Type_III":     ("high",   "🔴  Obesidade Tipo III"),
}
CORES_PALETTE = ["#43A047","#66BB6A","#FDD835","#FB8C00","#E53935","#B71C1C","#4A148C"]
PALETTE_DICT  = dict(zip(ORDER_CLS, CORES_PALETTE))
PALETTE_PT    = dict(zip([LABEL_PT[c] for c in ORDER_CLS], CORES_PALETTE))
CAEC_MAP = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
CALC_MAP  = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}

OPCOES_FCVC = {
    0: "0 — Nunca como vegetais",
    1: "1 — Às vezes como vegetais",
    2: "2 — Frequentemente como vegetais",
    3: "3 — Sempre como vegetais em todas as refeições",
}
OPCOES_NCP = {
    1: "1 — Uma refeição por dia",
    2: "2 — Duas refeições por dia",
    3: "3 — Três refeições por dia",
    4: "4 — Quatro refeições por dia",
    5: "5 — Cinco ou mais refeições por dia",
}
OPCOES_CH2O = {
    0: "0 — Menos de 1 litro por dia",
    1: "1 — Entre 1 e 2 litros por dia",
    2: "2 — Entre 2 e 3 litros por dia",
    3: "3 — Mais de 3 litros por dia",
}
OPCOES_FAF = {
    0: "0 — Não pratico atividade física",
    1: "1 — 1 a 2 dias por semana",
    2: "2 — 2 a 4 dias por semana",
    3: "3 — 4 a 5 dias por semana (quase todos os dias)",
}
OPCOES_TUE = {
    0: "0 — Até 2 horas por dia",
    1: "1 — Entre 3 e 5 horas por dia",
    2: "2 — Entre 5 e 8 horas por dia",
    3: "3 — Mais de 8 horas por dia",
}

# ══════════════════════════════════════════════════════════════════════════════
# FEATURE ENGINEERING  (idêntico ao notebook)
# ══════════════════════════════════════════════════════════════════════════════
def calcular_age_group(age: float) -> str:
    if age < 18:  return "adolescente"
    if age < 25:  return "jovem_adulto"
    if age < 35:  return "adulto"
    if age < 50:  return "meia_idade"
    return "idoso"

def calcular_age_group_display(age: float) -> str:
    if age < 18:  return "Adolescente"
    if age < 25:  return "Jovem Adulto"
    if age < 35:  return "Adulto"
    if age < 50:  return "Meia-idade"
    return "Idoso"

def calcular_healthy_score(fcvc, ch2o, faf, caec, calc_freq, favc) -> float:
    caec_num = CAEC_MAP.get(caec, 0)
    calc_num = CALC_MAP.get(calc_freq, 0)
    favc_num = 1 if favc == "yes" else 0
    positive = (ch2o / 3) + (fcvc / 3) + (faf / 3)
    negative = (caec_num / 3) + (calc_num / 3) + favc_num
    score    = (positive - negative / 2) * 10 / 3
    return float(np.clip(round(score, 2), 0, 10))

def montar_entrada(inputs: dict) -> pd.DataFrame:
    age    = inputs["age"]
    fcvc   = inputs["fcvc"]
    ncp    = inputs["ncp"]
    ch2o   = inputs["ch2o"]
    faf    = inputs["faf"]
    tue    = inputs["tue"]
    caec   = inputs["caec"]
    calc_f = inputs["calc"]
    favc   = inputs["favc"]
    fam    = inputs["family_history"]

    caec_num = CAEC_MAP.get(caec, 0)
    calc_num = CALC_MAP.get(calc_f, 0)

    row = {
        "Gender"              : inputs["gender"],
        "Age"                 : age,
        "family_history"      : fam,
        "FAVC"                : favc,
        "FCVC"                : fcvc,
        "NCP"                 : ncp,
        "CAEC"                : caec,
        "SMOKE"               : inputs["smoke"],
        "CH2O"                : ch2o,
        "SCC"                 : inputs["scc"],
        "FAF"                 : faf,
        "TUE"                 : tue,
        "CALC"                : calc_f,
        "MTRANS"              : inputs["mtrans"],
        "CAEC_num"            : caec_num,
        "CALC_num"            : calc_num,
        "age_group"           : calcular_age_group(age),
        "healthy_score"       : calcular_healthy_score(fcvc, ch2o, faf, caec, calc_f, favc),
        "sedentary"           : int(faf == 0 and tue >= 1),
        "fam_x_favc"          : int(fam == "yes") * int(favc == "yes"),
        "meal_activity_ratio" : round(ncp / (faf + 1), 3),
        "high_alcohol"        : int(calc_num >= 2),
    }
    return pd.DataFrame([row])

# ══════════════════════════════════════════════════════════════════════════════
# CARREGAMENTO DOS ARTEFATOS (b64 — estrutura original do app.py)
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_resource
def carregar_artefatos():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with open(f"{ARTIFACT_DIR}/best_model.b64", "r") as f:
            pipeline = joblib.load(io.BytesIO(base64.b64decode(f.read())))
        with open(f"{ARTIFACT_DIR}/label_encoder.b64", "r") as f:
            label_enc = joblib.load(io.BytesIO(base64.b64decode(f.read())))
    with open(f"{ARTIFACT_DIR}/model_meta.json", "r", encoding="utf-8") as f:
        meta = json.load(f)
    return pipeline, label_enc, meta

@st.cache_data(show_spinner="Carregando base de dados...")
def carregar_dados():
    df = pd.read_csv(DATA_PATH)
    for col in ["FCVC", "NCP", "CH2O", "FAF", "TUE"]:
        df[col] = df[col].round().astype(int)

    bins_age   = [0, 18, 25, 35, 50, 100]
    labels_age = ["Adolescente", "Jovem Adulto", "Adulto", "Meia-idade", "Idoso"]
    df["age_group_display"] = pd.cut(df["Age"], bins=bins_age, labels=labels_age, right=False).astype(str)
    df["age_group"]         = df["Age"].apply(calcular_age_group)

    df["CAEC_num"] = df["CAEC"].map(CAEC_MAP)
    df["CALC_num"]  = df["CALC"].map(CALC_MAP)

    positive = (df["CH2O"] / 3) + (df["FCVC"] / 3) + (df["FAF"] / 3)
    negative = (df["CAEC_num"] / 3) + (df["CALC_num"] / 3) + df["FAVC"].map({"yes": 1, "no": 0})
    df["healthy_score"]       = ((positive - negative / 2) * 10 / 3).clip(0, 10).round(2)
    df["sedentary"]           = ((df["FAF"] == 0) & (df["TUE"] >= 1)).astype(int)
    df["fam_x_favc"]          = ((df["family_history"] == "yes").astype(int) * (df["FAVC"] == "yes").astype(int))
    df["meal_activity_ratio"] = (df["NCP"] / (df["FAF"] + 1)).round(3)
    df["high_alcohol"]        = df["CALC_num"].apply(lambda x: 1 if x >= 2 else 0)
    df["sintetico"]           = (df["Age"] % 1 != 0)

    df["Obesity_PT"] = df["Obesity"].map(LABEL_PT)
    df["Obesity"]    = pd.Categorical(df["Obesity"],    categories=ORDER_CLS, ordered=True)
    df["Obesity_PT"] = pd.Categorical(df["Obesity_PT"], categories=[LABEL_PT[c] for c in ORDER_CLS], ordered=True)
    return df

# ══════════════════════════════════════════════════════════════════════════════
# INICIALIZAÇÃO
# ══════════════════════════════════════════════════════════════════════════════
import os
if not os.path.exists(DATA_PATH):
    st.error(f"❌ Arquivo `{DATA_PATH}` não encontrado. Coloque o `Obesity.csv` dentro da pasta `data/`.")
    st.stop()

try:
    pipeline, label_enc, meta = carregar_artefatos()
    artefatos_ok = True
except FileNotFoundError:
    artefatos_ok = False

df_global = carregar_dados()

# ══════════════════════════════════════════════════════════════════════════════
# CABEÇALHO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="header-box">
  <h1>🏥 ObesityAI — Sistema Preditivo de Obesidade</h1>
  <p>Ferramenta de apoio à decisão clínica &nbsp;|&nbsp; FIAP POSTECH · Data Analytics · Tech Challenge Fase 4</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ABAS PRINCIPAIS
# ══════════════════════════════════════════════════════════════════════════════
tab1, tab2, tab3 = st.tabs([
    "🔮  Predição Individual",
    "📊  Dashboard Analítico",
    "🧠  Como Funciona",
])

# ╔══════════════════════════════════════════════════════════════════════════════
# ║  ABA 1 — PREDIÇÃO INDIVIDUAL
# ╚══════════════════════════════════════════════════════════════════════════════
with tab1:

    if not artefatos_ok:
        st.error(
            "⚠️ Artefatos do modelo não encontrados!\n\n"
            "Certifique-se de que a pasta **`model_artifacts/`** contém:\n"
            "- `best_model.b64`\n"
            "- `label_encoder.b64`\n"
            "- `model_meta.json`"
        )
        st.stop()

    # ── Sidebar — informações do modelo ──────────────────────────────────────
    with st.sidebar:
        st.header("ℹ️ Sobre o Modelo")
        st.markdown(f"**Algoritmo:** {meta.get('best_model_name', '—')}")
        st.markdown(f"**Acurácia (teste):** {float(meta.get('test_accuracy', 0)):.1%}")
        st.markdown(f"**AUC-ROC:** {float(meta.get('auc_roc', 0)):.4f}")
        st.markdown(f"**F1-macro:** {float(meta.get('f1_macro', 0)):.4f}")
        st.divider()
        st.caption("⚠️ Height e Weight foram removidos para evitar data leakage.")
        st.divider()
        with st.expander("📊 Todos os modelos testados"):
            for nome, res in meta.get("model_results", {}).items():
                st.markdown(
                    f"**{nome}**  \n"
                    f"CV: {res['cv_mean']:.4f} ±{res['cv_std']:.4f}  \n"
                    f"Teste: {res['test_acc']:.4f} | AUC: {res['auc_roc']:.4f}"
                )

    st.markdown('<div class="section-title">👤 Dados do Paciente</div>', unsafe_allow_html=True)
    st.caption("Preencha os campos abaixo e clique em **Realizar Diagnóstico**.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**👤 Perfil**")
        gender = st.selectbox("Gênero", ["Male", "Female"],
            format_func=lambda x: "Masculino" if x == "Male" else "Feminino")
        age    = st.number_input("Idade (anos)", min_value=10, max_value=100, value=25)
        height = st.number_input("Altura (m)", min_value=1.40, max_value=2.20, value=1.70, step=0.01,
                                  help="Usado para calcular o IMC informativo — não entra no modelo.")
        weight = st.number_input("Peso (kg)", min_value=30.0, max_value=250.0, value=70.0, step=0.5,
                                  help="Usado para calcular o IMC informativo — não entra no modelo.")
        family_history = st.selectbox("Histórico familiar de excesso de peso?",
            ["yes", "no"], format_func=lambda x: "Sim" if x == "yes" else "Não")
        smoke = st.selectbox("Fuma?", ["no", "yes"],
            format_func=lambda x: "Não" if x == "no" else "Sim")

    with col2:
        st.markdown("**🥗 Hábitos**")
        favc = st.selectbox("Come alimentos calóricos com frequência?",
            ["yes", "no"], format_func=lambda x: "Sim" if x == "yes" else "Não")
        scc  = st.selectbox("Monitora calorias ingeridas?",
            ["no", "yes"], format_func=lambda x: "Não" if x == "no" else "Sim")
        mtrans = st.selectbox("Meio de transporte habitual",
            ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"],
            format_func=lambda x: {
                "Public_Transportation": "Transporte Público", "Walking": "Caminhando",
                "Automobile": "Carro", "Motorbike": "Moto", "Bike": "Bicicleta"
            }[x])
        caec = st.selectbox("Come entre as refeições?",
            ["no", "Sometimes", "Frequently", "Always"],
            format_func=lambda x: {
                "no": "Não", "Sometimes": "Às vezes",
                "Frequently": "Frequentemente", "Always": "Sempre"
            }[x])

    st.divider()
    st.markdown('<div class="section-title">🥗 Hábitos Alimentares e de Saúde</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)

    with col3:
        fcvc_label = st.selectbox("Com que frequência come vegetais?", list(OPCOES_FCVC.values()))
        fcvc = [k for k, v in OPCOES_FCVC.items() if v == fcvc_label][0]

        ncp_label = st.selectbox("Quantas refeições principais faz por dia?", list(OPCOES_NCP.values()))
        ncp = [k for k, v in OPCOES_NCP.items() if v == ncp_label][0]

        ch2o_label = st.selectbox("Quanta água bebe por dia?", list(OPCOES_CH2O.values()))
        ch2o = [k for k, v in OPCOES_CH2O.items() if v == ch2o_label][0]

    with col4:
        faf_label = st.selectbox("Com que frequência pratica atividade física?", list(OPCOES_FAF.values()))
        faf = [k for k, v in OPCOES_FAF.items() if v == faf_label][0]

        tue_label = st.selectbox("Quanto tempo usa dispositivos tecnológicos por dia?", list(OPCOES_TUE.values()))
        tue = [k for k, v in OPCOES_TUE.items() if v == tue_label][0]

        calc = st.selectbox("Frequência do consumo de álcool",
            ["no", "Sometimes", "Frequently", "Always"],
            format_func=lambda x: {
                "no": "Não bebo", "Sometimes": "Às vezes",
                "Frequently": "Frequentemente", "Always": "Sempre"
            }[x])

    st.divider()

    # ── Botão de previsão ─────────────────────────────────────────────────────
    if st.button("🔍 Realizar Diagnóstico", type="primary", use_container_width=True):
        inputs = dict(
            gender=gender, age=age, family_history=family_history,
            favc=favc, fcvc=fcvc, ncp=ncp, caec=caec, smoke=smoke,
            ch2o=ch2o, scc=scc, faf=faf, tue=tue, calc=calc, mtrans=mtrans
        )

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            X_input    = montar_entrada(inputs)
            pred_enc   = pipeline.predict(X_input)[0]
            pred_class = label_enc.inverse_transform([pred_enc])[0]
            pred_proba = pipeline.predict_proba(X_input)[0]

        risk_level, risk_label = RISK_MAP.get(pred_class, ("low", pred_class))
        confianca = pred_proba.max() * 100
        hs        = calcular_healthy_score(fcvc, ch2o, faf, caec, calc, favc)
        sedentary = int(faf == 0 and tue >= 1)
        fam_favc  = int(family_history == "yes") * int(favc == "yes")

        # IMC informativo
        bmi = round(weight / (height ** 2), 1)
        if bmi < 18.5:   bmi_class, bmi_color = "Abaixo do peso",  "#1565c0"
        elif bmi < 25.0: bmi_class, bmi_color = "Peso normal",     "#2e7d32"
        elif bmi < 30.0: bmi_class, bmi_color = "Sobrepeso",       "#e65100"
        else:            bmi_class, bmi_color = "Obesidade (OMS)", "#b71c1c"

        st.markdown(f"""
        <div style="background:#f4f7fb; border-radius:10px; padding:.9rem 1.2rem;
                    border-left:3px solid {bmi_color}; margin-bottom:1rem; font-size:.9rem;">
          📏 <b>IMC calculado:</b> {bmi} kg/m²  —  <span style="color:{bmi_color}; font-weight:600">{bmi_class}</span>
          <br><small style="color:#888">Apenas informativo — o modelo preditivo não utiliza altura e peso diretamente.</small>
        </div>
        """, unsafe_allow_html=True)

        # Resultado principal
        st.markdown('<div class="section-title">📋 Resultado do Diagnóstico</div>', unsafe_allow_html=True)
        col_res, col_prob = st.columns([1, 2])

        with col_res:
            st.markdown(f'<div class="result-{risk_level}">{risk_label}</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <br><small>
            🤖 Confiança do modelo: <b>{confianca:.1f}%</b><br>
            🧬 Score de hábitos saudáveis: <b>{hs:.1f} / 10</b><br>
            🏃 Perfil sedentário: <b>{"Sim" if sedentary else "Não"}</b><br>
            🍔 Risco genético + alimentar: <b>{"Alto" if fam_favc else "Baixo"}</b><br>
            🏷️ Faixa etária: <b>{calcular_age_group_display(age)}</b>
            </small>
            """, unsafe_allow_html=True)
            if risk_level == "high":
                st.warning("Recomenda-se avaliação clínica detalhada.")
            elif risk_level == "medium":
                st.info("Recomenda-se acompanhamento nutricional preventivo.")
            else:
                st.success("Indicadores dentro da faixa saudável.")

        with col_prob:
            st.markdown("**Probabilidade por Classe**")
            prob_series = pd.Series(pred_proba, index=label_enc.classes_).sort_values(ascending=False)
            bar_colors  = ["#0d1b2a" if c == pred_class else "#90CAF9" for c in prob_series.index]

            fig, ax = plt.subplots(figsize=(7, 4))
            ax.barh([LABEL_PT.get(c, c) for c in prob_series.index], prob_series.values, color=bar_colors)
            ax.set_xlim(0, 1)
            ax.set_xlabel("Probabilidade")
            for i, v in enumerate(prob_series.values):
                ax.text(v + 0.01, i, f"{v:.1%}", va="center", fontsize=9)
            ax.spines[["top", "right"]].set_visible(False)
            plt.rcParams["figure.facecolor"] = "none"
            plt.rcParams["axes.facecolor"]   = "none"
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

        with st.expander("📝 Resumo dos dados inseridos"):
            resumo = {
                "Gênero"                    : "Masculino" if gender == "Male" else "Feminino",
                "Idade"                     : f"{age} anos ({calcular_age_group_display(age)})",
                "Altura / Peso"             : f"{height} m / {weight} kg (IMC: {bmi})",
                "Histórico familiar"        : "Sim" if family_history == "yes" else "Não",
                "Alimentos calóricos freq." : "Sim" if favc == "yes" else "Não",
                "Vegetais"                  : OPCOES_FCVC[fcvc],
                "Refeições/dia"             : OPCOES_NCP[ncp],
                "Come entre refeições"      : caec,
                "Fuma"                      : "Sim" if smoke == "yes" else "Não",
                "Água/dia"                  : OPCOES_CH2O[ch2o],
                "Monitora calorias"         : "Sim" if scc == "yes" else "Não",
                "Atividade física"          : OPCOES_FAF[faf],
                "Tempo em telas"            : OPCOES_TUE[tue],
                "Álcool"                    : calc,
                "Transporte"                : mtrans,
            }
            st.table(pd.DataFrame(resumo.items(), columns=["Campo", "Valor"]))

    st.divider()
    st.caption(
        "⚕️ Este sistema é um auxílio ao diagnóstico e **não substitui** a avaliação clínica. "
        "| POSTECH — Tech Challenge Fase 04 — Data Analytics"
    )

# ╔══════════════════════════════════════════════════════════════════════════════
# ║  ABA 2 — DASHBOARD ANALÍTICO
# ╚══════════════════════════════════════════════════════════════════════════════
with tab2:

    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.facecolor"] = "none"
    plt.rcParams["axes.facecolor"]   = "none"

    df = df_global.copy()
    ORDEM_PT = [LABEL_PT[c] for c in ORDER_CLS]

    # ── Filtros na sidebar (só visíveis nesta aba via st.sidebar) ─────────────
    with st.sidebar:
        st.markdown("## 🔍 Filtros do Dashboard")

        filtro_genero = st.multiselect(
            "Gênero",
            options=["Male", "Female"],
            default=["Male", "Female"],
            format_func=lambda x: "Masculino" if x == "Male" else "Feminino",
        )
        filtro_classe = st.multiselect(
            "Nível de Obesidade",
            options=ORDER_CLS,
            default=ORDER_CLS,
            format_func=lambda x: LABEL_PT[x],
        )
        filtro_idade = st.slider(
            "Faixa de Idade",
            min_value=int(df["Age"].min()),
            max_value=int(df["Age"].max()),
            value=(int(df["Age"].min()), int(df["Age"].max())),
        )
        filtro_faf = st.multiselect(
            "Atividade Física",
            options=[0, 1, 2, 3],
            default=[0, 1, 2, 3],
            format_func=lambda x: {0:"Nenhuma",1:"1-2x/sem",2:"3-4x/sem",3:"5x+/sem"}[x],
        )
        filtro_fam = st.multiselect(
            "Histórico Familiar",
            options=["yes", "no"],
            default=["yes", "no"],
            format_func=lambda x: "Com histórico" if x == "yes" else "Sem histórico",
        )
        mostrar_sintetico = st.radio(
            "Origem dos dados",
            ["Todos", "Apenas originais", "Apenas sintéticos (SMOTE)"], index=0
        )
        st.caption("65% dos dados são sintéticos (SMOTE).")
        st.markdown("---")
        st.caption(f"Dataset total: **{len(df):,}** pacientes.")

    # Aplicar filtros
    dff = df[
        df["Gender"].isin(filtro_genero) &
        df["Obesity"].isin(filtro_classe) &
        df["Age"].between(filtro_idade[0], filtro_idade[1]) &
        df["FAF"].isin(filtro_faf) &
        df["family_history"].isin(filtro_fam)
    ].copy()
    if mostrar_sintetico == "Apenas originais":
        dff = dff[~dff["sintetico"]]
    elif mostrar_sintetico == "Apenas sintéticos (SMOTE)":
        dff = dff[dff["sintetico"]]

    if dff.empty:
        st.warning("Nenhum dado com os filtros selecionados. Ajuste os filtros na barra lateral.")
        st.stop()

    n_filtrado = len(dff)
    pct_total  = n_filtrado / len(df) * 100

    # ── TÍTULO + CONTAGEM ─────────────────────────────────────────────────────
    st.markdown(f'<div class="section-title">📊 Visão Geral — <span style="color:#00838f">{n_filtrado:,} pacientes</span> ({pct_total:.1f}% do total)</div>', unsafe_allow_html=True)

    # ── KPIs ──────────────────────────────────────────────────────────────────
    k1, k2, k3, k4, k5, k6 = st.columns(6)
    obese_pct  = dff["Obesity"].isin(["Obesity_Type_I","Obesity_Type_II","Obesity_Type_III"]).mean()*100
    over_pct   = dff["Obesity"].isin(["Overweight_Level_I","Overweight_Level_II"]).mean()*100
    normal_pct = (dff["Obesity"]=="Normal_Weight").mean()*100
    sed_pct    = dff["sedentary"].mean()*100
    avg_hs     = dff["healthy_score"].mean()
    fam_pct    = (dff["family_history"]=="yes").mean()*100

    for col, val, lbl, color_cls in [
        (k1, f"{n_filtrado:,}",        "👥 Pacientes",       "kpi-card-blue"),
        (k2, f"{obese_pct:.1f}%",      "⚠️ Com Obesidade",   "kpi-card-red"),
        (k3, f"{over_pct:.1f}%",       "🟡 Com Sobrepeso",   "kpi-card-yellow"),
        (k4, f"{normal_pct:.1f}%",     "✅ Peso Normal",      "kpi-card-green"),
        (k5, f"{avg_hs:.1f}/10",       "💚 Score Hábitos",   "kpi-card-teal"),
        (k6, f"{fam_pct:.1f}%",        "🧬 Hist. Familiar",  "kpi-card-purple"),
    ]:
        col.markdown(
            f'<div class="kpi-card {color_cls}"><div class="val">{val}</div>'
            f'<div class="lbl">{lbl}</div></div>',
            unsafe_allow_html=True,
        )

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 1 — DISTRIBUIÇÃO
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">📈 Distribuição dos Pacientes</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([3, 2])

    with c1:
        contagem = dff["Obesity_PT"].value_counts().reindex(ORDEM_PT).dropna()
        fig, ax = plt.subplots(figsize=(8, 4))
        bars = ax.bar(contagem.index, contagem.values,
                      color=[PALETTE_PT.get(c, "#999") for c in contagem.index], edgecolor="white")
        for bar in bars:
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2, str(int(bar.get_height())),
                    ha="center", va="bottom", fontsize=9)
        ax.set_title("Pacientes por Nível de Obesidade", fontsize=11, fontweight="bold")
        ax.set_ylabel("Pacientes"); ax.tick_params(axis="x", rotation=25)
        ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    with c2:
        gen_ob = dff.groupby(["Obesity_PT","Gender"]).size().unstack(fill_value=0)
        if "Female" in gen_ob.columns:
            gen_ob = gen_ob.rename(columns={"Female":"Feminino"})
        if "Male" in gen_ob.columns:
            gen_ob = gen_ob.rename(columns={"Male":"Masculino"})
        gen_ob = gen_ob.reindex(ORDEM_PT).dropna()
        fig, ax = plt.subplots(figsize=(5, 4))
        colors_gen = []
        for col in gen_ob.columns:
            colors_gen.append("#e91e63" if col == "Feminino" else "#1565c0")
        gen_ob.plot(kind="barh", ax=ax, color=colors_gen[:len(gen_ob.columns)], edgecolor="white")
        ax.set_title("Distribuição por Gênero", fontsize=11, fontweight="bold")
        ax.set_xlabel("Pacientes"); ax.set_ylabel("")
        ax.legend(title="Gênero", fontsize=8); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 2 — DISTRIBUIÇÕES CONTÍNUAS
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">📐 Distribuição de Idade, Altura e Peso</div>', unsafe_allow_html=True)

    cA, cB, cC = st.columns(3)

    with cA:
        fig, ax = plt.subplots(figsize=(5, 3.5))
        for cls in ORDER_CLS:
            subset = dff[dff["Obesity"] == cls]["Age"]
            if len(subset) > 1:
                sns.kdeplot(subset, ax=ax, label=LABEL_PT[cls],
                            color=PALETTE_DICT[cls], fill=True, alpha=0.25, linewidth=1.5)
        ax.set_title("Distribuição de Idade por Classe", fontsize=10, fontweight="bold")
        ax.set_xlabel("Idade"); ax.set_ylabel("Densidade")
        ax.legend(fontsize=6, loc="upper right"); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    with cB:
        fig, ax = plt.subplots(figsize=(5, 3.5))
        for cls in ORDER_CLS:
            subset = dff[dff["Obesity"] == cls]["Height"]
            if len(subset) > 1:
                sns.kdeplot(subset, ax=ax, label=LABEL_PT[cls],
                            color=PALETTE_DICT[cls], fill=True, alpha=0.25, linewidth=1.5)
        ax.set_title("Distribuição de Altura por Classe", fontsize=10, fontweight="bold")
        ax.set_xlabel("Altura (m)"); ax.set_ylabel("Densidade")
        ax.legend(fontsize=6); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    with cC:
        fig, ax = plt.subplots(figsize=(5, 3.5))
        for cls in ORDER_CLS:
            subset = dff[dff["Obesity"] == cls]["Weight"]
            if len(subset) > 1:
                sns.kdeplot(subset, ax=ax, label=LABEL_PT[cls],
                            color=PALETTE_DICT[cls], fill=True, alpha=0.25, linewidth=1.5)
        ax.set_title("Distribuição de Peso por Classe", fontsize=10, fontweight="bold")
        ax.set_xlabel("Peso (kg)"); ax.set_ylabel("Densidade")
        ax.legend(fontsize=6); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 3 — GRÁFICO EXPLORATÓRIO INTERATIVO
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">🔭 Exploração Interativa — Escolha os Gráficos</div>', unsafe_allow_html=True)
    st.caption("Selecione quais análises exibir lado a lado.")

    GRAFICOS_DISP = [
        "Distribuição por Nível de Obesidade",
        "Prevalência por Gênero",
        "Score de Hábitos Saudáveis",
        "Atividade Física × Obesidade",
        "Histórico Familiar × Obesidade",
        "Heatmap de Correlação com Target",
        "Sedentarismo por Classe",
        "Consumo de Álcool × Obesidade",
        "Razão Refeições / Atividade",
        "Consumo de Água por Classe",
        "Consumo de Vegetais por Classe",
    ]

    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        grafico_esq = st.selectbox("📈 Gráfico — esquerda", GRAFICOS_DISP, index=0)
    with col_sel2:
        grafico_dir = st.selectbox("📈 Gráfico — direita",  GRAFICOS_DISP, index=2)

    def render_grafico(nome: str, ax, df_plot: pd.DataFrame):
        classes_presentes = [c for c in ORDER_CLS if c in df_plot["Obesity"].unique()]
        palette_atual     = [PALETTE_DICT[c] for c in classes_presentes]
        labels_presentes  = [LABEL_PT[c] for c in classes_presentes]

        if nome == "Distribuição por Nível de Obesidade":
            counts = df_plot["Obesity"].value_counts().reindex(classes_presentes)
            ax.barh(labels_presentes, counts.values, color=palette_atual)
            for i, v in enumerate(counts.values):
                ax.text(v + 2, i, str(int(v)), va="center", fontsize=8)
            ax.set_xlabel("Nº de Pacientes")

        elif nome == "Prevalência por Gênero":
            for gdr, color, lbl in [("Male","#1565c0","Masculino"),("Female","#e91e63","Feminino")]:
                sub = (df_plot[df_plot["Gender"]==gdr]["Obesity"]
                       .value_counts().reindex(classes_presentes).fillna(0))
                ax.plot(labels_presentes, sub.values, marker="o",
                        label=lbl, color=color, linewidth=2)
            ax.set_xticklabels(labels_presentes, rotation=30, ha="right", fontsize=8)
            ax.set_ylabel("Nº de Pacientes"); ax.legend()

        elif nome == "Score de Hábitos Saudáveis":
            hs = df_plot.groupby("Obesity")["healthy_score"].mean().reindex(classes_presentes)
            bars = ax.barh(labels_presentes, hs.values, color=palette_atual, alpha=0.9)
            for i, v in enumerate(hs.values):
                ax.text(v + 0.05, i, f"{v:.1f}", va="center", fontsize=8)
            ax.set_xlim(0, 10); ax.set_xlabel("Score médio (0–10)")

        elif nome == "Atividade Física × Obesidade":
            faf_lbl = {0:"Nenhuma",1:"1-2x/sem",2:"3-4x/sem",3:"5x+/sem"}
            df2 = df_plot.copy()
            df2["FAF_label"] = df2["FAF"].map(faf_lbl)
            faf_pct = df2.groupby(["FAF_label","Obesity"]).size().reset_index(name="Count")
            faf_pct["Pct"] = faf_pct["Count"] / faf_pct.groupby("FAF_label")["Count"].transform("sum") * 100
            pivot = faf_pct.pivot(index="Obesity", columns="FAF_label", values="Pct").fillna(0)
            pivot.index = [LABEL_PT.get(i,i) for i in pivot.index]
            pivot.T.plot(kind="bar", ax=ax, colormap="RdYlGn_r", width=0.7)
            ax.set_ylabel("% dentro do grupo")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right", fontsize=8)
            ax.legend(fontsize=6, bbox_to_anchor=(1,1))

        elif nome == "Histórico Familiar × Obesidade":
            fam_pct = df_plot.groupby(["family_history","Obesity"]).size().reset_index(name="Count")
            fam_pct["Pct"] = fam_pct["Count"] / fam_pct.groupby("family_history")["Count"].transform("sum") * 100
            pivot2 = fam_pct.pivot(index="Obesity", columns="family_history", values="Pct").fillna(0)
            pivot2.index = [LABEL_PT.get(i,i) for i in pivot2.index]
            pivot2.plot(kind="barh", ax=ax, color=["#ef9a9a","#1565c0"], width=0.6)
            ax.set_xlabel("% dentro do grupo")
            ax.legend(["Sem histórico","Com histórico"], fontsize=9)

        elif nome == "Heatmap de Correlação com Target":
            df_corr = df_plot.copy()
            df_corr["Obesity"] = LabelEncoder().fit_transform(df_corr["Obesity"].astype(str))
            for c in ["Gender","family_history","FAVC","CAEC","SMOKE",
                      "SCC","CALC","MTRANS","age_group","age_group_display","Obesity_PT","sintetico"]:
                if c in df_corr.columns:
                    df_corr[c] = LabelEncoder().fit_transform(df_corr[c].astype(str))
            df_heat = df_corr.select_dtypes(include="number")
            drop_cols = [c for c in ["FAF_label","Height","Weight"] if c in df_heat.columns]
            df_heat = df_heat.drop(columns=drop_cols)
            corr_t = (df_heat.corr(method="spearman")[["Obesity"]]
                      .drop("Obesity", errors="ignore").sort_values("Obesity", ascending=False))
            sns.heatmap(corr_t.T, ax=ax, cmap="coolwarm", center=0,
                        vmin=-1, vmax=1, annot=True, fmt=".2f",
                        annot_kws={"size":7}, linewidths=0.3,
                        cbar_kws={"shrink":0.5})
            ax.set_yticklabels(["Obesity"], rotation=0, fontsize=8)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=7)

        elif nome == "Sedentarismo por Classe":
            sed = df_plot.groupby("Obesity")["sedentary"].mean().reindex(classes_presentes) * 100
            ax.barh(labels_presentes, sed.values, color="#e53935", alpha=0.8)
            for i, v in enumerate(sed.values):
                ax.text(v + 0.5, i, f"{v:.1f}%", va="center", fontsize=8)
            ax.set_xlabel("% sedentários"); ax.set_xlim(0, 100)

        elif nome == "Consumo de Álcool × Obesidade":
            alc = df_plot.groupby("Obesity")["high_alcohol"].mean().reindex(classes_presentes) * 100
            ax.barh(labels_presentes, alc.values, color="#00838f", alpha=0.85)
            for i, v in enumerate(alc.values):
                ax.text(v + 0.5, i, f"{v:.1f}%", va="center", fontsize=8)
            ax.set_xlabel("% consumo elevado de álcool"); ax.set_xlim(0, 100)

        elif nome == "Razão Refeições / Atividade":
            mar = df_plot.groupby("Obesity")["meal_activity_ratio"].mean().reindex(classes_presentes)
            ax.barh(labels_presentes, mar.values, color=palette_atual, alpha=0.9)
            for i, v in enumerate(mar.values):
                ax.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=8)
            ax.set_xlabel("Razão média (maior = mais desequilibrado)")

        elif nome == "Consumo de Água por Classe":
            agua = df_plot.groupby("Obesity")["CH2O"].mean().reindex(classes_presentes)
            ax.barh(labels_presentes, agua.values, color=palette_atual, alpha=0.9)
            for i, v in enumerate(agua.values):
                ax.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=8)
            ax.set_xlim(0, 3); ax.set_xlabel("Consumo médio (0–3)")

        elif nome == "Consumo de Vegetais por Classe":
            veg = df_plot.groupby("Obesity")["FCVC"].mean().reindex(classes_presentes)
            ax.barh(labels_presentes, veg.values, color=palette_atual, alpha=0.9)
            for i, v in enumerate(veg.values):
                ax.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=8)
            ax.set_xlim(0, 3); ax.set_xlabel("Frequência média (0–3)")

        ax.set_title(nome, fontsize=10, fontweight="bold")
        ax.spines[["top","right"]].set_visible(False)

    col_ga, col_gb = st.columns(2)
    with col_ga:
        fig, ax = plt.subplots(figsize=(7, 4))
        render_grafico(grafico_esq, ax, dff)
        plt.tight_layout(); st.pyplot(fig); plt.close()
    with col_gb:
        fig, ax = plt.subplots(figsize=(7, 4))
        render_grafico(grafico_dir, ax, dff)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 4 — FEATURES ENGINEERED
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">🔬 Features Criadas no Modelo</div>', unsafe_allow_html=True)
    c3, c4, c5 = st.columns(3)

    with c3:
        hs = dff.groupby("Obesity_PT")["healthy_score"].mean().reindex(ORDEM_PT).dropna()
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.barh(hs.index, hs.values, color=[PALETTE_PT.get(c,"#999") for c in hs.index], alpha=0.9)
        for i, v in enumerate(hs.values):
            ax.text(v + 0.05, i, f"{v:.1f}", va="center", fontsize=8)
        ax.set_title("Score Médio de Hábitos\n(0=pior | 10=melhor)", fontsize=10, fontweight="bold")
        ax.set_xlabel("Score"); ax.set_xlim(0, 10); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    with c4:
        sed = dff.groupby("Obesity_PT")["sedentary"].mean().reindex(ORDEM_PT).dropna() * 100
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.barh(sed.index, sed.values, color=[PALETTE_PT.get(c,"#999") for c in sed.index], alpha=0.9)
        for i, v in enumerate(sed.values):
            ax.text(v + 0.5, i, f"{v:.1f}%", va="center", fontsize=8)
        ax.set_title("% Sedentários\n(FAF=0 e TUE≥1)", fontsize=10, fontweight="bold")
        ax.set_xlabel("%"); ax.set_xlim(0, 100); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    with c5:
        mar = dff.groupby("Obesity_PT")["meal_activity_ratio"].mean().reindex(ORDEM_PT).dropna()
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.barh(mar.index, mar.values, color=[PALETTE_PT.get(c,"#999") for c in mar.index], alpha=0.9)
        for i, v in enumerate(mar.values):
            ax.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=8)
        ax.set_title("Razão Refeições/Atividade\n(maior = mais desequilibrado)", fontsize=10, fontweight="bold")
        ax.set_xlabel("Razão"); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 5 — HÁBITOS ALIMENTARES
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">🥗 Hábitos Alimentares</div>', unsafe_allow_html=True)
    c6, c7, c8 = st.columns(3)

    with c6:
        fam = dff.groupby("Obesity_PT")["fam_x_favc"].mean().reindex(ORDEM_PT).dropna() * 100
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.barh(fam.index, fam.values, color=[PALETTE_PT.get(c,"#999") for c in fam.index], alpha=0.9)
        for i, v in enumerate(fam.values):
            ax.text(v + 0.5, i, f"{v:.1f}%", va="center", fontsize=8)
        ax.set_title("% Hist. Familiar\n× Alimentos Calóricos", fontsize=10, fontweight="bold")
        ax.set_xlabel("%"); ax.set_xlim(0, 100); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    with c7:
        veg = dff.groupby("Obesity_PT")["FCVC"].mean().reindex(ORDEM_PT).dropna()
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.barh(veg.index, veg.values, color=[PALETTE_PT.get(c,"#999") for c in veg.index], alpha=0.9)
        for i, v in enumerate(veg.values):
            ax.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=8)
        ax.set_title("Consumo Médio de Vegetais\n(0–3)", fontsize=10, fontweight="bold")
        ax.set_xlabel("Frequência"); ax.set_xlim(0, 3); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    with c8:
        alc = dff.groupby("Obesity_PT")["high_alcohol"].mean().reindex(ORDEM_PT).dropna() * 100
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.barh(alc.index, alc.values, color=[PALETTE_PT.get(c,"#999") for c in alc.index], alpha=0.9)
        for i, v in enumerate(alc.values):
            ax.text(v + 0.5, i, f"{v:.1f}%", va="center", fontsize=8)
        ax.set_title("% Alto Consumo de Álcool", fontsize=10, fontweight="bold")
        ax.set_xlabel("%"); ax.set_xlim(0, 100); ax.spines[["top","right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 6 — FAIXA ETÁRIA E TRANSPORTE
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">🚗 Faixa Etária e Transporte</div>', unsafe_allow_html=True)
    c9, c10 = st.columns(2)

    with c9:
        ordem_age = ["Adolescente","Jovem Adulto","Adulto","Meia-idade","Idoso"]
        ag = dff.groupby(["age_group_display","Obesity_PT"]).size().unstack(fill_value=0)
        ag = ag.reindex([a for a in ordem_age if a in ag.index])
        if not ag.empty:
            ag_pct = ag.div(ag.sum(axis=1), axis=0) * 100
            fig, ax = plt.subplots(figsize=(7, 4))
            ag_pct.plot(kind="bar", ax=ax,
                        color=[PALETTE_PT.get(c,"#999") for c in ag_pct.columns],
                        edgecolor="white", stacked=True)
            ax.set_title("Obesidade por Faixa Etária (%)", fontsize=11, fontweight="bold")
            ax.set_xlabel("Faixa Etária"); ax.set_ylabel("%")
            ax.tick_params(axis="x", rotation=30)
            ax.legend(title="Nível", fontsize=7, bbox_to_anchor=(1.01,1), loc="upper left")
            ax.spines[["top","right"]].set_visible(False)
            plt.tight_layout(); st.pyplot(fig); plt.close()

    with c10:
        TRANSP_PT = {"Public_Transportation":"Transp. Público","Walking":"Caminhando",
                     "Automobile":"Carro","Motorbike":"Moto","Bike":"Bicicleta"}
        TRANSP_CORES = {
            "Transp. Público": "#1565c0",
            "Caminhando"      : "#43A047",
            "Carro"           : "#FB8C00",
            "Moto"            : "#E53935",
            "Bicicleta"       : "#00838f",
        }
        transp = dff["MTRANS"].value_counts().sort_values(ascending=True)
        transp.index = [TRANSP_PT.get(i, i) for i in transp.index]
        cores_transp = [TRANSP_CORES.get(i, "#888") for i in transp.index]
        fig, ax = plt.subplots(figsize=(5, 4))
        bars = ax.barh(transp.index, transp.values, color=cores_transp, edgecolor="white")
        for bar in bars:
            ax.text(bar.get_width() + max(transp.values) * 0.01, bar.get_y() + bar.get_height() / 2,
                    str(int(bar.get_width())), va="center", fontsize=9)
        ax.set_title("Meio de Transporte Habitual", fontsize=11, fontweight="bold")
        ax.set_xlabel("Nº de Pacientes")
        ax.spines[["top", "right"]].set_visible(False)
        plt.tight_layout(); st.pyplot(fig); plt.close()

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 7 — COMPOSIÇÃO DO DATASET
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">🔍 Composição do Dataset</div>', unsafe_allow_html=True)
    c11, c12 = st.columns(2)

    with c11:
        n_orig = (~df_global["sintetico"]).sum()
        n_sint = df_global["sintetico"].sum()
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.pie([n_orig, n_sint],
               labels=[f"Originais ({n_orig})", f"SMOTE ({n_sint})"],
               colors=["#1565c0","#e53935"], autopct="%1.1f%%", startangle=90)
        ax.set_title("Dados Originais vs Sintéticos", fontsize=11, fontweight="bold")
        plt.tight_layout(); st.pyplot(fig); plt.close()

    with c12:
        st.info(
            f"**Por que existem dados sintéticos?**\n\n"
            f"O dataset distribuído pelo UCI já vem com dados sintéticos incorporados: "
            f"os autores aplicaram **SMOTE** (Synthetic Minority Oversampling Technique) "
            f"para balancear as classes antes da publicação, totalizando **{len(df_global):,} registros**.\n\n"
            f"A separação entre originais e sintéticos é feita aqui por uma **heurística**: "
            f"registros com idade não-inteira (ex: 21.4) tendem a ser gerados pelo SMOTE, "
            f"pois a técnica interpola valores entre amostras reais. "
            f"Por esse critério, identificamos **{n_orig} registros como originais** e "
            f"**{n_sint} como sintéticos** — números aproximados, não exatos.\n\n"
            f"Nos filtros laterais é possível explorar apenas os dados classificados como originais."
        )

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 8 — DESEMPENHO DO MODELO
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">🤖 Desempenho do Modelo</div>', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    for col, val, lbl in [
        (m1, f"{meta['test_accuracy']:.1%}", "Acurácia (Teste)"),
        (m2, f"{meta['auc_roc']:.3f}",        "AUC-ROC (OvR)"),
        (m3, f"{meta['f1_macro']:.3f}",        "F1-Score Macro"),
        (m4, meta["best_model_name"],           "Melhor Modelo"),
    ]:
        col.markdown(
            f'<div class="kpi-card"><div class="val" style="font-size:1.3rem">{val}</div>'
            f'<div class="lbl">{lbl}</div></div>',
            unsafe_allow_html=True,
        )

    st.divider()

    # ══════════════════════════════════════════════════════════════════════════
    # SEÇÃO 9 — INSIGHTS CLÍNICOS
    # ══════════════════════════════════════════════════════════════════════════
    st.markdown('<div class="section-title">💡 Principais Insights para a Equipe Médica</div>', unsafe_allow_html=True)

    col_i1, col_i2 = st.columns(2)
    with col_i1:
        st.markdown('<div class="insight-success">💚 <b>Score de Hábitos Saudáveis</b><br>Pacientes com peso normal apresentam score significativamente maior. Hidratação, consumo de vegetais e atividade física são fatores modificáveis de fácil intervenção clínica.</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight-success">🥦 <b>Consumo de Vegetais</b><br>Quanto mais grave a obesidade, menor o consumo médio de vegetais. Orientação nutricional com foco em fibras e micronutrientes deve ser prioridade no plano terapêutico.</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight"><b>👨‍👩‍👧 Histórico Familiar × Alimentação</b><br>A combinação de histórico familiar positivo com alimentos calóricos é mais prevalente nos casos graves. Pacientes com esse perfil precisam de acompanhamento redobrado e triagem precoce.</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight">🚶 <b>Transporte Ativo</b><br>Pacientes que caminham ou usam bicicleta como transporte habitual apresentam menores taxas de obesidade. O incentivo ao deslocamento ativo é uma intervenção de baixo custo e alto impacto.</div>', unsafe_allow_html=True)
    with col_i2:
        st.markdown('<div class="insight-warn">🛋️ <b>Sedentarismo</b><br>Obesidade Tipo II e III concentram a maior proporção de pacientes sedentários. Intervenções de incentivo ao movimento físico, mesmo que leve, são altamente recomendadas nesse grupo.</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight-warn">🍽️ <b>Razão Refeições / Atividade</b><br>O desequilíbrio entre calorias ingeridas e gasto energético cresce com a gravidade da obesidade. Reduzir refeições ou aumentar atividade pode ter impacto direto no controle do peso.</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight-alert">🍺 <b>Álcool</b><br>O consumo frequente de álcool está associado aos níveis mais graves de obesidade. A triagem alcoólica deve integrar a avaliação de risco metabólico de rotina.</div>', unsafe_allow_html=True)
        st.markdown('<div class="insight-alert">📱 <b>Tempo de Tela</b><br>Alto tempo de uso de dispositivos (>5h/dia) combinado com ausência de atividade física cria um perfil de risco elevado. Recomenda-se avaliação do comportamento digital como parte do histórico clínico.</div>', unsafe_allow_html=True)

    st.divider()

    # ── Tabela de dados filtrados ─────────────────────────────────────────────
    with st.expander("📄 Ver tabela de dados filtrados"):
        cols_exibir = ["Gender","Age","age_group_display","Height","Weight","family_history",
                       "FAVC","FCVC","FAF","CH2O","TUE","healthy_score","sedentary","Obesity_PT"]
        rename = {
            "Gender":"Gênero","Age":"Idade","age_group_display":"Faixa Etária",
            "Height":"Altura","Weight":"Peso","family_history":"Hist. Familiar",
            "FAVC":"Alim. Calóricos","FCVC":"Vegetais","FAF":"Ativ. Física","CH2O":"Água",
            "TUE":"Tempo Telas","healthy_score":"Score Hábitos","sedentary":"Sedentário","Obesity_PT":"Nível"
        }
        exibir = dff[[c for c in cols_exibir if c in dff.columns]].rename(columns=rename)
        exibir["Gênero"] = exibir["Gênero"].map({"Male":"Masculino","Female":"Feminino"})
        st.dataframe(exibir, use_container_width=True, hide_index=True)
        st.caption(f"{n_filtrado:,} registros exibidos ({pct_total:.1f}% do total).")

    st.caption("📊 POSTECH Tech Challenge Fase 04 — Data Analytics")

# ╔══════════════════════════════════════════════════════════════════════════════
# ║  ABA 3 — COMO FUNCIONA
# ╚══════════════════════════════════════════════════════════════════════════════
with tab3:

    st.markdown('<div class="section-title">🧠 Como o ObesityAI Foi Construído</div>', unsafe_allow_html=True)
    st.markdown(
        "Esta página explica, em linguagem acessível, o **caminho completo** desde os dados brutos "
        "até a ferramenta interativa que você está usando — sem precisar saber programar."
    )
    st.divider()

    # ── Etapa 1 — Dados ───────────────────────────────────────────────────────
    st.markdown("### 1️⃣ De onde vêm os dados?")
    col_d1, col_d2 = st.columns([2,1])
    with col_d1:
        st.markdown("""
<div class="timeline-step">
<h4>📦 Dataset: UCI Obesity Estimation</h4>
<p>Os dados originais foram coletados por pesquisadores da Colômbia, Peru e México e publicados no repositório da UCI (Universidade da Califórnia). O dataset contém <b>2.111 registros</b> e <b>17 variáveis</b> sobre hábitos alimentares, estilo de vida e nível de obesidade de indivíduos entre 14 e 61 anos.</p>
</div>

<div class="timeline-step">
<h4>⚗️ SMOTE — Dados Sintéticos</h4>
<p>O dataset original tinha apenas ~498 registros reais. Para treinar o modelo com mais exemplos balanceados por classe, os autores aplicaram <b>SMOTE</b> (Synthetic Minority Oversampling Technique) — uma técnica que cria registros artificiais com características semelhantes aos dados reais. Isso explica as acurácias mais altas. No dashboard, é possível filtrar apenas os dados originais.</p>
</div>
        """, unsafe_allow_html=True)
    with col_d2:
        n_orig = (~df_global["sintetico"]).sum()
        n_sint = df_global["sintetico"].sum()
        st.markdown(f"""
<div class="kpi-card kpi-card-blue">
  <div class="val">{len(df_global):,}</div>
  <div class="lbl">Total de registros</div>
</div>
<div class="kpi-card kpi-card-green">
  <div class="val">{n_orig}</div>
  <div class="lbl">Registros originais</div>
</div>
<div class="kpi-card kpi-card-red">
  <div class="val">{n_sint:,}</div>
  <div class="lbl">Gerados por SMOTE</div>
</div>
<div class="kpi-card kpi-card-purple">
  <div class="val">7</div>
  <div class="lbl">Classes de obesidade</div>
</div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── Etapa 2 — Variáveis ───────────────────────────────────────────────────
    st.markdown("### 2️⃣ O que foi medido?")

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown("**🔢 Variáveis do questionário**")
        variaveis = [
            ("👤 Gênero", "Masculino ou Feminino"),
            ("📅 Idade", "Idade em anos"),
            ("📏 Altura / ⚖️ Peso", "Usados só para calcular o IMC informativo — não entram no modelo"),
            ("👨‍👩‍👧 Histórico familiar", "Parentes com excesso de peso?"),
            ("🍔 FAVC", "Come alimentos calóricos com frequência?"),
            ("🥦 FCVC", "Com que frequência come vegetais? (0–3)"),
            ("🍽️ NCP", "Número de refeições principais por dia"),
            ("🍩 CAEC", "Come entre as refeições? (Nunca → Sempre)"),
            ("🚬 SMOKE", "Fuma?"),
            ("💧 CH2O", "Litros de água por dia (0–3)"),
            ("📊 SCC", "Monitora calorias?"),
            ("🏋️ FAF", "Dias de atividade física por semana (0–3)"),
            ("📱 TUE", "Horas em telas por dia (0–3)"),
            ("🍺 CALC", "Frequência de consumo de álcool"),
            ("🚗 MTRANS", "Meio de transporte habitual"),
        ]
        for var, desc in variaveis:
            st.markdown(f'<span class="tag">{var}</span> {desc}  ', unsafe_allow_html=True)

    with col_v2:
        st.markdown("**🛠️ Features criadas pela equipe (Feature Engineering)**")
        st.markdown("""
<div class="timeline-step">
<h4>🧮 O que é Feature Engineering?</h4>
<p>Além das variáveis originais, criamos novas métricas que combinam informações para capturar padrões mais complexos. Essas features foram fundamentais para melhorar a precisão do modelo.</p>
</div>
        """, unsafe_allow_html=True)
        features_eng = [
            ("age_group", "Faixa etária categórica derivada da idade", "tag"),
            ("healthy_score", "Score 0–10 que combina água, vegetais, atividade vs. álcool e junk food", "tag-green"),
            ("sedentary", "1 se FAF=0 e TUE≥1 (sem exercício e muito tempo em telas)", "tag-orange"),
            ("fam_x_favc", "Risco combinado: histórico familiar E alimentos calóricos", "tag-orange"),
            ("meal_activity_ratio", "Razão entre refeições e atividade física — desequilíbrio calórico", "tag-orange"),
            ("high_alcohol", "1 se consumo de álcool for frequente ou sempre", "tag-orange"),
            ("CAEC_num / CALC_num", "Versão numérica das variáveis ordinais de snacking e álcool", "tag"),
        ]
        for feat, desc, cls in features_eng:
            st.markdown(f'<span class="tag {cls}">{feat}</span> {desc}  <br>', unsafe_allow_html=True)

    st.divider()

    # ── Etapa 3 — Por que remover Altura e Peso? ──────────────────────────────
    st.markdown("### 3️⃣ Por que Altura e Peso foram removidos do modelo?")
    st.markdown("""
<div class="timeline-step" style="border-left-color:#e53935;">
<h4>⚠️ Data Leakage — O que é e por que é problemático?</h4>
<p>O <b>IMC (Índice de Massa Corporal)</b> é calculado com base em peso e altura, e é exatamente o critério usado para classificar os níveis de obesidade. Se deixássemos essas variáveis no modelo, ele "trapacearia": em vez de aprender padrões de comportamento, simplesmente recalcularia o IMC e acertaria quase 100% — sem nenhuma utilidade clínica real.</p>
<p style="margin-top:.5rem">Ao remover altura e peso, forçamos o modelo a aprender com <b>hábitos de vida</b> (alimentação, exercício, hidratação, sono, etc.), tornando a ferramenta genuinamente útil para intervenção preventiva.</p>
</div>
    """, unsafe_allow_html=True)

    col_lk1, col_lk2 = st.columns(2)
    with col_lk1:
        st.error("**🚫 COM altura e peso no modelo**\n\n~99% de acurácia, mas sem utilidade prática. O modelo apenas calcula o IMC automaticamente — qualquer médico já faria isso com uma calculadora.")
    with col_lk2:
        st.success("**✅ SEM altura e peso (nossa abordagem)**\n\n~79% de acurácia, mas com alto valor clínico: o modelo identifica perfis de risco por comportamento, permitindo intervenção preventiva antes que a obesidade se instale.")

    st.divider()

    # ── Etapa 4 — Modelos testados ────────────────────────────────────────────
    st.markdown("### 4️⃣ Quais algoritmos foram testados?")
    st.markdown("Cinco algoritmos de machine learning foram treinados e comparados. O vencedor foi selecionado com base na acurácia no conjunto de teste.")

    model_results = meta.get("model_results", {})
    modelos_info = {
        "Logistic Regression": ("📏", "Modelo linear simples — útil como baseline. Assume relações lineares entre variáveis.", "#1565c0"),
        "Random Forest": ("🌲", "Conjunto de árvores de decisão. Robusto e resistente a overfitting.", "#2e7d32"),
        "Gradient Boosting": ("⚡", "Árvores construídas sequencialmente, corrigindo os erros da anterior.", "#e65100"),
        "Hist Gradient Boosting": ("🏆", "Versão otimizada do Gradient Boosting — mais rápido e com melhor regularização.", "#7b1fa2"),
        "SVM": ("🔵", "Support Vector Machine. Encontra a fronteira de decisão de margem máxima.", "#00838f"),
    }

    for nome, res in model_results.items():
        info = modelos_info.get(nome, ("🤖", nome, "#607d8b"))
        is_best = nome == meta.get("best_model_name","")
        border = "border:2px solid #7b1fa2;" if is_best else ""
        badge  = " 🏆 <b style='color:#7b1fa2'>SELECIONADO</b>" if is_best else ""
        st.markdown(f"""
<div class="timeline-step" style="{border}">
<h4>{info[0]} {nome}{badge}</h4>
<p style="margin-bottom:.4rem">{info[1]}</p>
<span class="tag">CV: {res['cv_mean']:.1%} ±{res['cv_std']:.1%}</span>
<span class="tag tag-green">Teste: {res['test_acc']:.1%}</span>
<span class="tag tag-purple">AUC-ROC: {res['auc_roc']:.3f}</span>
<span class="tag tag-orange">F1-Macro: {res['f1_macro']:.3f}</span>
</div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── Etapa 5 — Pipeline ────────────────────────────────────────────────────
    st.markdown("### 5️⃣ Como o modelo foi preparado para o deploy?")

    etapas_pipeline = [
        ("📥", "Coleta dos Dados", "O arquivo Obesity.csv foi carregado e inspecionado. Verificamos tipos de dados, valores ausentes e distribuição das classes.", "#1565c0"),
        ("🛠️", "Feature Engineering", "Criamos 7 novas features que combinam variáveis originais para capturar padrões mais ricos: score de hábitos, sedentarismo, risco combinado genético-alimentar e outras.", "#2e7d32"),
        ("✂️", "Divisão Treino / Teste", "Os dados foram divididos: 80% para treinar os modelos e 20% para testar o desempenho em dados nunca vistos antes. Usamos estratificação por classe para garantir proporções iguais.", "#e65100"),
        ("🔄", "Pré-processamento", "Variáveis numéricas foram normalizadas com StandardScaler. Variáveis categóricas foram codificadas com OneHotEncoder. Tudo dentro de um Pipeline sklearn para evitar vazamento de dados.", "#00838f"),
        ("🏋️", "Treinamento e Validação Cruzada", "Cada modelo foi avaliado com validação cruzada de 5 folds (StratifiedKFold). Isso nos dá uma estimativa mais confiável do desempenho real.", "#7b1fa2"),
        ("🏆", "Seleção do Melhor Modelo", "O Hist Gradient Boosting foi selecionado com 79.2% de acurácia, AUC-ROC de 0.966 e F1-macro de 0.79 — o melhor equilíbrio entre precisão e generalização.", "#c62828"),
        ("💾", "Exportação dos Artefatos", "O pipeline completo (pré-processamento + modelo) foi serializado com joblib e codificado em Base64 para facilitar o deploy. O LabelEncoder e os metadados foram salvos separadamente.", "#455a64"),
        ("🚀", "Deploy com Streamlit", "O arquivo app.py carrega os artefatos, recebe o formulário do usuário, aplica as mesmas transformações do treinamento e retorna a predição com probabilidades por classe.", "#1565c0"),
    ]

    for i, (icon, titulo, desc, cor) in enumerate(etapas_pipeline, 1):
        st.markdown(f"""
<div class="timeline-step" style="border-left-color:{cor};">
<h4>{icon} Etapa {i}: {titulo}</h4>
<p>{desc}</p>
</div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── Etapa 6 — Interpretando o resultado ───────────────────────────────────
    st.markdown("### 6️⃣ Como interpretar o resultado da predição?")

    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.markdown("""
<div class="timeline-step">
<h4>📊 O que é a "Confiança do modelo"?</h4>
<p>O modelo retorna a probabilidade de pertencer a cada uma das 7 classes. A "confiança" é a probabilidade da classe predita — quanto maior, mais o modelo está "seguro" de sua resposta. Valores acima de 70% indicam alta confiança.</p>
</div>

<div class="timeline-step">
<h4>🧬 O que é o Score de Hábitos Saudáveis?</h4>
<p>É uma métrica de 0 a 10 criada pela equipe que combina fatores positivos (água, vegetais, exercício) e negativos (snacking excessivo, álcool, alimentos calóricos). Serve como indicador imediato da qualidade de vida do paciente.</p>
</div>
        """, unsafe_allow_html=True)
    with col_r2:
        st.markdown("""
<div class="timeline-step">
<h4>⚠️ Limitações importantes</h4>
<p>• O modelo foi treinado com dados da América Latina — pode ter viés geográfico.<br>
• 65% dos dados são sintéticos (SMOTE) — as acurácias podem estar superestimadas.<br>
• O modelo <b>não substitui</b> avaliação clínica, exames laboratoriais ou anamnese detalhada.<br>
• Alturas e pesos não entram no cálculo — por design, para evitar leakage.</p>
</div>

<div class="timeline-step">
<h4>✅ Quando usar esta ferramenta?</h4>
<p>• Triagem inicial em consultas preventivas.<br>
• Identificação de perfis de risco comportamental.<br>
• Acompanhamento longitudinal de mudanças de hábito.<br>
• Educação e conscientização do paciente sobre fatores de risco.</p>
</div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── Rodapé informativo ─────────────────────────────────────────────────────
    st.markdown("""
<div style="background:linear-gradient(135deg,#0d1b2a,#1b2d45); border-radius:12px; padding:1.2rem 1.8rem; color:white; margin-top:1rem;">
  <b style="font-size:1rem">📚 Referências e Tecnologias Utilizadas</b><br><br>
  <span class="tag">Python 3.11</span>
  <span class="tag">Streamlit</span>
  <span class="tag">scikit-learn</span>
  <span class="tag">pandas</span>
  <span class="tag">numpy</span>
  <span class="tag">matplotlib</span>
  <span class="tag">seaborn</span>
  <span class="tag">joblib</span>
  <br><br>
  <span style="opacity:.7; font-size:.82rem">
  </span>
</div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# RODAPÉ GLOBAL
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:#aaa;font-size:0.78rem;'>"
    "ObesityAI · FIAP POSTECH Data Analytics · Tech Challenge Fase 4 · "
    "⚠️ Ferramenta de apoio — não substitui diagnóstico médico."
    "</div>",
    unsafe_allow_html=True,
)
