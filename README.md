# 🎮 Játékos Projekt - Online Játék Platform

Modern, játékos témájú webalkalmazás Flask backend-del, dinamikus témákkal és teljes körű felhasználói rendszerrel.

## 📁 Projekt Struktúra

```
jatekos_projekt/
├── .gitignore                 # Git figyelmen kívül hagyandó fájlok
├── .venv/                     # Python virtual environment (NE commitold!)
├── kovspec.md                 # Követelmény specifikáció
├── meeting.md                 # Projekt meeting jegyzetek
├── README.md                  # Projekt főoldal dokumentáció
├── user_storyk.md            # User story-k
├── backend/                   # Flask backend alkalmazás
│   ├── app.py                # Fő Flask alkalmazás
│   ├── requirements.txt      # Python függőségek
│   └── instance/             # Adatbázis mappa (NE commitold!)
│       └── users.db          # SQLite adatbázis
├── frontend/                  # Frontend fájlok
│   ├── static/               # Statikus fájlok (CSS, JS, képek)
│   │   ├── css/             # Stíluslapok
│   │   │   └── custom.css   # Egyedi stílusok és témák
│   │   └── games/           # Beágyazott játékok
│   ├── templates/            # Jinja2 HTML template-ek
│   │   ├── partials/        # Újrafelhasználható részek
│   │   │   ├── head.html    # <head> makro
│   │   │   └── navbar.html  # Navbar makró
│   │   ├── home.html        # Főoldal
│   │   ├── login.html       # Bejelentkezés
│   │   ├── register.html    # Regisztráció (név + email)
│   │   ├── beallitasok.html # Felhasználói beállítások
│   │   ├── akcio.html       # Akció játékok kategória
│   │   ├── logikai.html     # Logikai játékok kategória
│   │   ├── verseny.html     # Verseny játékok kategória
│   │   ├── sport.html       # Sport játékok kategória
│   │   ├── retro.html       # Retro játékok kategória
│   │   ├── help.html        # Súgó oldal
│   │   ├── kapcsolat.html   # Kapcsolatfelvétel
│   │   ├── gyik.html        # Gyakori kérdések
│   │   └── admin_messages.html  # Admin üzenetek kezelő
│   └── WebCarGame/           # Unity WebGL build
│       ├── index.html       # Játék betöltő oldal
│       ├── Build/           # Unity build fájlok
│       └── TemplateData/    # Unity template fájlok
└── jatekok/                  # Játékok forráskódja
    └── cargame_unity/        # Unity CarGame projekt
        ├── Assets/          # Unity assets
        ├── Packages/        # Unity packages
        └── ProjectSettings/ # Unity beállítások
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
cd backend
pip install -r requirements.txt
```

### 3. Alkalmazás indítása

```powershell
# A backend mappában
python app.py
```

### 4. Böngészőben megnyitás

Nyisd meg: `http://127.0.0.1:5000/`

## ✨ Funkciók

### 🔐 Felhasználói Rendszer

- **Regisztráció**: Név, email, felhasználónév és jelszó megadása
  - Email egyediség ellenőrzés
  - Jelszó hash-elés (bcrypt)
  - Minden mező kötelező
- **Bejelentkezés**: Biztonságos authentikáció
- **Kijelentkezés**: Session kezelés
- **Beállítások oldal**:
  - Név módosítása
  - Email cím frissítése (egyediség ellenőrzéssel)
  - Jelszó változtatás (jelenlegi jelszó ellenőrzéssel)
  - Téma választás (3 féle)
  - Animációk ki/bekapcsolása
  - Fiók törlése (dupla megerősítéssel)

### 🎨 Téma Rendszer

**3 különböző téma:**

1. **Színes (Colored)** - Animált színes gradiens háttér (alapértelmezett)
2. **Sötét (Dark)** - Professzionális sötét téma
3. **Világos (Light)** - Tiszta, világos megjelenés

**Téma specifikus elemek:**

- Navbar háttér és szöveg színek
- Kártya és űrlap stílusok
- Dropdown menük
- Accordion elemek
- Toast értesítések
- Modal ablakok
- Navbar toggler ikonok

### 🎮 Játék Kategóriák (5 db)

1. **🎮 Akció** - Intenzív csaták és izgalmas kalandok
2. **🧩 Logikai** - Gondolkodtató feladványok
3. **🏎️ Verseny** - Gyorsasági versenyek
4. **⚽ Sport** - Virtuális sportélmények
5. **👾 Retro** - Klasszikus játékok

