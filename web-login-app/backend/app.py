from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'jatekos_projekt_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)  # Teljes név
    email = db.Column(db.String(255), nullable=False, unique=True)  # Email kötelező és egyedi
    theme = db.Column(db.String(50), default='colored')  # colored, dark, light
    animations_enabled = db.Column(db.Boolean, default=True)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # NULL ha nem bejelentkezett
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(50), default='new')  # new, read, replied
    
    # Relationship to User
    user = db.relationship('User', backref=db.backref('messages', lazy=True))

def get_user_settings():
    """Helper function to get current user settings"""
    username = session.get('username')
    if username:
        user = User.query.filter_by(username=username).first()
        return user
    return None



@app.route('/')
def home():
    username = session.get('username')
    user = get_user_settings()
    return render_template('home.html', username=username, user=user)

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
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Validáció
        if not name or not email:
            flash('Minden mező kitöltése kötelező!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('A felhasználónév már foglalt!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Ez az email cím már használatban van!', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('Sikeres regisztráció! Most már bejelentkezhetsz.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/akcio')
def akcio():
    username = session.get('username')
    user = get_user_settings()
    return render_template('akcio.html', username=username, user=user)

@app.route('/logikai')
def logikai():
    username = session.get('username')
    user = get_user_settings()
    return render_template('logikai.html', username=username, user=user)

@app.route('/verseny')
def verseny():
    username = session.get('username')
    user = get_user_settings()
    return render_template('verseny.html', username=username, user=user)

@app.route('/sport')
def sport():
    username = session.get('username')
    user = get_user_settings()
    return render_template('sport.html', username=username, user=user)

@app.route('/retro')
def retro():
    username = session.get('username')
    user = get_user_settings()
    return render_template('retro.html', username=username, user=user)

@app.route('/beallitasok')
def beallitasok():
    username = session.get('username')
    if not username:
        flash('Kérlek jelentkezz be a beállítások eléréséhez!', 'warning')
        return redirect(url_for('login_page'))
    
    user = User.query.filter_by(username=username).first()
    return render_template('beallitasok.html', username=username, user=user)

@app.route('/help')
def help_page():
    username = session.get('username')
    user = get_user_settings()
    return render_template('help.html', username=username, user=user)

@app.route('/kapcsolat', methods=['GET', 'POST'])
def kapcsolat():
    username = session.get('username')
    user = get_user_settings()
    if request.method == 'POST':
        # Kapcsolati űrlap feldolgozása
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Üzenet mentése az adatbázisba
        new_message = ContactMessage(
            user_id=user.id if user else None,
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        db.session.add(new_message)
        db.session.commit()
        
        flash('Köszönjük az üzeneted! Hamarosan válaszolunk.', 'success')
        return redirect(url_for('kapcsolat'))
    return render_template('kapcsolat.html', username=username, user=user)

@app.route('/gyik')
def gyik():
    username = session.get('username')
    user = get_user_settings()
    return render_template('gyik.html', username=username, user=user)

@app.route('/admin/messages')
def admin_messages():
    username = session.get('username')
    user = get_user_settings()
    
    # Csak az admin felhasználó férhet hozzá
    if not username or username != 'admin':
        flash('Nincs jogosultságod az oldal megtekintéséhez!', 'danger')
        return redirect(url_for('home'))
    
    # Összes üzenet lekérése időrendben
    messages = ContactMessage.query.order_by(ContactMessage.timestamp.desc()).all()
    
    return render_template('admin_messages.html', username=username, user=user, messages=messages)

@app.route('/admin/messages/<int:message_id>/mark-read', methods=['POST'])
def mark_message_read(message_id):
    username = session.get('username')
    if not username or username != 'admin':
        return jsonify({'success': False, 'message': 'Nincs jogosultságod!'}), 403
    
    message = ContactMessage.query.get_or_404(message_id)
    message.status = 'read'
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Üzenet olvasottnak jelölve!'})

@app.route('/admin/messages/<int:message_id>/mark-replied', methods=['POST'])
def mark_message_replied(message_id):
    username = session.get('username')
    if not username or username != 'admin':
        return jsonify({'success': False, 'message': 'Nincs jogosultságod!'}), 403
    
    message = ContactMessage.query.get_or_404(message_id)
    message.status = 'replied'
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Üzenet megválaszolva jelölve!'})

@app.route('/admin/messages/<int:message_id>/delete', methods=['POST'])
def delete_message(message_id):
    username = session.get('username')
    if not username or username != 'admin':
        return jsonify({'success': False, 'message': 'Nincs jogosultságod!'}), 403
    
    message = ContactMessage.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Üzenet törölve!'})

@app.route('/update-email', methods=['POST'])
def update_email():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    email = request.form.get('email')
    if not email:
        return jsonify({'success': False, 'message': 'Az email cím kötelező!'}), 400
    
    # Ellenőrizzük hogy más felhasználó nem használja-e már ezt az email címet
    existing_user = User.query.filter_by(email=email).first()
    if existing_user and existing_user.username != session['username']:
        return jsonify({'success': False, 'message': 'Ez az email cím már használatban van!'}), 400
    
    user = User.query.filter_by(username=session['username']).first()
    if user:
        user.email = email
        db.session.commit()
        return jsonify({'success': True, 'message': 'Email cím sikeresen mentve!'})
    
    return jsonify({'success': False, 'message': 'Hiba történt!'}), 500

@app.route('/update-name', methods=['POST'])
def update_name():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    name = request.form.get('name')
    if not name:
        return jsonify({'success': False, 'message': 'A név kötelező!'}), 400
    
    user = User.query.filter_by(username=session['username']).first()
    if user:
        user.name = name
        db.session.commit()
        return jsonify({'success': True, 'message': 'Név sikeresen mentve!'})
    
    return jsonify({'success': False, 'message': 'Hiba történt!'}), 500

@app.route('/change-password', methods=['POST'])
def change_password():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    
    if not all([current_password, new_password, confirm_password]):
        return jsonify({'success': False, 'message': 'Minden mező kitöltése kötelező!'}), 400
    
    if len(new_password) < 6:
        return jsonify({'success': False, 'message': 'Az új jelszónak legalább 6 karakter hosszúnak kell lennie!'}), 400
    
    if new_password != confirm_password:
        return jsonify({'success': False, 'message': 'Az új jelszavak nem egyeznek!'}), 400
    
    user = User.query.filter_by(username=session['username']).first()
    if not user or not check_password_hash(user.password, current_password):
        return jsonify({'success': False, 'message': 'A jelenlegi jelszó helytelen!'}), 400
    
    user.password = generate_password_hash(new_password)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Jelszó sikeresen megváltoztatva!'})

@app.route('/update-settings', methods=['POST'])
def update_settings():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    theme = request.form.get('theme')
    animations = request.form.get('animations') == 'true'
    
    user = User.query.filter_by(username=session['username']).first()
    if user:
        if theme:
            user.theme = theme
        user.animations_enabled = animations
        db.session.commit()
        return jsonify({'success': True, 'message': 'Beállítások mentve!', 'theme': user.theme, 'animations': user.animations_enabled})
    
    return jsonify({'success': False, 'message': 'Hiba történt!'}), 500

@app.route('/delete-account', methods=['POST'])
def delete_account():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    password = request.form.get('password')
    confirmation = request.form.get('confirmation')
    
    if confirmation != 'TÖRLÉS':
        return jsonify({'success': False, 'message': 'A megerősítés nem megfelelő!'}), 400
    
    user = User.query.filter_by(username=session['username']).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'success': False, 'message': 'Helytelen jelszó!'}), 400
    
    username = session['username']
    db.session.delete(user)
    db.session.commit()
    session.pop('username', None)
    
    return jsonify({'success': True, 'message': f'{username} fiók sikeresen törölve!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)