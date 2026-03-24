from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import random

app = Flask(__name__)
app.secret_key = "quizsecret"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        con = sqlite3.connect("quiz.db", timeout=10)
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (user, pwd)
        )
        data = cur.fetchone()

        if data:
            session["user_id"] = data[0]
            session["username"] = data[1]
        else:
            cur.execute(
                "INSERT INTO users (username, password) VALUES (?,?)",
                (user, pwd)
            )
            con.commit()
            session["user_id"] = cur.lastrowid
            session["username"] = user

        con.close()
        return redirect("/select_language")

    return render_template("login.html")


@app.route('/select_language', methods=['GET', 'POST'])
def select_language():
    if request.method == 'POST':
        session['language'] = request.form['language']
        return redirect('/quiz')
    return render_template('select_language.html')




@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "user_id" not in session:
        return redirect("/")

    if "language" not in session:
        return redirect("/select_language")

    con = sqlite3.connect("quiz.db")
    cur = con.cursor()

    # ---------- FIRST LOAD ----------
    if request.method == "GET":
        cur.execute(
            "SELECT * FROM questions WHERE language=?",
            (session["language"],)
        )
        questions = cur.fetchall()

        random.shuffle(questions)   # shuffle on every retake

        session["question_ids"] = [q[0] for q in questions]

        con.close()
        return render_template(
            "quiz.html",
            questions=questions,
            username=session["username"]
        )

    # ---------- SUBMIT ----------
    score = 0
    question_ids = session.get("question_ids", [])

    for qid in question_ids:
        cur.execute("SELECT * FROM questions WHERE id=?", (qid,))
        q = cur.fetchone()

        user_answer = request.form.get(str(qid))
        if user_answer == q[6]:   # q[6] = answer
            score += 1

    cur.execute(
        "INSERT INTO results (user_id, score, total) VALUES (?,?,?)",
        (session["user_id"], score, len(question_ids))
    )
    con.commit()
    con.close()

    return render_template(
        "result.html",
        score=score,
        total=len(question_ids),
        username=session["username"]
    )


 # ✅ FIXED NAME

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        con = sqlite3.connect("quiz.db")
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM admin WHERE username=? AND password=?",
            (user, pwd)
        )
        admin = cur.fetchone()
        con.close()

        if admin:
            session["admin"] = user
            return redirect("/admin/dashboard")
        else:
            # Show error message for invalid credentials
            return render_template("admin_login.html", error="Invalid username or password")

    return render_template("admin_login.html")
@app.route("/admin/dashboard")
def admin_dashboard():
    if "admin" not in session:
        return redirect("/admin")

    return render_template("admin_dashboard.html")

@app.route("/admin/add_question", methods=["GET", "POST"])
def add_question():
    if "admin" not in session:
        return redirect("/admin")

    if request.method == "POST":
        question = request.form["question"]
        opt1 = request.form["opt1"]
        opt2 = request.form["opt2"]
        opt3 = request.form["opt3"]
        opt4 = request.form["opt4"]
        answer = request.form["answer"]
        category = request.form["category"]

        con = sqlite3.connect("quiz.db")
        cur = con.cursor()

        cur.execute("""
            INSERT INTO questions
            (question, o1, o2, o3, o4, answer, language)
            VALUES (?,?,?,?,?,?,?)
        """, (question, opt1, opt2, opt3, opt4, answer, category))

        con.commit()
        con.close()

        return redirect("/admin/dashboard")

    return render_template("add_question.html")



@app.route("/admin/results")
def admin_results():
    if "admin" not in session:
        return redirect("/admin")

    con = sqlite3.connect("quiz.db")
    cur = con.cursor()
    cur.execute("""
        SELECT u.username, r.score, r.total
        FROM users u
        JOIN results r ON u.id = r.user_id
    """)
    data = cur.fetchall()
    con.close()

    return render_template("admin_results.html", data=data)

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    return redirect("/admin")



@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