### 📧 Kapcsolatfelvételi Rendszer

**Felhasználók számára:**

- Kapcsolat űrlap név, email, tárgy és üzenet mezőkkel
- Bejelentkezett felhasználóknál automatikus név és email kitöltés (readonly)
- Vendégek kézzel töltik ki az űrlapot
- Üzenetek adatbázisban tárolva

**Admin számára:**

- `/admin/messages` oldal (csak 'admin' felhasználónak)
- Üzenetek listázása kártyákban
- Státusz követés (új, olvasott, megválaszolt)
- Statisztikák (összesen, új, olvasott, megválaszolt)
- Akciók:
  - Olvasottnak jelölés
  - Email válasz (mailto link)
  - Üzenet törlés
- Regisztrált vs. vendég felhasználók megkülönböztetése

### 🎯 Hasznos Oldalak

- **Súgó** - Útmutatók és első lépések
- **GYIK** - Gyakran ismételt kérdések
  - Admin email válasz információ
- **Kapcsolat** - Kapcsolatfelvételi űrlap

### 🎨 Modern UI/UX

- **Animált gradient háttér** - Folyamatosan mozgó színek (színes témában)
- **Glassmorphism dizájn** - Üveges, modern felületek
- **Hover animációk** - Interaktív visszajelzések
- **Responsive layout** - Mobil és desktop támogatás
- **Bootstrap 5.3.2** - Modern komponensek
- **Bootstrap Icons** - Gazdag ikon készlet
- **Toast értesítések** - Felhasználóbarát feedback
- **Animációk ki/bekapcsolása** - Akadálymentesség

## 🛠️ Technológiák

### Backend

- **Flask 2.x** - Python web framework
- **Flask-SQLAlchemy** - ORM adatbázis kezelés
- **Werkzeug** - Jelszó hashelés (bcrypt)
- **SQLite** - Adatbázis

### Frontend

- **HTML5** - Szemantikus struktúra
- **Bootstrap 5.3.2** - UI framework
- **CSS3** - Modern animációk és témák
- **JavaScript (ES6+)** - Fetch API, AJAX
- **Jinja2** - Template engine (macro-k)

## 📝 Adatbázis Séma

### User Model

```python
id: Integer (Primary Key)
username: String(150) (Unique, Not Null)
password: String(255) (Hash, Not Null)
name: String(255) (Not Null)                    # Teljes név
email: String(255) (Not Null, Unique)           # Email cím
theme: String(50) (Default: 'colored')          # colored/dark/light
animations_enabled: Boolean (Default: True)     # Animációk engedélyezése
```

### ContactMessage Model

```python
id: Integer (Primary Key)
user_id: Integer (Foreign Key -> User.id, Nullable)  # NULL ha vendég
name: String(255) (Not Null)
email: String(255) (Not Null)
subject: String(255) (Not Null)
message: Text (Not Null)
timestamp: DateTime (Default: CURRENT_TIMESTAMP)
status: String(50) (Default: 'new')             # new/read/replied
```

## 🔒 Biztonság

- ✅ Jelszavak **bcrypt** hash-eléssel tárolva
- ✅ Session-alapú authentikáció
- ✅ Flask secret key használata
- ✅ SQL injection védelem (SQLAlchemy ORM)
- ✅ XSS védelem (Jinja2 auto-escape)
- ✅ Email egyediség validáció
- ✅ Jelszó erősség ellenőrzés (min. 6 karakter)
- ✅ Admin jogosultság ellenőrzés
- ✅ CSRF védelem form-oknál

## 🎯 API Végpontok

### Publikus

- `GET /` - Főoldal
- `GET /login` - Bejelentkezés oldal
- `POST /login` - Bejelentkezés feldolgozás
- `GET /register` - Regisztráció oldal
- `POST /register` - Regisztráció feldolgozás
- `GET /logout` - Kijelentkezés
- `GET /help` - Súgó oldal
- `GET /kapcsolat` - Kapcsolat oldal
- `POST /kapcsolat` - Üzenet küldés
- `GET /gyik` - GYIK oldal

### Játék Kategóriák

- `GET /akcio` - Akció játékok
- `GET /logikai` - Logikai játékok
- `GET /verseny` - Verseny játékok
- `GET /sport` - Sport játékok
- `GET /retro` - Retro játékok

### Beállítások (Login szükséges)

- `GET /beallitasok` - Beállítások oldal
- `POST /update-name` - Név frissítése (AJAX)
- `POST /update-email` - Email frissítése (AJAX)
- `POST /change-password` - Jelszó változtatás (AJAX)
- `POST /update-settings` - Téma és animációk (AJAX)
- `POST /delete-account` - Fiók törlése (AJAX)

