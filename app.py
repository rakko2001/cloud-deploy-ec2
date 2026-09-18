import os
import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "dados_turma.db"

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS mensagens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                sentimento TEXT NOT NULL,
                mensagem TEXT NOT NULL,
                criado_em TEXT NOT NULL
            )
            """
        )
        conn.commit()


@app.route("/", methods=["GET", "POST"])
def index():
    init_db()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()[:80]
        sentimento = request.form.get("sentimento", "").strip()[:40]
        mensagem = request.form.get("mensagem", "").strip()[:280]

        if nome and sentimento and mensagem:
            with get_connection() as conn:
                conn.execute(
                    "INSERT INTO mensagens (nome, sentimento, mensagem, criado_em) VALUES (?, ?, ?, ?)",
                    (nome, sentimento, mensagem, datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
                )
                conn.commit()

        return redirect(url_for("index"))

    with get_connection() as conn:
        mensagens = conn.execute(
            "SELECT nome, sentimento, mensagem, criado_em FROM mensagens ORDER BY id DESC LIMIT 30"
        ).fetchall()

    return render_template("index.html", mensagens=mensagens)


@app.route("/health")
def health():
    return {"status": "ok", "database": str(DB_PATH.name)}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
