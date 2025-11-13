from flask import abort
from dotenv import load_dotenv

# .env fájl betöltése
load_dotenv()

games_data = [
    {
        'category': 'Akció',
        'icon': '🎮',
        'name': 'Shadow Strike',
        'desc': 'Légy a végső harcos ebben az intenzív akció játékban.',
    },
    {
        'category': 'Akció',
        'icon': '🎮',
        'name': 'Cyber Warriors',
        'desc': 'Futurisztikus harcok a kibertérben.',
    },
    {
        'category': 'Akció',
        'icon': '🎮',
        'name': 'Dragon Assault',
        'desc': 'Repülj sárkányokon és hódítsd meg az égboltot!',
    },
    {
        'category': 'Logikai',
        'icon': '🧩',
        'name': 'Puzzle Master',
        'desc': 'Teszteld a logikádat ezzel a rejtvényjátékkal.',
    },
    {
        'category': 'Verseny',
        'icon': '🏎️',
        'name': 'Speed Racer',
        'desc': 'Versenyezz a leggyorsabb autókkal!',
    },
    {
        'category': 'Sport',
        'icon': '⚽',
        'name': 'Football Pro',
        'desc': 'Légy a legjobb futballista!',
    },
    {
        'category': 'Retro',
        'icon': '👾',
        'name': 'Pac-Man Reborn',
        'desc': 'A klasszikus Pac-Man újragondolva!',
    }
]
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# A frontend és backend külön mappákban van
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), 'frontend')

# Frontend URL environment változóból
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:5000')

app = Flask(__name__, 
            template_folder=os.path.join(FRONTEND_DIR, 'templates'),
            static_folder=os.path.join(FRONTEND_DIR, 'static'))
app.secret_key = os.getenv('SECRET_KEY', 'jatekos_projekt_secret_key')

# Az adatbázis útvonal a backend/instance mappában van
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
os.makedirs(INSTANCE_DIR, exist_ok=True)  # Instance mappa létrehozása, ha nem létezik
DB_PATH = os.path.join(INSTANCE_DIR, 'users.db')

# DATABASE_URL csak akkor használjuk, ha nem üres
db_url = os.getenv('DATABASE_URL')
if db_url and db_url.strip():
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Relationships
    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('friendships', lazy=True))
    friend = db.relationship('User', foreign_keys=[friend_id])

class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    read = db.Column(db.Boolean, default=False)
    
    # Relationships
    sender = db.relationship('User', foreign_keys=[sender_id], backref=db.backref('sent_messages', lazy=True))
    receiver = db.relationship('User', foreign_keys=[receiver_id], backref=db.backref('received_messages', lazy=True))

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
    # Kategóriák adatai
    categories = [
        {
            'name': 'Akció',
            'icon': '🎮',
            'desc': 'Gyors reflexek és izgalmas kalandok',
            'url': url_for('akcio')
        },
        {
            'name': 'Logikai',
            'icon': '🧩',
            'desc': 'Gondolkodtató feladványok',
            'url': url_for('logikai')
        },
        {
            'name': 'Verseny',
            'icon': '🏎️',
            'desc': 'Gyorsaság és adrenalin',
            'url': url_for('verseny')
        },
        {
            'name': 'Sport',
            'icon': '⚽',
            'desc': 'Virtuális sportélmények',
            'url': url_for('sport')
        },
        {
            'name': 'Retro',
            'icon': '👾',
            'desc': 'Klasszikus játékok',
            'url': url_for('retro')
        }
    ]
    return render_template('home.html', username=username, user=user, categories=categories, search_mode=False)
@app.route('/search')
def search():
    username = session.get('username')
    user = get_user_settings()
    query = request.args.get('q', '').strip().lower()
    # Szűrés játék névre
    filtered = [game for game in games_data if query in game['name'].lower()]
    # Minden játékhoz egyedi url
    for game in filtered:
        game['url'] = url_for('game_detail', name=game['name'].replace(' ', '-').lower())
    return render_template('home.html', username=username, user=user, games=filtered, search_mode=True, search_query=query)
@app.route('/game/<name>')
def game_detail(name):
    username = session.get('username')
    user = get_user_settings()
    # Keresés a játékok között
    game = next((g for g in games_data if g['name'].replace(' ', '-').lower() == name), None)
    if not game:
        abort(404)
    return render_template('game_detail.html', username=username, user=user, game=game)

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


@app.route('/play/<game_name>')
def play_game(game_name):
    """Render an embedded page that loads the game's index.html from static/games/<game_name>/index.html"""
    username = session.get('username')
    user = get_user_settings()

    # Validate the game directory exists under static/games
    static_game_path = os.path.join(app.static_folder or 'static', 'games', game_name)
    if not os.path.isdir(static_game_path):
        abort(404)

    iframe_src = url_for('static', filename=f'games/{game_name}/index.html')
    return render_template('game_embed.html', username=username, user=user, game_name=game_name, iframe_src=iframe_src)