### Admin (Csak 'admin' felhasználó)

- `GET /admin/messages` - Üzenetek listája
- `POST /admin/messages/<id>/mark-read` - Olvasottnak jelölés
- `POST /admin/messages/<id>/mark-replied` - Megválaszoltnak jelölés
- `POST /admin/messages/<id>/delete` - Üzenet törlése

## 👨‍💻 Fejlesztés

### Admin Fiók Létrehozása

1. Regisztrálj egy új felhasználót **'admin'** felhasználónévvel
2. Jelentkezz be
3. A navbar-ban megjelenik az "Üzenetek" menüpont

### Adatbázis Migráció Futtatása

Ha frissíted a modelleket, az adatbázis automatikusan létrejön az első futtatáskor.

### Új Témaszín Hozzáadása

1. Adj hozzá új `body[data-theme="nev"]` szabályt a `frontend/static/css/custom.css`-ben
2. Frissítsd a `frontend/templates/beallitasok.html` téma választót
3. Add hozzá a navbar és egyéb elemek stílusait

### Új Template Készítése

1. Használd a `head` és `navbar` makrókat:

```html
{% from 'partials/head.html' import head %} {% from 'partials/navbar.html'
import navbar %} {{ head('Oldal Cím') }} {{ navbar(username) }}
```

2. Add hozzá a téma attribútumot:

```html
<body
  data-theme="{{ user.theme if user else 'colored' }}"
  {%
  if
  user
  and
  not
  user.animations_enabled
  %}class="no-animations"
  {%
  endif
  %}
></body>
```

## 🧪 Tesztelés

### Regisztráció

- [ ] Név, email, felhasználónév, jelszó kitöltése
- [ ] Email egyediség ellenőrzés
- [ ] Jelszó minimum hossz (6 karakter)

### Bejelentkezés

- [ ] Helyes hitelesítő adatokkal
- [ ] Hibás jelszóval (hibaüzenet)

### Beállítások

- [ ] Név módosítása
- [ ] Email módosítása (egyediség)
- [ ] Jelszó változtatás (validáció)
- [ ] Téma váltás (3 téma tesztelése)
- [ ] Animációk ki/bekapcsolása
- [ ] Fiók törlése (dupla megerősítés)

### Kapcsolatfelvétel

- [ ] Üzenet küldés bejelentkezve (auto-fill)
- [ ] Üzenet küldés vendégként
- [ ] Üzenet adatbázisba kerül

### Admin

- [ ] Admin bejelentkezés
- [ ] Üzenetek megtekintése
- [ ] Olvasottnak jelölés
- [ ] Email válasz (mailto)
- [ ] Üzenet törlése

## 📄 Licenc

Ez egy oktatási projekt.

## 🤝 Közreműködés

Patrik - Fejlesztő
Erik - Fejlesztő
László - Fejlesztő

## 📄 Dokumentáció

A projekt részletes dokumentációja a következő fájlokban található:

- **[README.md](README.md)** - Telepítési útmutató, funkciók, API végpontok
- **[kovspec.md](kovspec.md)** - Követelmény specifikáció, use case-ek
- **[rendszerterv.md](rendszerterv.md)** - Rendszerterv, architektúra, implementáció
- **[user_storyk.md](user_storyk.md)** - User story-k Gherkin formátumban (30 db)
- **[meeting.md](meeting.md)** - Meeting jegyzetek és döntések

---

## 🎮 Unity CarGame

A projekt tartalmaz egy Unity WebGL játékot is:

- **Forráskód:** `jatekok/cargame_unity/` - Unity projekt fájlok
- **WebGL Build:** `frontend/WebCarGame/` - Böngészőben futtatható build
- **Játék elérése:** A webalkalmazásban beágyazva elérhető

### Unity Projekt Struktúra

```
jatekok/cargame_unity/
├── Assets/           # Unity eszközök és szkriptek
├── Packages/         # Unity package-ek
└── ProjectSettings/  # Unity beállítások
```

---

**Verzió:** 2.1.0  
**Utolsó frissítés:** 2025. november 11.  
**Főbb változások:**

- Projekt struktúra átrendezése (backend/frontend/jatekok)
- Unity CarGame integráció
- Téma rendszer továbbfejlesztése
- Kapcsolatfelvételi rendszer, admin felület
- Útvonalak és referenciák frissítése
