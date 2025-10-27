# 🎮 Játékos Projekt - Online Játék Platform

Modern, játékos témájú webalkalmazás Flask backend-el és interaktív frontend-el.

## 📁 Projekt Struktúra

```
jatekos_projekt/
├── .gitignore                 # Git figyelmen kívül hagyandó fájlok
├── .venv/                     # Python virtual environment (NE commitold!)
├── instance/                  # Adatbázis mappa (NE commitold!)
│   └── users.db              # SQLite adatbázis
├── Meeting.md                 # Projekt meeting jegyzetek
├── README.md                  # Projekt főoldal dokumentáció
├── User_Storyk.md            # User story-k
└── web-login-app/            # Fő alkalmazás mappa
    ├── README.md             # Alkalmazás dokumentáció
    └── backend/              # Flask backend alkalmazás
        ├── app.py            # Fő Flask alkalmazás
        ├── requirements.txt  # Python függőségek
        ├── README.md         # Backend dokumentáció
        ├── instance/         # Backend adatbázis (auto-generált)
        │   └── users.db     # SQLite adatbázis
        ├── static/          # Statikus fájlok (CSS, JS, képek)
        │   ├── css/
        │   │   └── style.css        # Fő stíluslap
        │   └── js/
        │       └── game-cards.js    # Játék kártya interakciók
        └── templates/       # Jinja2 HTML template-ek
            ├── home.html            # Főoldal
            ├── login.html           # Bejelentkezés
            ├── register.html        # Regisztráció
            ├── akcio.html           # Akció játékok kategória
            ├── logikai.html         # Logikai játékok kategória
            ├── verseny.html         # Verseny játékok kategória
            ├── sport.html           # Sport játékok kategória
            └── retro.html           # Retro játékok kategória
```

## 🚀 Gyors Kezdés

### 1. Virtual Environment létrehozása és aktiválása

```powershell
# Virtual environment létrehozása
python -m venv .venv

# Aktiválás (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Vagy (Windows CMD)
.venv\Scripts\activate.bat
```

### 2. Függőségek telepítése

```powershell
cd web-login-app\backend
pip install -r requirements.txt
```

### 3. Alkalmazás indítása

```powershell
# Még mindig a backend mappában
python app.py
```

### 4. Böngészőben megnyitás

Nyisd meg: `http://127.0.0.1:5000/`

## ✨ Funkciók

### 🔐 Felhasználói Rendszer

- **Regisztráció**: Új felhasználó létrehozása hash-elt jelszóval
- **Bejelentkezés**: Biztonságos authentikáció
- **Kijelentkezés**: Session kezelés
- **Felhasználónév megjelenítés**: Személyre szabott üdvözlés

### 🎮 Játék Kategóriák (5 db, egyenként 10 játékkal)

1. **🎮 Akció** - Intenzív csaták és izgalmas kalandok
2. **🧩 Logikai** - Gondolkodtató feladványok és agytornák
3. **🏎️ Verseny** - Gyorsasági versenyek és száguldás
4. **⚽ Sport** - Virtuális sportélmények
5. **👾 Retro** - Klasszikus játékok modern köntösben

### 🎨 Modern UI/UX

- **Animált gradient háttér** - Folyamatosan mozgó színek
- **Lebegő formák** - Dinamikus háttér effektek
- **Glassmorphism dizájn** - Üveges, modern felületek
- **Hover animációk** - Interaktív visszajelzések
- **Responsive layout** - Mobil és desktop támogatás

### 🃏 Játék Kártyák

- Színes gradient képek
- Interaktív hover effektek
- Lenyíló leírások
- "PLAY" gomb megjelenés hover-re
- Smooth CSS animációk

## 🛠️ Technológiák

### Backend

- **Flask** - Python web framework
- **Flask-SQLAlchemy** - ORM adatbázis kezelés
- **Werkzeug** - Jelszó hashelés (bcrypt)
- **SQLite** - Adatbázis

### Frontend

- **HTML5** - Szemantikus struktúra
- **CSS3** - Modern animációk és effektek
- **JavaScript (ES6+)** - Interaktivitás
- **Jinja2** - Template engine

## 📝 Adatbázis Séma

### User Model

```python
id: Integer (Primary Key)
username: String(150) (Unique, Not Null)
password: String(255) (Hash, Not Null)
```

## 🔒 Biztonság

- ✅ Jelszavak **bcrypt** hash-eléssel tárolva
- ✅ Session-alapú authentikáció
- ✅ Flask secret key használata
- ✅ SQL injection védelem (SQLAlchemy ORM)
- ✅ XSS védelem (Jinja2 auto-escape)

## 🎯 Következő Lépések

- [ ] Valódi játékok implementálása
- [ ] Felhasználói profil oldal
- [ ] Kedvenc játékok funkció
- [ ] Játék értékelések és kommentek
- [ ] Leaderboard (ranglisták)
- [ ] Többjátékos mód
- [ ] Achievement rendszer

## 👨‍💻 Fejlesztés

### Új kategória hozzáadása

1. Adj hozzá egy route-ot `app.py`-ban
2. Hozz létre egy template-et `templates/` mappában
3. Adj hozzá linket a `home.html`-ben
4. Használd a meglévő CSS osztályokat

### Új játék hozzáadása kategóriához

Másold be ezt a struktúrát a kategória template-be:

```html
<div class="game-card">
  <div
    class="game-image"
    style="background: linear-gradient(135deg, #color1, #color2);"
  ></div>
  <div class="game-info">
    <h3 class="game-title">Játék Név</h3>
    <button class="game-description-toggle">Részletek ▼</button>
    <p class="game-description">Játék leírása...</p>
  </div>
</div>
```

## 📄 Licenc

Ez egy oktatási projekt.

## 🤝 Közreműködés

Patrik - Fejlesztő
Erik - Fejlesztő
László - Fejlesztő

---

**Verzió:** 1.0.0  
**Utolsó frissítés:** 2025. október 8.
