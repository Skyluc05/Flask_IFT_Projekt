
from flask import Flask, render_template, request, redirect, url_for, flash






app = Flask(__name__)
app.secret_key = 'secretkey'  # Wichtig für Flash-Nachrichten und Sessions

USER_CREDENTIALS = {
    'username': 'admin',
    'password': '123'
}


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            return redirect(url_for("homepage"))
        else:
            flash("Ungültige Anmeldedaten. Bitte versuchen Sie es erneut.")

    return render_template("login.html")


@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)
