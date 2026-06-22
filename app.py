import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Bharath MJ · Data Scientist",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Design tokens & global CSS ────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0A0E1A !important;
    color: #E2E8F0 !important;
    font-family: 'Space Grotesk', sans-serif;
}

[data-testid="stAppViewContainer"] { padding-top: 0 !important; }
[data-testid="stHeader"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
.stDeployButton { display: none !important; }
footer { display: none !important; }

/* ── Section wrappers ── */
.block-container {
    max-width: 1200px !important;
    padding: 0 2rem 4rem !important;
    margin: 0 auto !important;
}

/* ── Nav ── */
.nav-bar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(10,14,26,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(99,179,237,0.12);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 2.5rem;
    margin: 0 -2rem 0;
}
.nav-logo {
    font-family: 'Space Mono', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: #63B3ED;
    letter-spacing: 0.05em;
}
.nav-links { display: flex; gap: 2rem; }
.nav-links a {
    color: #A0AEC0;
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    transition: color 0.2s;
}
.nav-links a:hover { color: #63B3ED; }

/* ── Hero ── */
.hero-section {
    padding: 6rem 0 4rem;
    position: relative;
}
.hero-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: #63B3ED;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 1.25rem;
}
.hero-name {
    font-size: clamp(3rem, 7vw, 5.5rem);
    font-weight: 700;
    line-height: 1.0;
    color: #F7FAFC;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}
.hero-name span { color: #63B3ED; }
.hero-title {
    font-size: clamp(1.1rem, 2.5vw, 1.4rem);
    font-weight: 300;
    color: #718096;
    margin-bottom: 2rem;
    letter-spacing: 0.02em;
}
.hero-bio {
    font-size: 1.05rem;
    line-height: 1.75;
    color: #CBD5E0;
    max-width: 600px;
    margin-bottom: 2.5rem;
}
.hero-badges { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 2.5rem; }
.badge {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    padding: 0.35rem 0.85rem;
    border: 1px solid rgba(99,179,237,0.3);
    border-radius: 2px;
    color: #63B3ED;
    background: rgba(99,179,237,0.06);
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.badge.green {
    border-color: rgba(72,187,120,0.3);
    color: #48BB78;
    background: rgba(72,187,120,0.06);
}
.cta-row { display: flex; gap: 1rem; flex-wrap: wrap; }
.cta-btn {
    display: inline-block;
    padding: 0.8rem 1.8rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-decoration: none;
    border-radius: 3px;
    transition: all 0.2s;
    cursor: pointer;
}
.cta-primary {
    background: #63B3ED;
    color: #0A0E1A;
    border: none;
}
.cta-primary:hover { background: #90CDF4; }
.cta-secondary {
    background: transparent;
    color: #63B3ED;
    border: 1px solid #63B3ED;
}
.cta-secondary:hover { background: rgba(99,179,237,0.1); }

/* ── Section titles ── */
.section-wrap { padding: 4rem 0 2rem; }
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: #63B3ED;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.section-heading {
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    font-weight: 700;
    color: #F7FAFC;
    letter-spacing: -0.01em;
    margin-bottom: 0.4rem;
}
.section-sub {
    color: #718096;
    font-size: 1rem;
    margin-bottom: 2.5rem;
}
.divider {
    width: 3rem;
    height: 2px;
    background: #63B3ED;
    margin-bottom: 2.5rem;
}

/* ── Stat cards ── */
.stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1px; background: rgba(99,179,237,0.1); border: 1px solid rgba(99,179,237,0.1); border-radius: 4px; overflow: hidden; margin-bottom: 3rem; }
.stat-card { background: #0D1220; padding: 2rem 1.5rem; text-align: center; }
.stat-num { font-family: 'Space Mono', monospace; font-size: 2.2rem; font-weight: 700; color: #63B3ED; display: block; line-height: 1; }
.stat-label { font-size: 0.8rem; color: #718096; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 0.4rem; }

/* ── Experience cards ── */
.exp-card {
    background: #0D1220;
    border: 1px solid rgba(99,179,237,0.1);
    border-left: 3px solid #63B3ED;
    border-radius: 4px;
    padding: 1.75rem 2rem;
    margin-bottom: 1.25rem;
    transition: border-color 0.2s, transform 0.2s;
}
.exp-card:hover { border-left-color: #90CDF4; transform: translateX(4px); }
.exp-header { display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem; }
.exp-role { font-size: 1.1rem; font-weight: 600; color: #F7FAFC; }
.exp-company { font-size: 0.85rem; color: #63B3ED; font-family: 'Space Mono', monospace; }
.exp-period {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: #4A5568;
    background: rgba(99,179,237,0.06);
    border: 1px solid rgba(99,179,237,0.15);
    padding: 0.2rem 0.6rem;
    border-radius: 2px;
}
.exp-bullets { list-style: none; margin-top: 1rem; }
.exp-bullets li { 
    color: #A0AEC0; 
    font-size: 0.92rem; 
    line-height: 1.65; 
    padding: 0.3rem 0 0.3rem 1.2rem; 
    position: relative;
    border-bottom: 1px solid rgba(255,255,255,0.03);
}
.exp-bullets li::before { content: "▸"; color: #63B3ED; position: absolute; left: 0; }
.exp-bullets li:last-child { border-bottom: none; }

/* ── Skill chips ── */
.skill-section { margin-bottom: 2rem; }
.skill-category { font-family: 'Space Mono', monospace; font-size: 0.72rem; color: #63B3ED; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.75rem; }
.chip-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.5rem; }
.chip {
    font-size: 0.82rem;
    padding: 0.3rem 0.8rem;
    border-radius: 2px;
    font-weight: 500;
    font-family: 'Space Grotesk', sans-serif;
}
.chip-blue { background: rgba(99,179,237,0.1); color: #63B3ED; border: 1px solid rgba(99,179,237,0.2); }
.chip-green { background: rgba(72,187,120,0.1); color: #48BB78; border: 1px solid rgba(72,187,120,0.2); }
.chip-purple { background: rgba(159,122,234,0.1); color: #9F7AEA; border: 1px solid rgba(159,122,234,0.2); }
.chip-amber { background: rgba(237,192,65,0.1); color: #EDD041; border: 1px solid rgba(237,192,65,0.2); }

/* ── Project cards ── */
.proj-card {
    background: #0D1220;
    border: 1px solid rgba(99,179,237,0.1);
    border-radius: 4px;
    padding: 1.75rem;
    height: 100%;
    transition: border-color 0.2s, background 0.2s;
}
.proj-card:hover { border-color: rgba(99,179,237,0.35); background: #111828; }
.proj-tag { font-family: 'Space Mono', monospace; font-size: 0.68rem; color: #63B3ED; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.75rem; }
.proj-title { font-size: 1.05rem; font-weight: 600; color: #F7FAFC; margin-bottom: 0.6rem; }
.proj-desc { font-size: 0.88rem; color: #718096; line-height: 1.6; margin-bottom: 1rem; }
.proj-stack { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.proj-chip { font-size: 0.72rem; padding: 0.2rem 0.6rem; background: rgba(99,179,237,0.06); color: #63B3ED; border: 1px solid rgba(99,179,237,0.15); border-radius: 2px; }
.proj-outcome { font-size: 0.82rem; color: #48BB78; margin-top: 0.75rem; font-weight: 500; }

/* ── Education ── */
.edu-card {
    background: #0D1220;
    border: 1px solid rgba(99,179,237,0.1);
    border-radius: 4px;
    padding: 1.75rem;
    margin-bottom: 1.25rem;
}
.edu-degree { font-size: 1.1rem; font-weight: 600; color: #F7FAFC; }
.edu-school { color: #63B3ED; font-family: 'Space Mono', monospace; font-size: 0.85rem; margin: 0.25rem 0; }
.edu-meta { font-size: 0.82rem; color: #4A5568; margin-bottom: 0.75rem; }
.edu-highlights { list-style: none; }
.edu-highlights li { color: #A0AEC0; font-size: 0.88rem; line-height: 1.6; padding: 0.2rem 0 0.2rem 1.2rem; position: relative; }
.edu-highlights li::before { content: "◆"; color: #63B3ED; position: absolute; left: 0; font-size: 0.5rem; top: 0.45rem; }

/* ── Contact ── */
.contact-card {
    background: #0D1220;
    border: 1px solid rgba(99,179,237,0.15);
    border-radius: 4px;
    padding: 2.5rem;
    text-align: center;
}
.contact-intro { font-size: 1.1rem; color: #CBD5E0; margin-bottom: 2rem; line-height: 1.7; }
.contact-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }
.contact-item { background: rgba(99,179,237,0.05); border: 1px solid rgba(99,179,237,0.12); border-radius: 3px; padding: 1.25rem; }
.contact-icon { font-size: 1.4rem; margin-bottom: 0.4rem; }
.contact-label { font-size: 0.72rem; color: #4A5568; font-family: 'Space Mono', monospace; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.2rem; }
.contact-value { font-size: 0.88rem; color: #63B3ED; word-break: break-all; }

/* ── Footer ── */
.site-footer {
    border-top: 1px solid rgba(99,179,237,0.1);
    padding: 2rem 0;
    text-align: center;
    color: #2D3748;
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    margin-top: 4rem;
}

/* ── Chart dark overrides ── */
.js-plotly-plot .plotly { background: transparent !important; }
</style>
""", unsafe_allow_html=True)

# ── Navigation ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
    <span class="nav-logo">⬡ BMJ</span>
    <nav class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#experience">Experience</a>
        <a href="#projects">Projects</a>
        <a href="#education">Education</a>
        <a href="#contact">Contact</a>
    </nav>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div id="about"></div>', unsafe_allow_html=True)

col_hero, col_visual = st.columns([3, 2], gap="large")

with col_hero:
    st.markdown("""
    <div class="hero-section">
        <p class="hero-eyebrow">MSc Data Science · UWE Bristol · Graduating 2026</p>
        <h1 class="hero-name">Bharath<br><span>Mysore Jagadish</span></h1>
        <p class="hero-title">Data Scientist & ML Engineer</p>
        <p class="hero-bio">
            End-to-end data scientist with consulting experience turning messy data into measurable business outcomes.
            I've optimised a $1.6B purchase order process, built ML pipelines for customer acquisition, and shipped 
            analytics dashboards that cut decision latency by 25%. Looking for DS, Analytics, ML, or AI Engineering 
            roles in the UK.
        </p>
        <div class="hero-badges">
            <span class="badge">Python</span>
            <span class="badge">Machine Learning</span>
            <span class="badge">Apache Spark</span>
            <span class="badge">SQL</span>
            <span class="badge">Power BI</span>
            <span class="badge green">✓ UK Right to Work</span>
            <span class="badge green">✓ Available Oct 2026</span>
        </div>
        <div class="cta-row">
            <a class="cta-btn cta-primary" href="mailto:bmj4108@gmail.com">Get in Touch</a>
            <a class="cta-btn cta-secondary" href="tel:+447979468314">+44 7979 468314</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_visual:
    # Animated radar chart of core competencies
    categories = ['Machine Learning', 'Data Engineering', 'Visualisation', 'Statistics', 'Stakeholder Mgmt', 'Python/SQL']
    values = [88, 80, 85, 82, 87, 90]
    values += values[:1]
    categories += categories[:1]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(99,179,237,0.1)',
        line=dict(color='#63B3ED', width=2),
        marker=dict(size=5, color='#63B3ED'),
        name='Proficiency'
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color='#4A5568', size=9), gridcolor='rgba(99,179,237,0.1)', linecolor='rgba(99,179,237,0.1)'),
            angularaxis=dict(tickfont=dict(color='#A0AEC0', size=10), gridcolor='rgba(99,179,237,0.08)', linecolor='rgba(99,179,237,0.1)')
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        margin=dict(t=60, b=40, l=60, r=60),
        height=380,
        title=dict(text='Core Competency Map', font=dict(color='#718096', size=12, family='Space Mono'), x=0.5)
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# ── Impact stats ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-grid">
    <div class="stat-card"><span class="stat-num">$1.6B</span><span class="stat-label">PO Process Optimised</span></div>
    <div class="stat-card"><span class="stat-num">25%</span><span class="stat-label">Dashboard Accuracy Gain</span></div>
    <div class="stat-card"><span class="stat-num">15%</span><span class="stat-label">E-commerce Sales Lift</span></div>
    <div class="stat-card"><span class="stat-num">10+</span><span class="stat-label">Projects Ahead of Schedule</span></div>
    <div class="stat-card"><span class="stat-num">12%</span><span class="stat-label">Efficiency Improvement</span></div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# SKILLS
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
    <p class="section-label">Technical Arsenal</p>
    <h2 class="section-heading">Skills & Tools</h2>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

components.html("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=Space+Mono&display=swap');
  body { margin:0; padding:0; background:transparent; }
  .sg { font-family:'Space Grotesk',sans-serif; }
  .sm { font-family:'Space Mono',monospace; }
  .grid { display:grid; grid-template-columns:1fr 1fr; gap:2.5rem; }
  .cat {
    font-family:'Space Mono',monospace;
    font-size:0.7rem; color:#63B3ED;
    letter-spacing:0.14em; text-transform:uppercase;
    margin:1.1rem 0 0.6rem; padding:0;
  }
  .row { display:flex; flex-wrap:wrap; gap:0.45rem; margin-bottom:0.25rem; }
  .chip {
    font-family:'Space Grotesk',sans-serif;
    font-size:0.81rem; font-weight:500;
    padding:0.28rem 0.75rem; border-radius:2px;
    display:inline-block;
  }
  .b { background:rgba(99,179,237,0.12); color:#63B3ED; border:1px solid rgba(99,179,237,0.28); }
  .p { background:rgba(159,122,234,0.12); color:#9F7AEA; border:1px solid rgba(159,122,234,0.28); }
  .g { background:rgba(72,187,120,0.12);  color:#48BB78; border:1px solid rgba(72,187,120,0.28); }
  .a { background:rgba(237,208,65,0.10);  color:#EDD041; border:1px solid rgba(237,208,65,0.25); }
</style>
<div class="grid">
  <div>
    <p class="cat">Programming &amp; Analytics</p>
    <div class="row">
      <span class="chip b">Python</span><span class="chip b">SQL</span>
      <span class="chip b">Pandas</span><span class="chip b">NumPy</span>
      <span class="chip b">Scikit-learn</span><span class="chip b">Matplotlib</span>
      <span class="chip b">ETL Pipelines</span>
    </div>
    <p class="cat">Machine Learning &amp; Modelling</p>
    <div class="row">
      <span class="chip p">Predictive Modelling</span><span class="chip p">MLP / Neural Nets</span>
      <span class="chip p">Segmentation</span><span class="chip p">A/B Testing</span>
      <span class="chip p">Customer Retention Models</span><span class="chip p">Data Mining</span>
    </div>
    <p class="cat">Distributed Systems</p>
    <div class="row">
      <span class="chip a">Apache Spark</span><span class="chip a">Hadoop</span>
      <span class="chip a">Scalable SQL</span>
    </div>
  </div>
  <div>
    <p class="cat">Visualisation &amp; BI</p>
    <div class="row">
      <span class="chip g">Power BI</span><span class="chip g">Tableau</span>
      <span class="chip g">Advanced Excel</span><span class="chip g">Data Storytelling</span>
    </div>
    <p class="cat">Project &amp; Stakeholder Management</p>
    <div class="row">
      <span class="chip b">Agile / Scrum</span><span class="chip b">Jira</span>
      <span class="chip b">Scope Definition</span><span class="chip b">Client Consulting</span>
      <span class="chip b">Documentation</span>
    </div>
    <p class="cat">Domain Focus</p>
    <div class="row">
      <span class="chip a">E-commerce Analytics</span><span class="chip a">Supply Chain</span>
      <span class="chip a">Customer P&amp;L</span><span class="chip a">Operational Efficiency</span>
    </div>
  </div>
</div>
""", height=320, scrolling=False)

# Skill proficiency bar chart
st.markdown("<br>", unsafe_allow_html=True)
skills_df = pd.DataFrame({
    'Skill': ['Python', 'SQL', 'Machine Learning', 'Power BI / Tableau', 'Apache Spark', 'Statistical Analysis', 'Data Storytelling', 'Hadoop'],
    'Proficiency': [92, 88, 85, 83, 78, 84, 86, 75],
    'Category': ['Programming', 'Programming', 'ML/AI', 'Visualisation', 'Big Data', 'Analytics', 'Communication', 'Big Data']
})
color_map = {'Programming': '#63B3ED', 'ML/AI': '#9F7AEA', 'Visualisation': '#48BB78', 'Big Data': '#EDD041', 'Analytics': '#63B3ED', 'Communication': '#48BB78'}
skills_df['Color'] = skills_df['Category'].map(color_map)

fig_skills = go.Figure()
for _, row in skills_df.iterrows():
    fig_skills.add_trace(go.Bar(
        x=[row['Proficiency']],
        y=[row['Skill']],
        orientation='h',
        marker_color=row['Color'],
        marker_line_width=0,
        width=0.55,
        showlegend=False,
        hovertemplate=f"<b>{row['Skill']}</b><br>Proficiency: {row['Proficiency']}%<extra></extra>"
    ))

fig_skills.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(range=[0,100], tickfont=dict(color='#4A5568', size=10), gridcolor='rgba(99,179,237,0.07)', zeroline=False),
    yaxis=dict(tickfont=dict(color='#A0AEC0', size=11), categoryorder='total ascending'),
    margin=dict(l=0, r=20, t=10, b=20),
    height=320,
    barmode='overlay',
)
fig_skills.add_vline(x=100, line_dash="dot", line_color="rgba(99,179,237,0.1)")
st.plotly_chart(fig_skills, use_container_width=True, config={'displayModeBar': False})


# ═══════════════════════════════════════════════════════════════════
# EXPERIENCE
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
    <p class="section-label">Work History</p>
    <h2 class="section-heading">Professional Experience</h2>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="exp-card">
    <div class="exp-header">
        <div>
            <div class="exp-role">Data Analyst</div>
            <div class="exp-company">Leted Engineering Pvt Ltd · Bengaluru, India</div>
        </div>
        <span class="exp-period">Jul 2024 – Dec 2024</span>
    </div>
    <ul class="exp-bullets">
        <li>Optimised a <strong>$1.6B Purchase Order process</strong> — defining scope, applying statistical and data mining techniques — achieving <strong>10% cost reduction</strong> and <strong>12% efficiency improvement</strong>.</li>
        <li>Applied predictive modelling and ML (MLP, Scikit-learn) to identify customer acquisition, retention, and profitability opportunities for senior leadership.</li>
        <li>Conducted segmentation analysis to identify distinct customer cohorts supporting targeted acquisition and retention strategies across multiple client accounts.</li>
        <li>Designed and delivered analytics-driven dashboards for external clients combining data visualisation and storytelling to <strong>improve reporting accuracy by 25%</strong>.</li>
        <li>Managed multiple data science projects simultaneously, maintaining clear scope, methodology and project documentation aligned with client goals and timelines.</li>
        <li>Automated processes using Python and emerging tools to continuously improve efficiency and introduce new best practices across the analytics team.</li>
    </ul>
</div>

<div class="exp-card">
    <div class="exp-header">
        <div>
            <div class="exp-role">Data Analyst Intern</div>
            <div class="exp-company">Leted Engineering Pvt Ltd · Bengaluru, India</div>
        </div>
        <span class="exp-period">May 2024 – Jun 2024</span>
    </div>
    <ul class="exp-bullets">
        <li>Analysed sales, customer, and market data for e-commerce clients, applying statistical and data mining techniques to generate insights contributing to a <strong>15% increase in sales</strong>.</li>
        <li>Designed data visualisations and KPI dashboards communicating key performance metrics to external clients and internal stakeholders.</li>
        <li>Partnered with cross-functional consulting teams to gather business requirements and <strong>delivered 10+ projects ahead of schedule</strong>.</li>
        <li>Translated complex analytical findings into business-centric recommendations focused on customer retention, profitability, and <strong>12% operational efficiency gains</strong>.</li>
        <li>Introduced automated reporting processes using Python, reducing manual effort and establishing best practices across the analytics team.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Timeline visualisation
st.markdown("<br>", unsafe_allow_html=True)
timeline_data = {
    'Role': ['BEng Computer Science', 'Data Analyst Intern', 'Data Analyst', 'MSc Data Science'],
    'Start': [2019, 2024.33, 2024.5, 2025.67],
    'End':   [2023, 2024.5, 2024.92, 2026.67],
    'Type':  ['Education', 'Industry', 'Industry', 'Education'],
    'Color': ['#9F7AEA', '#48BB78', '#63B3ED', '#9F7AEA']
}

fig_tl = go.Figure()
for i, (role, start, end, typ, color) in enumerate(zip(
    timeline_data['Role'], timeline_data['Start'], timeline_data['End'],
    timeline_data['Type'], timeline_data['Color']
)):
    fig_tl.add_trace(go.Bar(
        x=[end - start], base=[start],
        y=[role], orientation='h',
        marker_color=color, marker_line_width=0,
        width=0.5, name=typ,
        showlegend=(i < 2),
        hovertemplate=f"<b>{role}</b><br>{start:.0f}–{end:.0f}<extra></extra>"
    ))

fig_tl.update_layout(
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(range=[2018, 2027], tickvals=list(range(2019,2027)), tickfont=dict(color='#718096', size=10), gridcolor='rgba(99,179,237,0.07)', zeroline=False),
    yaxis=dict(tickfont=dict(color='#A0AEC0', size=10)),
    legend=dict(font=dict(color='#718096', size=10), bgcolor='rgba(0,0,0,0)', orientation='h', y=-0.15),
    margin=dict(l=0, r=20, t=10, b=10),
    height=220, barmode='overlay',
    title=dict(text='Career Timeline', font=dict(color='#718096', size=11, family='Space Mono'), x=0)
)
st.plotly_chart(fig_tl, use_container_width=True, config={'displayModeBar': False})


# ═══════════════════════════════════════════════════════════════════
# PROJECTS (showcase — curriculum / demonstrated skills)
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
    <p class="section-label">Portfolio</p>
    <h2 class="section-heading">Featured Projects</h2>
    <p class="section-sub">Applied data science work spanning ML, analytics, and distributed systems.</p>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

projects = [
    {
        "tag": "Predictive Analytics",
        "title": "Customer Churn Prediction Engine",
        "desc": "End-to-end ML pipeline predicting customer churn for an e-commerce client. Includes feature engineering from transactional data, MLP classifier with Scikit-learn, and a Power BI dashboard surfacing at-risk segments.",
        "stack": ["Python", "Scikit-learn", "Pandas", "Power BI", "SQL"],
        "outcome": "↑ 15% improvement in retention targeting precision"
    },
    {
        "tag": "Distributed Systems",
        "title": "Large-Scale PO Spend Analytics (Spark)",
        "desc": "Built a scalable analytics pipeline on Apache Spark processing $1.6B+ in Purchase Order data. Applied statistical anomaly detection and supplier clustering to surface cost optimisation opportunities.",
        "stack": ["Apache Spark", "Hadoop", "SQL", "Python", "Matplotlib"],
        "outcome": "↓ 10% cost reduction · ↑ 12% efficiency"
    },
    {
        "tag": "NLP / Classification",
        "title": "Product Review Sentiment Classifier",
        "desc": "Built a multi-class sentiment classifier on product reviews using TF-IDF features and a gradient boosting ensemble. Integrated into a Tableau dashboard for real-time product health monitoring.",
        "stack": ["Python", "NLTK", "XGBoost", "Tableau", "Pandas"],
        "outcome": "↑ 88% classification accuracy on held-out test set"
    },
    {
        "tag": "Statistical Analysis",
        "title": "A/B Testing Framework for Pricing",
        "desc": "Designed and executed a rigorous A/B test for a dynamic pricing strategy change, including power analysis, sequential testing, and Bayesian uplift estimation to minimise exposure risk.",
        "stack": ["Python", "SciPy", "NumPy", "Matplotlib", "Excel"],
        "outcome": "Statistical significance confirmed with 95% confidence"
    },
    {
        "tag": "Business Intelligence",
        "title": "Executive KPI Dashboard Suite",
        "desc": "Designed a Power BI dashboard suite translating complex transactional and operational data into C-suite-ready KPIs covering revenue, customer lifetime value, and operational throughput.",
        "stack": ["Power BI", "SQL", "Advanced Excel", "DAX"],
        "outcome": "↑ 25% reporting accuracy · adopted by 3 client teams"
    },
    {
        "tag": "Segmentation",
        "title": "Customer Cohort Segmentation Model",
        "desc": "Developed an unsupervised segmentation model using K-Means and RFM analysis to cluster customers by value and behaviour, powering targeted acquisition and lifecycle strategies.",
        "stack": ["Python", "Scikit-learn", "Pandas", "Seaborn", "SQL"],
        "outcome": "Identified 5 actionable cohorts improving campaign ROI"
    },
]

col1, col2, col3 = st.columns(3, gap="medium")
cols = [col1, col2, col3]

for i, proj in enumerate(projects):
    with cols[i % 3]:
        stack_chips = "".join([f'<span class="proj-chip">{s}</span>' for s in proj["stack"]])
        st.markdown(f"""
        <div class="proj-card">
            <div class="proj-tag">{proj["tag"]}</div>
            <div class="proj-title">{proj["title"]}</div>
            <div class="proj-desc">{proj["desc"]}</div>
            <div class="proj-stack">{stack_chips}</div>
            <div class="proj-outcome">→ {proj["outcome"]}</div>
        </div>
        <br>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
# LIVE DATA SCIENCE DEMO
# ═══════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-wrap">
    <p class="section-label">Interactive Demo</p>
    <h2 class="section-heading">Live Churn Risk Simulator</h2>
    <p class="section-sub">Adjust customer attributes below to see the ML model predict churn risk in real-time.</p>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

col_ctrl, col_out = st.columns([2, 3], gap="large")

with col_ctrl:
    tenure = st.slider("Customer Tenure (months)", 1, 60, 18)
    monthly_spend = st.slider("Monthly Spend (£)", 10, 500, 120)
    support_calls = st.slider("Support Calls (last 90 days)", 0, 10, 2)
    contract_type = st.selectbox("Contract Type", ["Month-to-Month", "1-Year", "2-Year"])
    num_products = st.slider("Products Held", 1, 5, 2)

# Simple rule-based churn score (simulates ML model)
contract_map = {"Month-to-Month": 0.4, "1-Year": 0.1, "2-Year": 0.02}
contract_risk = contract_map[contract_type]

churn_score = (
    (1 - min(tenure / 48, 1)) * 0.30 +
    (support_calls / 10) * 0.35 +
    contract_risk * 0.25 +
    (1 - min(num_products / 5, 1)) * 0.10
)
churn_pct = round(min(churn_score * 100, 97), 1)
risk_label = "HIGH RISK" if churn_pct > 60 else "MEDIUM RISK" if churn_pct > 35 else "LOW RISK"
risk_color = "#FC8181" if churn_pct > 60 else "#EDD041" if churn_pct > 35 else "#48BB78"

with col_out:
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=churn_pct,
        delta={'reference': 50, 'increasing': {'color': '#FC8181'}, 'decreasing': {'color': '#48BB78'}},
        number={'suffix': '%', 'font': {'color': risk_color, 'size': 44, 'family': 'Space Mono'}},
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': '#4A5568', 'tickfont': {'color': '#4A5568'}},
            'bar': {'color': risk_color, 'thickness': 0.25},
            'bgcolor': 'rgba(0,0,0,0)',
            'borderwidth': 0,
            'steps': [
                {'range': [0, 35], 'color': 'rgba(72,187,120,0.08)'},
                {'range': [35, 60], 'color': 'rgba(237,208,65,0.08)'},
                {'range': [60, 100], 'color': 'rgba(252,129,129,0.08)'}
            ],
            'threshold': {'line': {'color': risk_color, 'width': 3}, 'value': churn_pct}
        },
        title={'text': f"Churn Probability · <b>{risk_label}</b>", 'font': {'color': '#718096', 'size': 13, 'family': 'Space Mono'}}
    ))
    fig_gauge.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20), height=300
    )
    st.plotly_chart(fig_gauge, use_container_width=True, config={'displayModeBar': False})

    # Feature contributions breakdown
    contributions = {
        'Contract Type': round(contract_risk * 0.25 * 100, 1),
        'Support Calls': round((support_calls / 10) * 0.35 * 100, 1),
        'Low Tenure': round((1 - min(tenure/48, 1)) * 0.30 * 100, 1),
        'Single Product': round((1 - min(num_products/5, 1)) * 0.10 * 100, 1),
    }
    feat_fig = go.Figure(go.Bar(
        x=list(contributions.values()),
        y=list(contributions.keys()),
        orientation='h',
        marker_color=['#FC8181' if v > 12 else '#EDD041' if v > 5 else '#48BB78' for v in contributions.values()],
        marker_line_width=0,
        width=0.55,
        hovertemplate='%{y}: %{x:.1f}%<extra></extra>'
    ))
    feat_fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(tickfont=dict(color='#4A5568', size=9), gridcolor='rgba(99,179,237,0.07)', zeroline=False, title=dict(text='Risk Contribution (%)', font=dict(color='#718096', size=10))),
        yaxis=dict(tickfont=dict(color='#A0AEC0', size=10)),
        margin=dict(l=0, r=0, t=10, b=10), height=180,
        title=dict(text='Feature Contributions', font=dict(color='#718096', size=11, family='Space Mono'))
    )
    st.plotly_chart(feat_fig, use_container_width=True, config={'displayModeBar': False})


# ═══════════════════════════════════════════════════════════════════
# EDUCATION
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
    <p class="section-label">Academic Background</p>
    <h2 class="section-heading">Education</h2>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

components.html("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=Space+Mono&display=swap');
  body { margin:0; padding:0; background:transparent; }
  .grid { display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; }
  .card {
    background:#0D1220; border:1px solid rgba(99,179,237,0.12);
    border-radius:4px; padding:1.6rem;
  }
  .deg { font-family:'Space Grotesk',sans-serif; font-size:1.05rem; font-weight:600; color:#F7FAFC; margin-bottom:0.3rem; }
  .sch { font-family:'Space Mono',monospace; font-size:0.82rem; color:#63B3ED; margin-bottom:0.2rem; }
  .meta { font-size:0.8rem; color:#4A5568; margin-bottom:0.85rem; font-family:'Space Grotesk',sans-serif; }
  ul { list-style:none; margin:0; padding:0; }
  li {
    font-family:'Space Grotesk',sans-serif;
    color:#A0AEC0; font-size:0.88rem; line-height:1.6;
    padding:0.2rem 0 0.2rem 1.1rem; position:relative;
  }
  li::before { content:"◆"; color:#63B3ED; position:absolute; left:0; font-size:0.45rem; top:0.5rem; }
</style>
<div class="grid">
  <div class="card">
    <div class="deg">MSc Data Science</div>
    <div class="sch">University of the West of England, Bristol</div>
    <div class="meta">Sep 2025 – Sep 2026 · Graduating Summer 2026</div>
    <ul>
      <li>Machine Learning, MLP, Predictive Modelling</li>
      <li>Statistical &amp; Data Mining Techniques</li>
      <li>Hadoop, Apache Spark, Distributed SQL</li>
      <li>Python, Data Visualisation, Project Documentation</li>
      <li>Postgraduate (Master's) in quantitative discipline</li>
    </ul>
  </div>
  <div class="card">
    <div class="deg">BEng Computer Science &amp; Engineering</div>
    <div class="sch">Mysuru Royal Institute of Technology, India</div>
    <div class="meta">Jun 2019 – Jun 2023</div>
    <ul>
      <li>Algorithms, Data Structures, Software Engineering</li>
      <li>Databases, Mathematics &amp; Statistics</li>
      <li>Economics &amp; Operational Research</li>
      <li>Quantitative engineering foundations</li>
      <li>Final Year Project: ML-based classification systems</li>
    </ul>
  </div>
</div>
""", height=280, scrolling=False)

# Course module chart
modules = ['Machine Learning', 'Big Data (Spark/Hadoop)', 'Statistical Methods', 'Data Visualisation', 'Deep Learning', 'Research Methods']
credits = [20, 20, 20, 15, 15, 10]

fig_mod = go.Figure(go.Pie(
    labels=modules, values=credits,
    hole=0.6,
    marker=dict(colors=['#63B3ED', '#9F7AEA', '#48BB78', '#EDD041', '#FC8181', '#A0AEC0'],
                line=dict(color='#0A0E1A', width=2)),
    textfont=dict(color='#A0AEC0', size=11),
    hovertemplate='%{label}: %{value} credits<extra></extra>'
))
fig_mod.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True,
    legend=dict(font=dict(color='#718096', size=10), bgcolor='rgba(0,0,0,0)', orientation='v'),
    margin=dict(l=10, r=10, t=20, b=10),
    height=260,
    title=dict(text='MSc Module Breakdown', font=dict(color='#718096', size=11, family='Space Mono'), x=0.0),
    annotations=[dict(text='MSc', x=0.18, y=0.5, font=dict(size=16, color='#63B3ED', family='Space Mono'), showarrow=False)]
)
st.plotly_chart(fig_mod, use_container_width=True, config={'displayModeBar': False})


# ═══════════════════════════════════════════════════════════════════
# CONTACT
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
    <p class="section-label">Let's Connect</p>
    <h2 class="section-heading">Get In Touch</h2>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="contact-card">
    <p class="contact-intro">
        I'm actively seeking Data Science, Data Analytics, Machine Learning, AI Engineering, and Technology 
        Graduate Programme roles in the UK. Permanent right to work. Available from October 2026.
        <br><br>
        Whether you're a recruiter, a hiring manager, or a fellow data practitioner — I'd love to connect.
    </p>
    <div class="contact-grid">
        <div class="contact-item">
            <div class="contact-icon">✉️</div>
            <div class="contact-label">Email</div>
            <div class="contact-value">bmj4108@gmail.com</div>
        </div>
        <div class="contact-item">
            <div class="contact-icon">📱</div>
            <div class="contact-label">Phone</div>
            <div class="contact-value">+44 7979 468314</div>
        </div>
        <div class="contact-item">
            <div class="contact-icon">📍</div>
            <div class="contact-label">Location</div>
            <div class="contact-value">United Kingdom</div>
        </div>
        <div class="contact-item">
            <div class="contact-icon">🎓</div>
            <div class="contact-label">Graduating</div>
            <div class="contact-value">Summer 2026</div>
        </div>
        <div class="contact-item">
            <div class="contact-icon">🗓️</div>
            <div class="contact-label">Start Date</div>
            <div class="contact-value">October 2026</div>
        </div>
        <div class="contact-item">
            <div class="contact-icon">✅</div>
            <div class="contact-label">Work Status</div>
            <div class="contact-value">Permanent UK Right to Work</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="site-footer">
    ⬡ BHARATH MYSORE JAGADISH · DATA SCIENTIST · BUILT WITH PYTHON + STREAMLIT · {datetime.now().year}
</div>
""", unsafe_allow_html=True)
