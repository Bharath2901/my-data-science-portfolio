# Bharath MJ — Data Science Portfolio

A production-ready Streamlit portfolio website for a Data Science graduate.

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Sections

| Section | What's inside |
|---------|---------------|
| **Hero** | Name, title, bio, key badges, radar chart |
| **Impact Stats** | 5 quantified achievements from your CV |
| **Skills** | Chip grid + horizontal proficiency bar chart |
| **Experience** | Two exp cards with bullet points + career timeline |
| **Projects** | 6 project cards (ML, Spark, NLP, A/B, BI, Segmentation) |
| **Live Demo** | Interactive churn risk simulator with gauge + feature chart |
| **Education** | Two edu cards + MSc module pie chart |
| **Contact** | Full contact grid with availability details |

## Customisation Tips

- **Swap the demo**: Replace the rule-based `churn_score` logic in the "Live Demo" section with a real trained model (`joblib.load('model.pkl')`).
- **Add GitHub links**: Add `<a href="...">` tags inside `.proj-card` divs.
- **Update projects**: Edit the `projects` list dict in the Portfolio section.
- **Deploy free**: Push to GitHub → connect to [Streamlit Community Cloud](https://streamlit.io/cloud).

## Deploy to Streamlit Cloud (Free)

1. Push this folder to a GitHub repo
2. Go to share.streamlit.io → New app → select your repo
3. Set `app.py` as the main file
4. Click Deploy — your portfolio will be live at `yourname.streamlit.app`

## Tech Stack

- **Python 3.12+**
- **Streamlit** — app framework
- **Plotly** — all charts (radar, bar, gauge, pie, Gantt)
- **Pandas / NumPy** — data manipulation
