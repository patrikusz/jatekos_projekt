from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)



@app.route('/')
def home():
    username = session.get('username')
    return render_template('home.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            flash('Sikeres bejelentkezés!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Hibás felhasználónév vagy jelszó', 'danger')
            return redirect(url_for('login_page'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Sikeres kijelentkezés!', 'success')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('A felhasználónév már foglalt!', 'danger')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Sikeres regisztráció! Most már bejelentkezhetsz.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/akcio')
def akcio():
    username = session.get('username')
    return render_template('akcio.html', username=username)

@app.route('/logikai')
def logikai():
    username = session.get('username')
    return render_template('logikai.html', username=username)

@app.route('/verseny')
def verseny():
    username = session.get('username')
    return render_template('verseny.html', username=username)

@app.route('/sport')
def sport():
    username = session.get('username')
    return render_template('sport.html', username=username)

@app.route('/retro')
def retro():
    username = session.get('username')
    return render_template('retro.html', username=username)

@app.route('/beallitasok', methods=['GET', 'POST'])
def beallitasok():
    username = session.get('username')
    if not username:
        flash('Jelentkezz be a beállítások megtekintéséhez.', 'danger')
        return redirect(url_for('login_page'))
    user = User.query.filter_by(username=username).first()
    if request.method == 'POST':
        current = request.form.get('current_password', '')
        new = request.form.get('new_password', '')
        confirm = request.form.get('confirm_password', '')

        if not user or not check_password_hash(user.password, current):
            flash('A jelenlegi jelszó hibás.', 'danger')
            return redirect(url_for('beallitasok'))
        if new != confirm:
            flash('Az új jelszavak nem egyeznek.', 'danger')
            return redirect(url_for('beallitasok'))
        if len(new) < 6 or not any(c.isupper() for c in new) or not any(c.isdigit() for c in new) or not any(not c.isalnum() for c in new):
            flash('Az új jelszó nem felel meg a követelményeknek.', 'danger')
            return redirect(url_for('beallitasok'))

        user.password = generate_password_hash(new)
        db.session.commit()
        flash('A jelszó sikeresen megváltozott.', 'success')
        return redirect(url_for('beallitasok'))

    return render_template('beallitasok.html', username=username)

@app.route('/help')
def help_page():
    username = session.get('username')
    return render_template('help.html', username=username)

@app.route('/kapcsolat', methods=['GET', 'POST'])
def kapcsolat():
    username = session.get('username')
    if request.method == 'POST':
        # Kapcsolati űrlap feldolgozása
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Itt normál esetben email-t küldenél vagy adatbázisba mentenéd
        flash('Köszönjük az üzeneted! Hamarosan válaszolunk.', 'success')
        return redirect(url_for('kapcsolat'))
    return render_template('kapcsolat.html', username=username)

@app.route('/gyik')
def gyik():
    username = session.get('username')
    return render_template('gyik.html', username=username)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)