# Barátjelölés és chat API endpoint-ok
@app.route('/api/add-friend', methods=['POST'])
def add_friend():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    friend_email = request.form.get('email')
    if not friend_email:
        return jsonify({'success': False, 'message': 'Az email cím kötelező!'}), 400
    
    current_user = User.query.filter_by(username=session['username']).first()
    friend = User.query.filter_by(email=friend_email).first()
    
    if not friend:
        return jsonify({'success': False, 'message': 'Nincs ilyen felhasználó!'}), 404
    
    if friend.id == current_user.id:
        return jsonify({'success': False, 'message': 'Nem adhatod hozzá magad barátnak!'}), 400
    
    # Ellenőrizzük hogy már barátok-e
    existing_friendship = Friendship.query.filter_by(user_id=current_user.id, friend_id=friend.id).first()
    if existing_friendship:
        return jsonify({'success': False, 'message': 'Már barátok vagytok!'}), 400
    
    # Kétirányú barátság létrehozása
    friendship1 = Friendship(user_id=current_user.id, friend_id=friend.id)
    friendship2 = Friendship(user_id=friend.id, friend_id=current_user.id)
    db.session.add(friendship1)
    db.session.add(friendship2)
    db.session.commit()
    
    return jsonify({'success': True, 'message': f'{friend.name} sikeresen hozzáadva a barátaidhoz!', 'friend': {'id': friend.id, 'name': friend.name, 'email': friend.email}})

@app.route('/api/friends')
def get_friends():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    current_user = User.query.filter_by(username=session['username']).first()
    friendships = Friendship.query.filter_by(user_id=current_user.id).all()
    
    friends = []
    for friendship in friendships:
        friend = User.query.get(friendship.friend_id)
        if friend:
            # Ellenőrizzük hogy van-e olvasatlan üzenet ettől a baráttól
            unread_count = ChatMessage.query.filter_by(sender_id=friend.id, receiver_id=current_user.id, read=False).count()
            friends.append({
                'id': friend.id,
                'name': friend.name,
                'email': friend.email,
                'unread_count': unread_count
            })
    
    return jsonify({'success': True, 'friends': friends})

@app.route('/api/chat/send', methods=['POST'])
def send_message():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    receiver_id = request.form.get('receiver_id')
    message_text = request.form.get('message')
    
    if not receiver_id or not message_text:
        return jsonify({'success': False, 'message': 'Minden mező kitöltése kötelező!'}), 400
    
    current_user = User.query.filter_by(username=session['username']).first()
    receiver = User.query.get(receiver_id)
    
    if not receiver:
        return jsonify({'success': False, 'message': 'A címzett nem található!'}), 404
    
    # Ellenőrizzük hogy barátok-e
    friendship = Friendship.query.filter_by(user_id=current_user.id, friend_id=receiver.id).first()
    if not friendship:
        return jsonify({'success': False, 'message': 'Csak barátaidnak küldhetsz üzenetet!'}), 403
    
    new_message = ChatMessage(sender_id=current_user.id, receiver_id=receiver.id, message=message_text)
    db.session.add(new_message)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Üzenet elküldve!', 'chat_message': {
        'id': new_message.id,
        'sender_id': current_user.id,
        'sender_name': current_user.name,
        'message': new_message.message,
        'timestamp': new_message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    }})

@app.route('/api/chat/<int:friend_id>')
def get_chat_messages(friend_id):
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    current_user = User.query.filter_by(username=session['username']).first()
    friend = User.query.get(friend_id)
    
    if not friend:
        return jsonify({'success': False, 'message': 'A barát nem található!'}), 404
    
    # Lekérjük az összes üzenetet a két felhasználó között
    messages = ChatMessage.query.filter(
        ((ChatMessage.sender_id == current_user.id) & (ChatMessage.receiver_id == friend_id)) |
        ((ChatMessage.sender_id == friend_id) & (ChatMessage.receiver_id == current_user.id))
    ).order_by(ChatMessage.timestamp.asc()).all()
    
    # Megjelöljük olvasottnak az összes üzenetet amit a barát küldött
    unread_messages = ChatMessage.query.filter_by(sender_id=friend_id, receiver_id=current_user.id, read=False).all()
    for msg in unread_messages:
        msg.read = True
    db.session.commit()
    
    chat_messages = []
    for msg in messages:
        chat_messages.append({
            'id': msg.id,
            'sender_id': msg.sender_id,
            'sender_name': msg.sender.name,
            'message': msg.message,
            'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'is_mine': msg.sender_id == current_user.id
        })
    
    return jsonify({'success': True, 'messages': chat_messages, 'friend': {'id': friend.id, 'name': friend.name}})

@app.route('/baratok')
def baratok():
    username = session.get('username')
    if not username:
        flash('Kérlek jelentkezz be a barátok eléréséhez!', 'warning')
        return redirect(url_for('login_page'))
    
    user = User.query.filter_by(username=username).first()
    return render_template('baratok.html', username=username, user=user)

@app.route('/api/unread-messages')
def get_unread_messages():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Nem vagy bejelentkezve!'}), 401
    
    current_user = User.query.filter_by(username=session['username']).first()
    
    # Olvasatlan üzenetek száma
    unread_count = ChatMessage.query.filter_by(receiver_id=current_user.id, read=False).count()
    
    # Legutóbbi olvasatlan üzenet
    latest_message = ChatMessage.query.filter_by(receiver_id=current_user.id, read=False).order_by(ChatMessage.timestamp.desc()).first()
    
    latest_msg_data = None
    if latest_message:
        latest_msg_data = {
            'message': latest_message.message,
            'sender_name': latest_message.sender.name,
            'sender_id': latest_message.sender_id,
            'timestamp': latest_message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    return jsonify({
        'success': True,
        'unread_count': unread_count,
        'latest_message': latest_msg_data
    })

if __name__ == '__main__':
    # Ensure the instance directory for the SQLite DB exists so db.create_all() can create the file
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with app.app_context():
        db.create_all()
    app.run(debug=True)