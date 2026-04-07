import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import re
import base64
import warnings
warnings.filterwarnings("ignore")

# ─── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Udemy Competition Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding: 1.2rem 2rem 2rem; }

.app-header {
    background: linear-gradient(135deg, #0f3460 0%, #185FA5 70%, #2176c4 100%);
    border-radius: 14px; padding: 18px 28px; margin-bottom: 1.4rem;
    display: flex; align-items: center; justify-content: space-between;
}
.app-header h1 { color:#fff; font-size:20px; font-weight:600; margin:0; }
.app-header p  { color:rgba(255,255,255,0.65); font-size:12px; margin:4px 0 0; }
.header-badge  {
    background:rgba(255,255,255,0.15); color:#fff; font-size:11px;
    padding:4px 14px; border-radius:20px; border:1px solid rgba(255,255,255,0.25);
    white-space:nowrap;
}
.kpi-wrap { display:flex; gap:10px; margin-bottom:1rem; flex-wrap:wrap; }
.kpi-card {
    flex:1; min-width:110px;
    background:#f0f6ff; border:1px solid #c7ddf8;
    border-radius:12px; padding:12px 14px; text-align:center;
}
.kpi-card .val { font-size:20px; font-weight:600; color:#0f3460; line-height:1.2; }
.kpi-card .lbl { font-size:10px; color:#5a7a99; margin-top:3px; text-transform:uppercase; letter-spacing:.04em; }
.sec-hdr {
    font-size:12px; font-weight:600; color:#0f3460;
    text-transform:uppercase; letter-spacing:.06em;
    border-left:3px solid #185FA5; padding-left:9px;
    margin: 1.2rem 0 .7rem;
}
.insight {
    background:#eff6ff; border-left:4px solid #185FA5;
    border-radius:0 10px 10px 0; padding:11px 15px;
    font-size:13px; color:#1e3a5f; line-height:1.6; margin-top:.6rem;
}
.pred-box {
    background:linear-gradient(135deg,#dbeafe,#eff6ff);
    border:1.5px solid #93c5fd; border-radius:14px;
    padding:22px 28px; margin-bottom:1rem;
}
.pred-box .big { font-size:52px; font-weight:700; color:#1e40af; line-height:1; }
.pred-box .sub { font-size:13px; color:#3b82f6; margin-top:6px; }
.pred-box .tag { font-size:11px; color:#3b82f6; font-weight:500; margin-bottom:4px; }
.pred-box .conf{ font-size:26px; font-weight:600; color:#1e40af; }

/* Recommendation Card Styles - Fixed */
.rec-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.rec-card:hover {
    border-color: #185FA5;
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(24,95,165,0.1);
}
.rec-card-inner {
    display: flex;
    align-items: center;
    gap: 16px;
}
.rank-badge {
    display: inline-flex;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 700;
    flex-shrink: 0;
}
.r1 { background: linear-gradient(135deg, #fef3c7, #fde68a); color: #92400e; }
.r2 { background: linear-gradient(135deg, #dbeafe, #bfdbfe); color: #1e40af; }
.r3 { background: linear-gradient(135deg, #dcfce7, #bbf7d0); color: #166534; }
.rec-content {
    flex: 1;
    min-width: 0;
}
.rec-title {
    font-size: 15px;
    font-weight: 600;
    color: #0f3460;
    margin-bottom: 8px;
    line-height: 1.4;
}
.rec-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 6px;
}
.pill {
    display: inline-block;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 20px;
    background: #f1f5f9;
    color: #475569;
}
.pill-subject { background: #dbeafe; color: #1e40af; }
.pill-level { background: #f1f5f9; color: #475569; }
.pill-duration { background: #e0e7ff; color: #4338ca; }
.pill-subscribers { background: #dcfce7; color: #166534; }
.pill-price-paid { background: #fef3c7; color: #92400e; }
.pill-price-free { background: #dcfce7; color: #166534; font-weight: 600; }
.rec-score {
    text-align: right;
    flex-shrink: 0;
}
.score-value {
    font-size: 24px;
    font-weight: 700;
    color: #185FA5;
}
.score-label {
    font-size: 10px;
    color: #94a3b8;
    margin-top: 4px;
}
.match-bar {
    width: 80px;
    height: 4px;
    background: #e2e8f0;
    border-radius: 4px;
    margin-top: 8px;
    overflow: hidden;
}
.match-bar-fill {
    height: 100%;
    background: #185FA5;
    border-radius: 4px;
    transition: width 0.3s ease;
}
.stTabs [data-baseweb="tab-list"] { gap: 4px; border-bottom: 1px solid #e2e8f0; }
.stTabs [data-baseweb="tab"] { font-size: 13px; font-weight: 500; padding: 8px 18px; border-radius: 8px 8px 0 0; color: #64748b; }
.stTabs [aria-selected="true"] { color: #185FA5 !important; border-bottom: 2px solid #185FA5 !important; }
hr { border: none; border-top: 1px solid #e2e8f0; margin: .8rem 0; }

/* Sidebar styles */
[data-testid="stSidebar"] {
    background: #f0f6ff;
    border-right: 1px solid #c7ddf8;
}
[data-testid="stSidebar"] .block-container { padding: 1rem; }
.sb-logo-box {
    background: linear-gradient(135deg,#0f3460,#185FA5);
    border-radius: 12px; padding: 18px 16px; text-align: center; margin-bottom: 14px;
}
.sb-logo-box .title { color: #fff; font-size: 16px; font-weight: 600; margin: 8px 0 4px; }
.sb-logo-box .sub { color: rgba(255,255,255,0.65); font-size: 11px; line-height: 1.5; }
.sb-section {
    font-size: 10px; font-weight: 600; color: #185FA5;
    text-transform: uppercase; letter-spacing: .08em;
    margin: 14px 0 6px;
}
.sb-divider { border: none; border-top: 1px solid #c7ddf8; margin: 12px 0; }
.sb-stat { display: flex; justify-content: space-between; align-items: center; padding: 5px 0; font-size: 12px; }
.sb-stat .sk { color: #5a7a99; }
.sb-stat .sv { color: #0f3460; font-weight: 500; }
.filter-note {
    background: #e0f2fe;
    border-left: 4px solid #0284c7;
    padding: 8px 12px;
    font-size: 11px;
    color: #0c4a6e;
    margin-top: 10px;
    border-radius: 4px;
}

/* Footer with larger name */
.footer-credit {
    text-align: center;
    padding: 16px 0 8px 0;
    border-top: 1px solid #c7ddf8;
    margin-top: 16px;
}
.credit-name {
    font-size: 18px;
    font-weight: 700;
    color: #185FA5;
    text-decoration: none;
    transition: all 0.3s ease;
    display: inline-block;
}
.credit-name:hover {
    color: #0f3460;
    transform: scale(1.05);
}
.credit-title {
    font-size: 12px;
    color: #5a7a99;
    margin-top: 5px;
}
.credit-heart {
    font-size: 14px;
    color: #ef4444;
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════
SUBJECT_COLORS = {
    "Web Development":    "#185FA5",
    "Business Finance":   "#2E7D32",
    "Graphic Design":     "#E65100",
    "Musical Instruments": "#6A1B9A",
}
LEVEL_COLORS = {
    "All Levels":         "#185FA5",
    "Beginner Level":     "#2E7D32",
    "Intermediate Level": "#E65100",
    "Expert Level":       "#C62828",
}
BASE = dict(
    font_family="DM Sans",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor ="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=40, b=10),
    legend=dict(bgcolor="rgba(255,255,255,0.85)",
                bordercolor="#e2e8f0", borderwidth=1, font_size=11),
)

def kpi(val, lbl):
    return f'<div class="kpi-card"><div class="val">{val}</div><div class="lbl">{lbl}</div></div>'

def sec(title):
    st.markdown(f'<div class="sec-hdr">{title}</div>', unsafe_allow_html=True)

def clean_text(t):
    t = str(t).lower()
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

# ─── Load Udemy logo as base64 ───────────────────────────────────────────
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return data
    except Exception:
        return None

LOGO_B64 = get_image_base64("udemy_logo.jpg")


# ═══════════════════════════════════════════════════════════════════════════
# DATA LOADING
# ═══════════════════════════════════════════════════════════════════════════
@st.cache_data
def load_data():
    df = pd.read_csv("udemy_courses_cleaned.csv")
    df["published"] = pd.to_datetime(df["published"])
    df = df.set_index("published")
    return df


# ─── Price prediction model ──────────────────────────────────────────────
@st.cache_resource
def build_price_model(_df):
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    data = _df.copy().reset_index()
    data = data[data["price"] > 0].dropna(
        subset=["subject", "level", "content_duration_cat",
                "num_lectures", "content_duration", "year", "quarter"])

    data["lectures_per_hour"] = data["num_lectures"] / (data["content_duration"] + 0.1)
    data["is_long_course"]    = (data["content_duration"] > 10).astype(int)

    level_dummies   = pd.get_dummies(data["level"],   prefix="level",   drop_first=True)
    subject_dummies = pd.get_dummies(data["subject"], prefix="subject", drop_first=True)

    base_feats = ["num_lectures", "content_duration", "year", "quarter",
                  "is_long_course", "lectures_per_hour"]
    feat_cols  = base_feats + list(level_dummies.columns) + list(subject_dummies.columns)

    X = pd.concat([
        data[base_feats].reset_index(drop=True),
        level_dummies.reset_index(drop=True),
        subject_dummies.reset_index(drop=True),
    ], axis=1)
    y = data["price"].reset_index(drop=True)

    xmm = MinMaxScaler(); ymm = MinMaxScaler()
    X_s = xmm.fit_transform(X)
    y_s = ymm.fit_transform(y.values.reshape(-1, 1)).ravel()

    X_tr, X_te, y_tr, y_te = train_test_split(X_s, y_s, test_size=0.2, random_state=42)

    try:
        from xgboost import XGBRegressor
        model = XGBRegressor(n_estimators=500, learning_rate=0.05,
                             max_depth=5, subsample=0.8,
                             colsample_bytree=0.8, random_state=42, verbosity=0)
        algo_name = "XGBoost"
    except ImportError:
        from sklearn.ensemble import GradientBoostingRegressor
        model = GradientBoostingRegressor(n_estimators=300, learning_rate=0.05,
                                          max_depth=5, random_state=42)
        algo_name = "Gradient Boosting"

    model.fit(X_tr, y_tr)

    y_pred_s = model.predict(X_te)
    y_pred   = ymm.inverse_transform(y_pred_s.reshape(-1, 1)).ravel()
    y_true   = ymm.inverse_transform(y_te.reshape(-1, 1)).ravel()

    metrics = dict(
        r2      = round(r2_score(y_true, y_pred), 3),
        mae     = round(mean_absolute_error(y_true, y_pred), 2),
        rmse    = round(mean_squared_error(y_true, y_pred) ** 0.5, 2),
        algo    = algo_name,
        y_true  = y_true,
        y_pred  = y_pred,
    )
    importances = dict(zip(feat_cols, model.feature_importances_))
    return model, xmm, ymm, feat_cols, \
           level_dummies.columns.tolist(), subject_dummies.columns.tolist(), \
           metrics, importances


# ─── Recommender ─────────────────────────────────────────────────────────
@st.cache_resource
def build_recommender(_df):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    rdf = _df.reset_index()[
        ["course_title", "subject", "level", "content_duration_cat",
         "price", "is_paid", "num_subscribers", "num_lectures",
         "profit", "num_reviews"]
    ].drop_duplicates("course_title").reset_index(drop=True)

    def build_soup(row):
        t = clean_text(row["course_title"])
        s = clean_text(row["subject"])
        l = clean_text(row["level"])
        return f"{t} {t} {t} {s} {s} {l}"

    rdf["clean_title"] = rdf["course_title"].apply(clean_text)
    rdf["soup"]        = rdf.apply(build_soup, axis=1)

    tfidf = TfidfVectorizer(analyzer="word", ngram_range=(1, 2),
                            min_df=1, stop_words="english", sublinear_tf=True)
    mat   = tfidf.fit_transform(rdf["soup"])
    sim   = cosine_similarity(mat, mat)
    idx   = pd.Series(rdf.index,
                      index=rdf["course_title"].str.lower()).drop_duplicates()
    return rdf, tfidf, sim, idx


# ═══════════════════════════════════════════════════════════════════════════
# LOAD ALL
# ═══════════════════════════════════════════════════════════════════════════
df = load_data()
(model, xmm, ymm, feat_cols,
 level_cols, subject_cols,
 metrics, importances) = build_price_model(df)
rdf, tfidf_rec, sim_matrix, rec_idx = build_recommender(df)

ALL_SUBJECTS = sorted(df["subject"].unique().tolist())
ALL_LEVELS   = sorted(df["level"].unique().tolist())

# ═══════════════════════════════════════════════════════════════════════════
# SESSION STATE – filter defaults (Only for Tab 1 & Tab 2)
# ═══════════════════════════════════════════════════════════════════════════
DEFAULTS = {
    "sb_subjects": [],
    "sb_levels": [],
    "sb_type": "All",
    "sb_yr_min": 2012,
    "sb_yr_max": 2017,
}

for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════
with st.sidebar:
    # Udemy logo
    if LOGO_B64:
        st.markdown(f"""
        <div class="sb-logo-box">
            <img src="data:image/jpeg;base64,{LOGO_B64}"
                 style="width:100%; max-width:180px; border-radius:12px;
                        margin-bottom:12px; background:#fff; padding:8px;" />
            <div class="title">Udemy Competition<br>Analysis</div>
            <div class="sub">Strategic market intelligence</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="sb-logo-box">
            <div style="font-size:48px">📚</div>
            <div class="title">Udemy Competition Analysis</div>
            <div class="sub">Strategic market intelligence</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section">About this project</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:12px;color:#334155;background:#fff;border-radius:10px;
                padding:12px 14px;border:1px solid #c7ddf8;">
        A full <b>competition analysis</b> of Udemy's course catalog (2012–2017)
        designed to help a new e-learning startup understand market dynamics.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section">Dataset snapshot</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:#fff;border-radius:10px;padding:10px 14px;border:1px solid #c7ddf8;">
        <div class="sb-stat"><span class="sk">Total courses</span><span class="sv">2,782</span></div>
        <div class="sb-stat"><span class="sk">Subjects</span><span class="sv">4</span></div>
        <div class="sb-stat"><span class="sk">Years covered</span><span class="sv">2012–2017</span></div>
        <div class="sb-stat"><span class="sk">Total profit</span><span class="sv">$163M</span></div>
        <div class="sb-stat"><span class="sk">Total subscribers</span><span class="sv">2.46M</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sb-section">🔎 Global filters</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:11px;color:#64748b;margin-bottom:8px">⚠️ Applied only to first two tabs</div>', unsafe_allow_html=True)

    selected_subjects = st.multiselect("Subject", options=ALL_SUBJECTS, default=st.session_state["sb_subjects"], key="subj_filter")
    st.session_state["sb_subjects"] = selected_subjects

    selected_type = st.radio("Course type", ["All", "Paid", "Free"], index=["All", "Paid", "Free"].index(st.session_state["sb_type"]), horizontal=True, key="type_filter")
    st.session_state["sb_type"] = selected_type

    selected_levels = st.multiselect("Course level", options=ALL_LEVELS, default=st.session_state["sb_levels"], key="level_filter")
    st.session_state["sb_levels"] = selected_levels

    yr_range = st.slider("Year range", 2012, 2017, (st.session_state["sb_yr_min"], st.session_state["sb_yr_max"]), key="year_filter")
    st.session_state["sb_yr_min"] = yr_range[0]
    st.session_state["sb_yr_max"] = yr_range[1]

    st.markdown("""
    <div class="filter-note">
    ℹ️ <b>Note:</b> These filters only apply to Subject Analysis & Profit/Subscribers tabs.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    # Footer with LARGER NAME
    st.markdown("""
    <div class="footer-credit">
        <a href="https://www.linkedin.com/in/abdallah-ibrahim-mohamed-4556792a5" 
           target="_blank" 
           class="credit-name">
            Eng.Abdallah Ibrahim
        </a>
        <div class="credit-title">
            <span class="credit-heart">❤️</span> Data Science & AI Engineer
        </div>
    </div>
    """, unsafe_allow_html=True)


# Get filter values
SB_SUBJECTS = st.session_state["sb_subjects"]
SB_LEVELS = st.session_state["sb_levels"]
SB_TYPE = st.session_state["sb_type"]
SB_YR_MIN = st.session_state["sb_yr_min"]
SB_YR_MAX = st.session_state["sb_yr_max"]


# ═══════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="app-header">
    <div>
        <h1>📊 Udemy Competition Analysis</h1>
        <p>Strategic insights to help you launch a smarter online course platform</p>
    </div>
    <span class="header-badge">Competition Analysis · 2012–2017</span>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
# TABS
# ═══════════════════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Subject Analysis",
    "💰 Profit & Subscribers",
    "🤖 Price Prediction",
    "🎯 Recommendation System",
])


# ────────────────────────────────────────────────────────────────────────────
# TAB 1 – SUBJECT ANALYSIS
# ────────────────────────────────────────────────────────────────────────────
with tab1:
    dff = df.copy()
    if SB_SUBJECTS:
        dff = dff[dff["subject"].isin(SB_SUBJECTS)]
    if SB_TYPE == "Paid":
        dff = dff[dff["is_paid"] == True]
    elif SB_TYPE == "Free":
        dff = dff[dff["is_paid"] == False]
    if SB_LEVELS:
        dff = dff[dff["level"].isin(SB_LEVELS)]

    avg_p = dff[dff["price"] > 0]["price"].mean()
    free_n = (dff["is_paid"] == False).sum()

    st.markdown(
        '<div class="kpi-wrap">'
        + kpi(f"{len(dff):,}", "Total Courses")
        + kpi(f"{dff['subject'].nunique()}", "Unique Subjects")
        + kpi(f"${avg_p:.0f}" if not np.isnan(avg_p) else "N/A", "AVG Price")
        + kpi(f"${dff['profit'].sum()/1e6:.1f}M", "Profit")
        + kpi(f"{dff['num_subscribers'].sum()/1e6:.2f}M", "Subscribers")
        + kpi(f"{free_n:,}", "Free Courses")
        + '</div>', unsafe_allow_html=True)

    sec("Courses & profit per subject")
    c1, c2 = st.columns(2)
    with c1:
        g = dff["subject"].value_counts().reset_index()
        g.columns = ["subject", "count"]
        fig = px.bar(g.sort_values("count"), x="count", y="subject", orientation="h",
                     color="subject", color_discrete_map=SUBJECT_COLORS,
                     title="Number of courses per subject")
        fig.update_layout(**BASE, showlegend=False, height=280)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        g2 = dff.groupby("subject")["profit"].sum().reset_index().sort_values("profit")
        fig2 = px.bar(g2, x="profit", y="subject", orientation="h",
                      color="subject", color_discrete_map=SUBJECT_COLORS,
                      title="Total profit per subject")
        fig2.update_layout(**BASE, showlegend=False, height=280, xaxis_tickformat="$,.0f")
        st.plotly_chart(fig2, use_container_width=True)

    sec("Profit by year & subscribers by price category")
    c3, c4 = st.columns(2)
    with c3:
        g3 = dff.reset_index().groupby(["subject", "year"])["profit"].sum().reset_index()
        fig3 = px.bar(g3, x="subject", y="profit", color="year", barmode="group",
                      title="Profit by subject and year")
        fig3.update_layout(**BASE, height=300, xaxis_tickangle=-20, yaxis_tickformat="$,.0f")
        st.plotly_chart(fig3, use_container_width=True)
    with c4:
        if "price_cat" in dff.columns:
            g4 = dff.reset_index().groupby(["subject", "price_cat"])["num_subscribers"].sum().reset_index()
            fig4 = px.bar(g4, x="subject", y="num_subscribers", color="price_cat", barmode="group",
                          title="Subscribers by subject and price category")
            fig4.update_layout(**BASE, height=300, xaxis_tickangle=-20, yaxis_tickformat=",")
            st.plotly_chart(fig4, use_container_width=True)

    sec("Subscribers by content duration & course level")
    c5, c6 = st.columns(2)
    with c5:
        if "content_duration_cat" in dff.columns:
            dur_order = ["0 : 1", "1 : 3", "3 : 7", "7 : 12", "12 : 20", "+20"]
            g5 = dff.reset_index().groupby(["subject", "content_duration_cat"])["num_subscribers"].sum().reset_index()
            g5["content_duration_cat"] = pd.Categorical(g5["content_duration_cat"], categories=dur_order, ordered=True)
            g5 = g5.sort_values("content_duration_cat")
            fig5 = px.bar(g5, x="subject", y="num_subscribers", color="content_duration_cat", barmode="stack",
                          title="Subscribers by subject and content duration")
            fig5.update_layout(**BASE, height=300, xaxis_tickangle=-20, yaxis_tickformat=",")
            st.plotly_chart(fig5, use_container_width=True)
    with c6:
        g6 = dff.groupby(["subject", "level"])["num_subscribers"].sum().reset_index()
        fig6 = px.bar(g6, x="subject", y="num_subscribers", color="level", barmode="stack",
                      color_discrete_map=LEVEL_COLORS, title="Subscribers by subject and level")
        fig6.update_layout(**BASE, height=300, xaxis_tickangle=-20, yaxis_tickformat=",")
        st.plotly_chart(fig6, use_container_width=True)


# ────────────────────────────────────────────────────────────────────────────
# TAB 2 – PROFIT & SUBSCRIBERS
# ────────────────────────────────────────────────────────────────────────────
with tab2:
    dft = df.copy()
    dft = dft[(dft.index.year >= SB_YR_MIN) & (dft.index.year <= SB_YR_MAX)]
    if SB_SUBJECTS:
        dft = dft[dft["subject"].isin(SB_SUBJECTS)]
    if SB_LEVELS:
        dft = dft[dft["level"].isin(SB_LEVELS)]

    peak_yr = (dft.resample("YE")["profit"].sum().idxmax().year if len(dft) > 0 else "N/A")
    st.markdown(
        '<div class="kpi-wrap">'
        + kpi(f"${dft['profit'].sum()/1e6:.1f}M", "Total Profit")
        + kpi(str(peak_yr), "Peak Profit Year")
        + kpi(f"{dft['num_subscribers'].sum()/1e6:.2f}M", "Total Subscribers")
        + kpi(f"{dft['num_reviews'].sum()/1e3:.1f}K", "Total Reviews")
        + '</div>', unsafe_allow_html=True)

    sec("📈 Profit Analysis")
    df_g = dft.resample("ME")["profit"].sum().reset_index()
    fig_p1 = px.line(df_g, x="published", y="profit", title="Monthly total profit over time", markers=True)
    fig_p1.update_traces(line_color="#185FA5", line_width=2.5)
    fig_p1.update_layout(**BASE, height=300, yaxis_tickformat="$,.0f")
    st.plotly_chart(fig_p1, use_container_width=True)

    pc1, pc2 = st.columns(2)
    with pc1:
        df_g2 = dft.groupby([pd.Grouper(freq="ME"), "level"])["profit"].sum().reset_index()
        fig_p2 = px.line(df_g2, x="published", y="profit", color="level", title="Monthly profit by level", color_discrete_map=LEVEL_COLORS)
        fig_p2.update_layout(**BASE, height=320, yaxis_tickformat="$,.0f")
        st.plotly_chart(fig_p2, use_container_width=True)
    with pc2:
        df_g3 = dft.groupby([pd.Grouper(freq="ME"), "subject"])["profit"].sum().reset_index()
        fig_p3 = px.line(df_g3, x="published", y="profit", color="subject", title="Monthly profit by subject", color_discrete_map=SUBJECT_COLORS)
        fig_p3.update_layout(**BASE, height=320, yaxis_tickformat="$,.0f")
        st.plotly_chart(fig_p3, use_container_width=True)

    sec("👥 Subscribers Analysis")
    df_g4 = dft.resample("ME")["num_subscribers"].sum().reset_index()
    fig_s1 = px.line(df_g4, x="published", y="num_subscribers", title="Monthly subscribers over time", markers=True)
    fig_s1.update_traces(line_color="#2E7D32", line_width=2.5)
    fig_s1.update_layout(**BASE, height=300, yaxis_tickformat=",")
    st.plotly_chart(fig_s1, use_container_width=True)

    sc1, sc2 = st.columns(2)
    with sc1:
        df_g5 = dft.groupby([pd.Grouper(freq="ME"), "subject"])["num_subscribers"].sum().reset_index()
        fig_s2 = px.line(df_g5, x="published", y="num_subscribers", color="subject", title="Monthly subscribers by subject", color_discrete_map=SUBJECT_COLORS)
        fig_s2.update_layout(**BASE, height=320, yaxis_tickformat=",")
        st.plotly_chart(fig_s2, use_container_width=True)
    with sc2:
        df_g6 = dft.groupby([pd.Grouper(freq="ME"), "level"])["num_subscribers"].sum().reset_index()
        fig_s3 = px.line(df_g6, x="published", y="num_subscribers", color="level", title="Monthly subscribers by level", color_discrete_map=LEVEL_COLORS)
        fig_s3.update_layout(**BASE, height=320, yaxis_tickformat=",")
        st.plotly_chart(fig_s3, use_container_width=True)


# ────────────────────────────────────────────────────────────────────────────
# TAB 3 – PRICE PREDICTION
# ────────────────────────────────────────────────────────────────────────────
with tab3:
    sec("Model performance")
    mk1, mk2, mk3 = st.columns(3)
    for col, (v, l) in zip([mk1, mk2, mk3],
        [(f"${metrics['mae']}", "MAE"),
         (f"${metrics['rmse']}", "RMSE"),
         (metrics["algo"], "Best Algorithm")]):
        col.markdown(f'<div class="kpi-card"><div class="val">{v}</div><div class="lbl">{l}</div></div>', unsafe_allow_html=True)

    sec("Enter course details")
    with st.form("price_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            p_subject = st.selectbox("Subject", sorted(df["subject"].unique().tolist()))
            p_level = st.selectbox("Course Level", sorted(df["level"].unique().tolist()))
            p_cont_dur = st.number_input("Duration (hours)", min_value=0.5, max_value=50.0, value=2.0, step=0.5)
        with col_b:
            p_lectures = st.number_input("Number of Lectures", min_value=1, max_value=500, value=24, step=1)
            p_year = st.selectbox("Publication Year", sorted(df["year"].unique().tolist(), reverse=True))
            p_quarter = st.selectbox("Quarter", [1, 2, 3, 4], index=1)
        submitted = st.form_submit_button("🔮 Predict Price", use_container_width=True)

    if submitted:
        lph = p_lectures / (p_cont_dur + 0.1)
        ilc = int(p_cont_dur > 10)
        row = {c: 0 for c in feat_cols}
        row["num_lectures"] = p_lectures
        row["content_duration"] = p_cont_dur
        row["year"] = p_year
        row["quarter"] = p_quarter
        row["is_long_course"] = ilc
        row["lectures_per_hour"] = lph
        lk, sk = f"level_{p_level}", f"subject_{p_subject}"
        if lk in row: row[lk] = 1
        if sk in row: row[sk] = 1
        X_in = pd.DataFrame([row])[feat_cols]
        X_sc = xmm.transform(X_in)
        pred = float(ymm.inverse_transform(model.predict(X_sc).reshape(-1, 1))[0][0])
        st.markdown(f"""
        <div class="pred-box">
            <div style="display:flex;justify-content:space-between;align-items:center">
                <div>
                    <div class="tag">PREDICTED OPTIMAL PRICE</div>
                    <div class="big">${pred:.0f}</div>

        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
# TAB 4 – RECOMMENDATION SYSTEM (FIXED - 3 recommendations only)
# ═══════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown(
        '<div class="kpi-wrap">'
        + kpi(f"{len(rdf):,}", "Courses Indexed")
        + kpi("TF-IDF + Cosine", "Similarity Method")
        + kpi("Content-Based", "Algorithm Type")
        + '</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="insight">
        ℹ️ Each course is encoded using <b>TF-IDF with bigrams</b> on title, subject, and level.
        Recommendations are ranked by <b>cosine similarity</b> to your preferences.
    </div>
    """, unsafe_allow_html=True)

    sec("Enter your preferences")

    with st.form("rec_form"):
        ra, rb, rc = st.columns(3)
        with ra:
            r_query = st.text_input("🔍 Search keyword or course title", placeholder="e.g., python web development")
            r_subject = st.multiselect("Subject", options=sorted(rdf["subject"].unique().tolist()), default=[])
        with rb:
            r_level = st.multiselect("Skill level", options=sorted(rdf["level"].unique().tolist()), default=[])
            r_type = st.radio("Course type", ["All", "Paid only", "Free only"], horizontal=True)
        with rc:
            r_budget = st.slider("Max budget ($)", 0, 200, 200, step=5)
            r_sort = st.selectbox("Sort by", ["Most subscribers", "Highest profit", "Lowest price", "Highest similarity"])
            # CHANGED: Default to 3 recommendations
            r_top_n = st.slider("Number of results", 1, 5, 3)
        rec_btn = st.form_submit_button("🎯 Get Recommendations", use_container_width=True)

    def get_recs(query, subjects_f, levels_f, max_p, ctype, sort_by, top_n):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        
        q_clean = clean_text(query) if query.strip() else "general online course"
        corpus = rdf["soup"].tolist() + [q_clean]
        vec = TfidfVectorizer(analyzer="word", ngram_range=(1, 2), min_df=1, stop_words="english", sublinear_tf=True)
        mat = vec.fit_transform(corpus)
        scores = cosine_similarity(mat[-1], mat[:-1]).flatten()
        
        res = rdf.copy()
        res["similarity_score"] = scores
        
        if subjects_f and len(subjects_f) > 0:
            res = res[res["subject"].isin(subjects_f)]
        if levels_f and len(levels_f) > 0:
            res = res[res["level"].isin(levels_f)]
        if ctype == "Paid only":
            res = res[res["is_paid"] == True]
        elif ctype == "Free only":
            res = res[res["is_paid"] == False]
        res = res[res["price"] <= max_p]
        
        sort_map = {
            "Most subscribers": ("num_subscribers", False),
            "Highest profit": ("profit", False),
            "Lowest price": ("price", True),
            "Highest similarity": ("similarity_score", False),
        }
        col, asc = sort_map[sort_by]
        return res.sort_values(col, ascending=asc).head(top_n).reset_index(drop=True)

    if rec_btn:
        with st.spinner("Finding best matching courses..."):
            recs = get_recs(r_query, r_subject, r_level, r_budget, r_type, r_sort, r_top_n)

        if recs.empty:
            st.warning("No courses match your filters. Try adjusting your preferences.")
        else:
            sec(f"🎯 Top {len(recs)} Recommended Courses")
            
            # Display recommendations using proper st.markdown with HTML
            for i, row in recs.iterrows():
                rank = i + 1
                rank_class = ["r1", "r2", "r3"][i] if i < 3 else "r3"
                price_class = "pill-price-free" if not row["is_paid"] else "pill-price-paid"
                price_text = "Free" if not row["is_paid"] else f"${row['price']}"
                similarity_pct = min(99, int(row["similarity_score"] * 100 + 35))
                
                # Using proper HTML with st.markdown
                st.markdown(f"""
                <div class="rec-card">
                    <div class="rec-card-inner">
                        <div class="rank-badge {rank_class}">#{rank}</div>
                        <div class="rec-content">
                            <div class="rec-title">{row['course_title'][:100]}{'...' if len(row['course_title']) > 100 else ''}</div>
                            <div class="rec-tags">
                                <span class="pill pill-subject">{row['subject']}</span>
                                <span class="pill pill-level">{row['level']}</span>
                                <span class="pill pill-duration">{row['content_duration_cat']}h</span>
                                <span class="pill pill-subscribers">{row['num_subscribers']:,} students</span>
                                <span class="pill {price_class}">{price_text}</span>
                            </div>
                        </div>
                        <div class="rec-score">
                            <div class="score-value">{similarity_pct}%</div>
                            <div class="score-label">match</div>
                            <div class="match-bar">
                                <div class="match-bar-fill" style="width:{similarity_pct}%"></div>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Show analysis charts
            sec("Results Analysis")
            rc1, rc2 = st.columns(2)
            with rc1:
                fig_r1 = px.bar(recs, x=[f"#{i+1}" for i in range(len(recs))], y="num_subscribers",
                                title="Subscriber count by rank", color_discrete_sequence=["#185FA5"])
                fig_r1.update_layout(**BASE, height=280, yaxis_tickformat=",", xaxis_title="Rank", yaxis_title="Subscribers")
                st.plotly_chart(fig_r1, use_container_width=True)
            with rc2:
                fig_r2 = px.scatter(recs, x="price", y="num_subscribers", size="num_subscribers",
                                    color="subject", color_discrete_map=SUBJECT_COLORS,
                                    title="Price vs Subscribers", hover_data=["course_title"])
                fig_r2.update_layout(**BASE, height=280, yaxis_tickformat=",")
                st.plotly_chart(fig_r2, use_container_width=True)
            
            st.markdown("""
            <div class="insight">
                💡 <b>Business insight:</b> Top competitors offer free or budget-friendly courses ($0-50)
                with high subscriber counts. Consider a <b>freemium strategy</b> for your platform launch.
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("👆 Fill in your preferences and click **Get Recommendations**.")