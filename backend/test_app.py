import unittest
import os
import tempfile
from app import app, db, User, ContactMessage, Friendship, ChatMessage
from werkzeug.security import check_password_hash
import json


class GamePlatformTestCase(unittest.TestCase):
    """Unit tesztek a játékplatform backend alkalmazásához"""

    def setUp(self):
        """Teszt környezet beállítása minden teszt előtt"""
        # Temp adatbázis létrehozása
        self.db_fd, self.db_path = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{self.db_path}'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SECRET_KEY'] = 'test_secret_key'
        
        self.app = app
        self.client = app.test_client()
        
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Teszt környezet takarítása minden teszt után"""
        with app.app_context():
            db.session.remove()
            db.drop_all()
        os.close(self.db_fd)
        os.unlink(self.db_path)

    # ========== User Registration Tests ==========
    
    def test_register_success(self):
        """Sikeres regisztráció tesztelése"""
        response = self.client.post('/register', data={
            'username': 'testuser',
            'password': 'testpass123',
            'name': 'Test User',
            'email': 'test@example.com'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.name, 'Test User')
            self.assertEqual(user.email, 'test@example.com')
            self.assertTrue(check_password_hash(user.password, 'testpass123'))

    def test_register_duplicate_username(self):
        """Duplikált felhasználónév tesztelése"""
        with app.app_context():
            user = User(username='existinguser', password='pass', name='Existing', email='existing@example.com')
            db.session.add(user)
            db.session.commit()
        
        response = self.client.post('/register', data={
            'username': 'existinguser',
            'password': 'newpass123',
            'name': 'New User',
            'email': 'new@example.com'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('foglalt'.encode('utf-8'), response.data)

    def test_register_duplicate_email(self):
        """Duplikált email cím tesztelése"""
        with app.app_context():
            user = User(username='user1', password='pass', name='User One', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        response = self.client.post('/register', data={
            'username': 'user2',
            'password': 'pass123',
            'name': 'User Two',
            'email': 'test@example.com'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('haszn'.encode('utf-8'), response.data)

    def test_register_missing_fields(self):
        """Hiányzó mezők tesztelése regisztrációnál"""
        response = self.client.post('/register', data={
            'username': 'testuser',
            'password': 'testpass'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        # A válasz tartalmaznia kell a regisztrációs oldalt és a hibaüzenet egy részét
        self.assertIn('Regisztr'.encode('utf-8'), response.data)
        self.assertIn('telez'.encode('utf-8'), response.data)

    # ========== Login/Logout Tests ==========
    
    def test_login_success(self):
        """Sikeres bejelentkezés tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('testpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testpass'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        
        with self.client.session_transaction() as sess:
            self.assertEqual(sess.get('username'), 'testuser')

    def test_login_wrong_password(self):
        """Hibás jelszó tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('correctpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'wrongpass'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hibás'.encode('utf-8'), response.data)

    def test_login_nonexistent_user(self):
        """Nem létező felhasználó tesztelése"""
        response = self.client.post('/login', data={
            'username': 'nonexistent',
            'password': 'testpass'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hibás'.encode('utf-8'), response.data)

    def test_logout(self):
        """Kijelentkezés tesztelése"""
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.get('/logout', follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        
        with self.client.session_transaction() as sess:
            self.assertIsNone(sess.get('username'))

    # ========== Route Access Tests ==========
    
    def test_home_page(self):
        """Főoldal elérhetőségének tesztelése"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_search_functionality(self):
        """Keresés funkció tesztelése"""
        response = self.client.get('/search?q=shadow')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Shadow'.encode('utf-8'), response.data)

    def test_game_detail_existing(self):
        """Létező játék részleteinek tesztelése"""
        response = self.client.get('/game/shadow-strike')
        self.assertEqual(response.status_code, 200)

    def test_game_detail_nonexistent(self):
        """Nem létező játék tesztelése"""
        response = self.client.get('/game/nonexistent-game')
        self.assertEqual(response.status_code, 404)

    def test_category_pages(self):
        """Kategória oldalak elérhetőségének tesztelése"""
        categories = ['/akcio', '/logikai', '/verseny', '/sport', '/retro']
        for category in categories:
            response = self.client.get(category)
            self.assertEqual(response.status_code, 200)

    def test_beallitasok_requires_login(self):
        """Beállítások oldal bejelentkezést igényel"""
        response = self.client.get('/beallitasok', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Redirect-el a login oldalra
        self.assertIn('Bejelentkez'.encode('utf-8'), response.data)

    def test_beallitasok_logged_in(self):
        """Beállítások oldal bejelentkezve"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('testpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.get('/beallitasok')
        self.assertEqual(response.status_code, 200)

    # ========== Contact Message Tests ==========
    
    def test_contact_form_submission(self):
        """Kapcsolati űrlap küldésének tesztelése"""
        response = self.client.post('/kapcsolat', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        
        with app.app_context():
            message = ContactMessage.query.filter_by(email='john@example.com').first()
            self.assertIsNotNone(message)
            self.assertEqual(message.name, 'John Doe')
            self.assertEqual(message.subject, 'Test Subject')
            self.assertEqual(message.status, 'new')

    def test_contact_form_logged_in_user(self):
        """Bejelentkezett felhasználó kapcsolati üzenetének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('testpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/kapcsolat', data={
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        
        with app.app_context():
            message = ContactMessage.query.first()
            self.assertIsNotNone(message)
            self.assertIsNotNone(message.user_id)

    # ========== Admin Tests ==========
    
    def test_admin_messages_unauthorized(self):
        """Admin oldal jogosulatlan hozzáférés tesztelése"""
        response = self.client.get('/admin/messages', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Redirect-el a főoldalra
        self.assertIn('Online'.encode('utf-8'), response.data)

    def test_admin_messages_non_admin_user(self):
        """Admin oldal normál felhasználóval"""
        with self.client.session_transaction() as sess:
            sess['username'] = 'normaluser'
        
        response = self.client.get('/admin/messages', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Redirect-el a főoldalra
        self.assertIn('Online'.encode('utf-8'), response.data)

    def test_admin_messages_authorized(self):
        """Admin oldal jogosult hozzáférés tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            admin = User(username='admin', password=generate_password_hash('adminpass'), 
                        name='Admin User', email='admin@example.com')
            db.session.add(admin)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'admin'
        
        response = self.client.get('/admin/messages')
        self.assertEqual(response.status_code, 200)

    def test_mark_message_read(self):
        """Üzenet olvasottnak jelölése tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            admin = User(username='admin', password=generate_password_hash('adminpass'), 
                        name='Admin User', email='admin@example.com')
            db.session.add(admin)
            db.session.commit()
            
            message = ContactMessage(name='Test', email='test@example.com', 
                                    subject='Test', message='Test message')
            db.session.add(message)
            db.session.commit()
            message_id = message.id
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'admin'
        
        response = self.client.post(f'/admin/messages/{message_id}/mark-read')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        with app.app_context():
            message = ContactMessage.query.get(message_id)
            self.assertEqual(message.status, 'read')

    def test_delete_message(self):
        """Üzenet törlésének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            admin = User(username='admin', password=generate_password_hash('adminpass'), 
                        name='Admin User', email='admin@example.com')
            db.session.add(admin)
            db.session.commit()
            
            message = ContactMessage(name='Test', email='test@example.com', 
                                    subject='Test', message='Test message')
            db.session.add(message)
            db.session.commit()
            message_id = message.id
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'admin'
        
        response = self.client.post(f'/admin/messages/{message_id}/delete')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        with app.app_context():
            message = ContactMessage.query.get(message_id)
            self.assertIsNone(message)

    # ========== User Settings Tests ==========
    
    def test_update_email(self):
        """Email cím frissítésének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('testpass'), 
                       name='Test User', email='old@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/update-email', data={
            'email': 'new@example.com'
        })
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertEqual(user.email, 'new@example.com')

    def test_update_email_duplicate(self):
        """Duplikált email cím frissítésének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user1 = User(username='user1', password=generate_password_hash('pass'), 
                        name='User One', email='user1@example.com')
            user2 = User(username='user2', password=generate_password_hash('pass'), 
                        name='User Two', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.post('/update-email', data={
            'email': 'user2@example.com'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_update_name(self):
        """Név frissítésének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('testpass'), 
                       name='Old Name', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/update-name', data={
            'name': 'New Name'
        })
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertEqual(user.name, 'New Name')

    def test_change_password_success(self):
        """Sikeres jelszó változtatás tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('oldpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/change-password', data={
            'current_password': 'oldpass',
            'new_password': 'newpass123',
            'confirm_password': 'newpass123'
        })
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertTrue(check_password_hash(user.password, 'newpass123'))

    def test_change_password_wrong_current(self):
        """Hibás jelenlegi jelszóval való változtatás tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('correctpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/change-password', data={
            'current_password': 'wrongpass',
            'new_password': 'newpass123',
            'confirm_password': 'newpass123'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_change_password_mismatch(self):
        """Nem egyező új jelszavak tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('oldpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/change-password', data={
            'current_password': 'oldpass',
            'new_password': 'newpass123',
            'confirm_password': 'different123'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_change_password_too_short(self):
        """Túl rövid új jelszó tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('oldpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/change-password', data={
            'current_password': 'oldpass',
            'new_password': 'short',
            'confirm_password': 'short'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_update_settings(self):
        """Beállítások frissítésének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('testpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/update-settings', data={
            'theme': 'dark',
            'animations': 'false'
        })
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['theme'], 'dark')
        self.assertFalse(data['animations'])
        
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertEqual(user.theme, 'dark')
            self.assertFalse(user.animations_enabled)

    def test_delete_account(self):
        """Fiók törlésének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('testpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/delete-account', data={
            'password': 'testpass',
            'confirmation': 'TÖRLÉS'
        })
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNone(user)

    def test_delete_account_wrong_password(self):
        """Fiók törlése hibás jelszóval"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='testuser', password=generate_password_hash('correctpass'), 
                       name='Test User', email='test@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'testuser'
        
        response = self.client.post('/delete-account', data={
            'password': 'wrongpass',
            'confirmation': 'TÖRLÉS'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    # ========== Friendship Tests ==========
    
    def test_add_friend_success(self):
        """Sikeres barát hozzáadás tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user1 = User(username='user1', password=generate_password_hash('pass'), 
                        name='User One', email='user1@example.com')
            user2 = User(username='user2', password=generate_password_hash('pass'), 
                        name='User Two', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.post('/api/add-friend', data={
            'email': 'user2@example.com'
        })
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        with app.app_context():
            friendships = Friendship.query.all()
            self.assertEqual(len(friendships), 2)  # Kétirányú barátság

    def test_add_friend_nonexistent(self):
        """Nem létező felhasználó hozzáadása barátnak"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='user1', password=generate_password_hash('pass'), 
                       name='User One', email='user1@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.post('/api/add-friend', data={
            'email': 'nonexistent@example.com'
        })
        
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_add_friend_self(self):
        """Saját magunk hozzáadása barátnak"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user = User(username='user1', password=generate_password_hash('pass'), 
                       name='User One', email='user1@example.com')
            db.session.add(user)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.post('/api/add-friend', data={
            'email': 'user1@example.com'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_add_friend_duplicate(self):
        """Már létező barát újra hozzáadása"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user1 = User(username='user1', password=generate_password_hash('pass'), 
                        name='User One', email='user1@example.com')
            user2 = User(username='user2', password=generate_password_hash('pass'), 
                        name='User Two', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            
            friendship = Friendship(user_id=user1.id, friend_id=user2.id)
            db.session.add(friendship)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.post('/api/add-friend', data={
            'email': 'user2@example.com'
        })
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_get_friends(self):
        """Barátlista lekérésének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user1 = User(username='user1', password=generate_password_hash('pass'), 
                        name='User One', email='user1@example.com')
            user2 = User(username='user2', password=generate_password_hash('pass'), 
                        name='User Two', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            
            friendship = Friendship(user_id=user1.id, friend_id=user2.id)
            db.session.add(friendship)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.get('/api/friends')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['friends']), 1)
        self.assertEqual(data['friends'][0]['name'], 'User Two')

    # ========== Chat Tests ==========
    
    def test_send_message_success(self):
        """Sikeres üzenetküldés tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user1 = User(username='user1', password=generate_password_hash('pass'), 
                        name='User One', email='user1@example.com')
            user2 = User(username='user2', password=generate_password_hash('pass'), 
                        name='User Two', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            
            friendship = Friendship(user_id=user1.id, friend_id=user2.id)
            db.session.add(friendship)
            db.session.commit()
            receiver_id = user2.id
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.post('/api/chat/send', data={
            'receiver_id': receiver_id,
            'message': 'Hello friend!'
        })
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        
        with app.app_context():
            messages = ChatMessage.query.all()
            self.assertEqual(len(messages), 1)
            self.assertEqual(messages[0].message, 'Hello friend!')

    def test_send_message_not_friends(self):
        """Üzenetküldés nem barátnak"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user1 = User(username='user1', password=generate_password_hash('pass'), 
                        name='User One', email='user1@example.com')
            user2 = User(username='user2', password=generate_password_hash('pass'), 
                        name='User Two', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            receiver_id = user2.id
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.post('/api/chat/send', data={
            'receiver_id': receiver_id,
            'message': 'Hello stranger!'
        })
        
        self.assertEqual(response.status_code, 403)
        data = json.loads(response.data)
        self.assertFalse(data['success'])

    def test_get_chat_messages(self):
        """Chat üzenetek lekérésének tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user1 = User(username='user1', password=generate_password_hash('pass'), 
                        name='User One', email='user1@example.com')
            user2 = User(username='user2', password=generate_password_hash('pass'), 
                        name='User Two', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            
            friendship = Friendship(user_id=user1.id, friend_id=user2.id)
            db.session.add(friendship)
            db.session.commit()
            
            msg1 = ChatMessage(sender_id=user1.id, receiver_id=user2.id, message='Hi!')
            msg2 = ChatMessage(sender_id=user2.id, receiver_id=user1.id, message='Hello!')
            db.session.add(msg1)
            db.session.add(msg2)
            db.session.commit()
            friend_id = user2.id
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.get(f'/api/chat/{friend_id}')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['messages']), 2)

    def test_unread_messages_count(self):
        """Olvasatlan üzenetek számának tesztelése"""
        with app.app_context():
            from werkzeug.security import generate_password_hash
            user1 = User(username='user1', password=generate_password_hash('pass'), 
                        name='User One', email='user1@example.com')
            user2 = User(username='user2', password=generate_password_hash('pass'), 
                        name='User Two', email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            
            msg1 = ChatMessage(sender_id=user2.id, receiver_id=user1.id, message='Hi!', read=False)
            msg2 = ChatMessage(sender_id=user2.id, receiver_id=user1.id, message='Hello!', read=False)
            db.session.add(msg1)
            db.session.add(msg2)
            db.session.commit()
        
        with self.client.session_transaction() as sess:
            sess['username'] = 'user1'
        
        response = self.client.get('/api/unread-messages')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['unread_count'], 2)

    # ========== Authorization Tests ==========
    
    def test_unauthorized_api_access(self):
        """API végpontok jogosulatlan hozzáférésének tesztelése"""
        endpoints = [
            '/update-email',
            '/update-name',
            '/change-password',
            '/update-settings',
            '/delete-account',
            '/api/add-friend',
            '/api/friends',
            '/api/unread-messages'
        ]
        
        for endpoint in endpoints:
            response = self.client.post(endpoint) if endpoint.startswith(('/update', '/change', '/delete', '/api/add')) else self.client.get(endpoint)
            self.assertEqual(response.status_code, 401)
            data = json.loads(response.data)
            self.assertFalse(data['success'])


if __name__ == '__main__':
    unittest.main()
