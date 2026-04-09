from flask import Flask, render_template
import os

app = Flask(__name__)

# ── Remplace cette URL par ton URL Railway après déploiement ──
API_URL = os.environ.get("DDA_API_URL", "https://TON_APP.up.railway.app")

@app.route("/")
def index():
    # On injecte l'URL de l'API dans le HTML au démarrage
    with open(os.path.join(os.path.dirname(__file__), "templates", "index.html"), encoding="utf-8") as f:
        html = f.read().replace("%%API_URL%%", API_URL)
    return html

if __name__ == "__main__":
    app.run(debug=False, port=5091)
