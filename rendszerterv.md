# Rendszerterv - Játékos Projekt

**Verzió:** 1.0.0  
**Dátum:** 2025. november 11.  
**Szerzők:** Kovács Patrik, Nagy Erik, Bocskai László

---

## 1. A rendszer célja

A rendszer célja, hogy a felhasználók számára egy modern, interaktív online játék platformot biztosítson, amely különböző kategóriákban (Akció, Logikai, Verseny, Sport, Retro) kínál játékélményt. A platform lehetővé teszi a felhasználók számára, hogy regisztráljanak, testreszabják profilukat, játszhassanak különböző játékokkal, valamint nyomon kövessék eredményeiket és interakciókat más felhasználókkal.

A platform fő funkciói között szerepel a személyre szabott felhasználói élmény, amely a témák (színes, sötét, világos) és animációk be/kikapcsolásával biztosítható. A felhasználók játszhatnak Unity-alapú 3D játékokkal (pl. CarGame) közvetlenül a böngészőben WebGL technológia segítségével. A rendszer scoreboard és rekordok funkcióval rendelkezik, ahol a játékosok követhetik teljesítményüket és versenyezhetnek másokkal.

A platform modern, felhasználóbarát interfészt kínál, amely könnyen navigálható és reszponzív design elemeket tartalmaz. A felhasználók regisztrálhatnak, személyes profilt hozhatnak létre, beállíthatják preferenciáikat (téma, animációk), valamint kapcsolatba léphetnek az adminisztrátorokkal.

A rendszer kizárólag webes platformra készül, Flask backend és modern frontend technológiák (Bootstrap 5, Jinja2) használatával. Az alkalmazás reszponzív design-nal rendelkezik, így asztali és mobil eszközökön egyaránt használható. A Unity játékok WebGL build-jei közvetlenül a böngészőben futnak, biztosítva a platform-független játékélményt.

A backend REST API-szerű végpontokat biztosít az adatok kezeléséhez, amely SQLite adatbázissal kommunikál Flask-SQLAlchemy ORM használatával. A rendszer biztonságos felhasználói hitelesítést valósít meg session-alapú authentikációval és bcrypt jelszó hasheléssel, valamint biztosítja az adatok integritását és a felhasználói adatvédelmet.

## 2. Projektterv

### Projektszerepkörök, felelőségek:

**Scrum master:** Kovács Patrik  
**Product owner:** Nagy Erik

**Projektmunkások és felelőségek:**

**Design & Frontend fejlesztés:** Kovács Patrik

Feladatai: Bootstrap 5 alapú felhasználói felület kialakítása, reszponzív design implementálása, téma rendszer megvalósítása (colored/dark/light), Jinja2 template-ek készítése, animációk és modern UI/UX elemek.

**Testing:** Nagy Erik

Feladatai: tesztelés és hibakeresés.

**Backend & Adatbázis tervezés:** Bocskai László

Feladatai: Flask szerver architektúra kialakítása, REST API végpontok implementálása, adatbázis kapcsolat kezelése Flask-SQLAlchemy-vel, hitelesítési rendszer megvalósítása (session + bcrypt), AJAX végpontok, SQLite adatbázis séma tervezése, Flask-SQLAlchemy modellek létrehozása, foreign key kapcsolatok definiálása, contact message rendszer implementálása, admin funkciók.

**Unity játék fejlesztés:** Nagy Erik

Feladatai: Unity CarGame fejlesztése, WebGL build létrehozása, játék mechanikák implementálása (mozgás, kamera, scoreboard), hanghatások és modellek integrálása.

### Ütemterv:

| Funkció / Story                | Feladat / Task                   | Prioritás | Becslés (óra) | Aktuális becslés (óra) | Eltelt idő (óra) | Hátralévő idő (óra) |
| ------------------------------ | -------------------------------- | --------- | ------------- | ---------------------- | ---------------- | ------------------- |
| **Követelmény specifikáció**   | Rendszer céljainak meghatározása | 0         | 8             | 8                      | 8                | 0                   |
| **Funkcionális specifikáció**  | Use case-ek és funkciók leírása  | 0         | 10            | 10                     | 10               | 0                   |
| **Rendszerterv**               | Architektúra és adatbázis terv   | 0         | 12            | 12                     | 10               | 2                   |
| **Adattárolás**                | Adatmodell megtervezése          | 0         | 6             | 6                      | 6                | 0                   |
|                                | Adatbázis megvalósítása          | 1         | 4             | 4                      | 4                | 0                   |
|                                | Flask-SQLAlchemy modellek        | 1         | 8             | 8                      | 8                | 0                   |
| **Autentikáció**               | Session alapú rendszer           | 1         | 6             | 6                      | 6                | 0                   |
|                                | Regisztráció/bejelentkezés       | 1         | 4             | 4                      | 4                | 0                   |
|                                | Bcrypt jelszó hashing            | 1         | 2             | 2                      | 2                | 0                   |
| **Téma rendszer**              | 3 téma implementálása            | 1         | 8             | 8                      | 8                | 0                   |
|                                | Animációk ki/bekapcsolása        | 2         | 4             | 4                      | 4                | 0                   |
|                                | LocalStorage persisztencia       | 2         | 2             | 2                      | 2                | 0                   |
| **Frontend alapok**            | Bootstrap 5 projekt setup        | 1         | 3             | 3                      | 3                | 0                   |
|                                | Jinja2 template struktúra        | 1         | 6             | 6                      | 6                | 0                   |
|                                | Navbar és layout rendszer        | 1         | 4             | 4                      | 4                | 0                   |
| **Játék kategóriák**           | 5 kategória oldal létrehozása    | 2         | 10            | 10                     | 10               | 0                   |
|                                | Játéklisták és szűrés            | 2         | 6             | 6                      | 4                | 2                   |
| **Unity CarGame**              | Unity projekt fejlesztés         | 1         | 40            | 40                     | 35               | 5                   |
|                                | WebGL build integráció           | 1         | 6             | 6                      | 6                | 0                   |
|                                | Játék beágyazás weboldalba       | 1         | 4             | 4                      | 4                | 0                   |
| **Felhasználói felületek**     | Bejelentkezés/regisztráció       | 1         | 8             | 8                      | 8                | 0                   |
|                                | Dashboard és navigáció           | 2         | 6             | 6                      | 6                | 0                   |
|                                | Beállítások oldal                | 2         | 8             | 8                      | 8                | 0                   |
|                                | Profil szerkesztés               | 2         | 4             | 4                      | 4                | 0                   |
| **Kapcsolatfelvétel**          | Kapcsolat űrlap                  | 2         | 4             | 4                      | 4                | 0                   |
|                                | ContactMessage modell            | 2         | 2             | 2                      | 2                | 0                   |
|                                | Admin üzenetek kezelő            | 2         | 6             | 6                      | 6                | 0                   |
| **Scoreboard rendszer**        | Scoreboard implementálása        | 3         | 8             | 8                      | 0                | 8                   |
|                                | Rekordok tárolása                | 3         | 4             | 4                      | 0                | 4                   |
| **Projekt struktúra**          | Backend/frontend szétválasztás   | 1         | 4             | 4                      | 4                | 0                   |
|                                | Átrendezés és refaktorálás       | 1         | 6             | 6                      | 6                | 0                   |
| **Tesztelés és optimalizáció** | Manuális tesztelés               | 2         | 8             | 8                      | 6                | 2                   |
|                                | Hibák javítása                   | 2         | 6             | 6                      | 4                | 2                   |
| **Dokumentáció**               | README.md frissítése             | 2         | 3             | 3                      | 3                | 0                   |
|                                | User story-k karbantartása       | 2         | 4             | 4                      | 4                | 0                   |
|                                | Kovspec és rendszerterv          | 2         | 4             | 4                      | 3                | 1                   |

**Prioritás:** 0 = Kritikus, 1 = Magas, 2 = Közepes, 3 = Alacsony

## 3. Üzleti folyamatok bemutatása

### Főbb üzleti folyamatok:

1. **Felhasználói regisztráció és bejelentkezés**

   - Felhasználó regisztrál → Adatok validálása → Jelszó hashelése → Mentés adatbázisba
   - Bejelentkezés → Hitelesítés → Session létrehozása → Dashboard átirányítás

2. **Játék böngészés és indítás**

   - Kategória választás → Játékok listázása → Játék kiválasztása → WebGL betöltés → Játék indítás

3. **Profil és beállítások kezelése**

   - Beállítások oldal → Téma/animáció módosítás → Név/email frissítés → Jelszó változtatás
   - Adatok validálása → Mentés adatbázisba → Visszajelzés

4. **Kapcsolatfelvétel**

   - Kapcsolat oldal → Űrlap kitöltése → Üzenet küldés → Adatbázisba mentés
   - Admin oldal → Üzenetek listázása → Státusz kezelés → Email válasz

5. **Admin működés**
   - Admin bejelentkezés → Üzenetek megtekintése → Státusz módosítás → Törlés/válasz

## 4. Követelmények

### Funkcionális követelmények:

- **F1:** Felhasználói regisztráció és hitelesítés (név, email, felhasználónév, jelszó)
- **F2:** Biztonságos bejelentkezés session-alapú authentikációval
- **F3:** 3 féle téma választás (színes, sötét, világos) felhasználónként
- **F4:** Animációk ki/bekapcsolása akadálymentesség céljából
- **F5:** Játékok kategorizálása 5 kategóriába (Akció, Logikai, Verseny, Sport, Retro)
- **F6:** Unity WebGL játékok beágyazása és futtatása böngészőben
- **F7:** Kapcsolatfelvételi rendszer űrlappal és adatbázis mentéssel
- **F8:** Admin felület üzenetek kezelésére (olvasott, megválaszolt, törlés)
- **F9:** Felhasználói beállítások oldal (név, email, jelszó, téma, animációk)
- **F10:** Fiók törlése funkció dupla megerősítéssel
- **F11:** Reszponzív webes felület (Bootstrap 5)
- **F12:** Navbar rögzítése görgetés közben
- **F13:** Toast értesítések felhasználói visszajelzésekhez
- **F14:** Scoreboard és rekordok kezelése (tervezett)

### Nem funkcionális követelmények:

- **NF1:** Biztonságos adatkezelés bcrypt jelszó hasheléssel
- **NF2:** Session-alapú jogosultságkezelés
- **NF3:** CSRF és XSS védelem (Jinja2 auto-escape, Flask beépített védelem)
- **NF4:** Gyors válaszidő (< 2 másodperc oldal betöltés)
- **NF5:** WebGL játékok 30-60 FPS teljesítmény
- **NF6:** Cross-platform kompatibilitás (Windows, macOS, Linux böngészők)
- **NF7:** Felhasználóbarát, intuitív felület
- **NF8:** Stabil működés SQLite adatbázissal
- **NF9:** Reszponzív design mobil és desktop eszközökön
- **NF10:** Akadálymentesség (animációk kikapcsolhatók, megfelelő kontrasztok)

### Törvényi előírások, szabványok:

- **GDPR megfelelés:** Személyes adatok kezelése (név, email, jelszó hash)
- **Adatvédelmi tájékoztató:** Felhasználók tájékoztatása adatkezelésről
- **Cookie kezelés:** Session cookie-k használata bejelentkezéshez
- **Adatbiztonság:** Jelszavak bcrypt hashelése, SQL injection védelem ORM-mel

## 5. Funkcionális terv

### Rendszerszereplők:

- **Vendég:** Nem regisztrált felhasználó (limitált hozzáférés)
- **Regisztrált felhasználó:** Teljes funkcionalitás (játék, beállítások, üzenetek)
- **Admin:** Speciális jogosultságok (üzenetek kezelése, moderáció)

### Rendszerhasználati esetek és lefutásaik:

**VENDÉG:**

- Főoldal megtekintése
- Játék kategóriák böngészése (csak nézés)
- Regisztráció lehetősége
- Bejelentkezési felület elérése
- Kapcsolatfelvétel (vendégként)

**REGISZTRÁLT FELHASZNÁLÓ:**

- Bejelentkezés és kijelentkezés
- Játékok böngészése kategóriákban
- Unity játékok indítása és játék
- Profil adatok módosítása (név, email, jelszó)
- Téma választás (colored, dark, light)
- Animációk be/kikapcsolása
- Kapcsolatfelvétel (előre kitöltött adatokkal)
- Beállítások mentése
- Fiók törlése
- Scoreboard és rekordok megtekintése (tervezett)

**ADMIN (username='admin'):**

- Minden regisztrált felhasználói funkció
- Üzenetek megtekintése admin felületen
- Üzenetek státusz kezelése (új, olvasott, megválaszolt)
- Üzenetek törlése
- Email válasz küldése (mailto link)
- Statisztikák megtekintése

### Menü-hierarchiák:

**BEJELENTKEZÉS ELŐTT (Navbar):**

- Kezdőlap
- Kategóriák (lenyíló)
  - Akció
  - Logikai
  - Verseny
  - Sport
  - Retro
- Súgó
- GYIK
- Kapcsolat
- Bejelentkezés

**BEJELENTKEZÉS UTÁN (Navbar):**

- Kezdőlap
- Kategóriák (lenyíló)
  - Akció
  - Logikai
  - Verseny
  - Sport
  - Retro
- Súgó
- GYIK
- Kapcsolat
- **[Admin] Üzenetek** (csak admin-nak)
- Felhasználó menü (lenyíló)
  - Beállítások
  - Kijelentkezés

## 6. Fizikai környezet

### Futtatási környezet:

**Szerver oldal:**

- Python 3.8+ runtime environment
- Flask 2.x web framework
- SQLite 3 adatbázis
- Operációs rendszer: Windows/Linux/macOS

**Kliens oldal:**

- Modern webböngésző (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- JavaScript engedélyezve
- Cookies engedélyezve (session kezeléshez)
- WebGL támogatás (Unity játékokhoz)
- Minimum felbontás: 320px szélesség (mobil)

**Fejlesztői környezet:**

- Python IDE (VS Code, PyCharm)
- Unity Editor 2021.3+ (játék fejlesztéshez)
- Git verziókezelő
- Böngésző DevTools (teszteléshez)

### Fejlesztő eszközök:

- **Backend:** Python, Flask, Flask-SQLAlchemy, Werkzeug
- **Frontend:** HTML5, CSS3, JavaScript ES6+, Bootstrap 5.3.2, Jinja2
- **Adatbázis:** SQLite 3
- **Játék engine:** Unity 2021.3+
- **Build tool:** Unity WebGL Exporter
- **Verziókezelés:** Git, GitHub
- **Testing:** Böngésző DevTools, manuális tesztelés

## 7. Absztrakt domain modell

### Entitások és kapcsolataik:

**User (Felhasználó)**

- Attribútumok: id, username, password_hash, name, email, theme, animations_enabled
- Kapcsolatok: 1:N ContactMessage, 1:N GameScore (tervezett)

**ContactMessage (Kapcsolatfelvételi üzenet)**

- Attribútumok: id, user_id (nullable), name, email, subject, message, timestamp, status
- Kapcsolatok: N:1 User (opcionális)

**GameScore (Játék pontszám - tervezett)**

- Attribútumok: id, user_id, game_name, score, timestamp
- Kapcsolatok: N:1 User

### Üzleti szabályok:

1. Egy felhasználónak egyedi username és email kell legyen
2. Jelszavak bcrypt hasheléssel tárolódnak
3. Vendégek is küldhetnek kapcsolati üzenetet (user_id = NULL)
4. Admin jogosultság username alapján ('admin')
5. Téma beállítások felhasználónként mentődnek
6. Session lejárati idő: böngésző bezárásig
7. Kontakt üzenetek státuszai: new, read, replied

## 8. Architekturális terv

### Backend architektúra:

A rendszer Flask-alapú MVC (Model-View-Controller) architektúrát követ:

**Model réteg:**

- Flask-SQLAlchemy ORM modellek (User, ContactMessage)
- SQLite adatbázis a `backend/instance/users.db` útvonalon
- Automatikus adatbázis inicializáció első indításkor

**Controller réteg:**

- Flask route függvények az `app.py`-ban
- HTTP GET/POST kérések kezelése
- AJAX végpontok JSON válaszokkal
- Session-alapú jogosultság ellenőrzés

**View réteg:**

- Jinja2 template-ek a `frontend/templates/` mappában
- Parciális template-ek (navbar, head) újrafelhasználáshoz
- Bootstrap 5 komponensek
- Client-side JavaScript fetch API-val

### Rétegződés:

```
┌─────────────────────────────────────┐
│  Frontend (Templates, Static files) │
│  - Jinja2 templates                 │
│  - Bootstrap 5 CSS                  │
│  - Custom CSS (themes)              │
│  - JavaScript (AJAX, animations)    │
└─────────────────────────────────────┘
              ↕ HTTP/AJAX
┌─────────────────────────────────────┐
│  Flask Backend (app.py)             │
│  - Route handlers                   │
│  - Session management               │
│  - Business logic                   │
│  - AJAX endpoints                   │
└─────────────────────────────────────┘
              ↕ SQLAlchemy ORM
┌─────────────────────────────────────┐
│  SQLite Database                    │
│  - users.db                         │
│  - User table                       │
│  - ContactMessage table             │
└─────────────────────────────────────┘
```

### Projekt struktúra:

```
jatekos_projekt/
├── backend/              # Flask backend
│   ├── app.py           # Fő alkalmazás
│   ├── requirements.txt # Python függőségek
│   └── instance/        # Adatbázis mappa
│       └── users.db     # SQLite DB
├── frontend/            # Frontend fájlok
│   ├── templates/       # Jinja2 templates
│   │   ├── partials/   # Újrafelhasználható részek
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── beallitasok.html
│   │   └── ...
│   ├── static/         # Statikus fájlok
│   │   ├── css/       # Stíluslapok
│   │   └── games/     # Játék fájlok
│   └── WebCarGame/    # Unity WebGL build
├── jatekok/            # Játékok forráskódja
│   └── cargame_unity/ # Unity projekt
└── dokumentáció/       # MD fájlok
```

### Web kliens architektúra:

**Template rendszer:**

- Makró-alapú újrafelhasználható komponensek (navbar, head)
- Téma-specifikus CSS változók
- Dinamikus tartalom Jinja2 vezérlő struktúrákkal

**Téma rendszer:**

- CSS custom properties (változók) témánként
- `data-theme` attribútum a body-n
- JavaScript téma váltás localStorage perzisztenciával
- 3 előre definiált téma (colored, dark, light)

**AJAX kommunikáció:**

- Fetch API modern JavaScript-tel
- JSON formátumú request/response
- Toast értesítések válasz alapján
- Dinamikus tartalom frissítés újratöltés nélkül

### Adatbázis séma:

```sql
-- User tábla
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,  -- bcrypt hash
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    theme VARCHAR(50) DEFAULT 'colored',
    animations_enabled BOOLEAN DEFAULT 1
);

-- ContactMessage tábla
CREATE TABLE contact_message (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'new',
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE SET NULL
);
```

### Adatbázis kapcsolatok:

- `user` 1:N `contact_message` (egy felhasználó több üzenetet küldhet)
- `contact_message.user_id` nullable (vendégek is küldhetnek üzenetet)

### Biztonsági architektúra:

**Authentikáció:**

- Session-alapú bejelentkezés Flask session-nel
- Bcrypt jelszó hashelés (Werkzeug)
- Secure session cookie (httpOnly)

**Authorizáció:**

- Session ellenőrzés route-onként
- Admin jogosultság username alapján
- Védett végpontok átirányítanak login-ra

**Adatvédelem:**

- SQL injection védelem (SQLAlchemy ORM)
- XSS védelem (Jinja2 auto-escape)
- CSRF védelem (Flask beépített)
- Jelszó erősség validáció (min. 6 karakter)

## 9. Adatbázis terv

### Entitás-kapcsolat diagram:

```
┌─────────────────────┐
│       User          │
├─────────────────────┤
│ id (PK)             │
│ username (UNIQUE)   │
│ password            │
│ name                │
│ email (UNIQUE)      │
│ theme               │
│ animations_enabled  │
└─────────────────────┘
          │ 1
          │
          │ *
┌─────────────────────┐
│  ContactMessage     │
├─────────────────────┤
│ id (PK)             │
│ user_id (FK, NULL)  │
│ name                │
│ email               │
│ subject             │
│ message             │
│ timestamp           │
│ status              │
└─────────────────────┘
```

### Tábla részletek:

**user tábla:**
| Mező | Típus | Megszorítás | Leírás |
|------|-------|-------------|---------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Egyedi azonosító |
| username | VARCHAR(150) | UNIQUE, NOT NULL | Felhasználónév |
| password | VARCHAR(255) | NOT NULL | Bcrypt hash |
| name | VARCHAR(255) | NOT NULL | Teljes név |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Email cím |
| theme | VARCHAR(50) | DEFAULT 'colored' | Téma preferencia |
| animations_enabled | BOOLEAN | DEFAULT 1 | Animációk engedélyezése |

**contact_message tábla:**
| Mező | Típus | Megszorítás | Leírás |
|------|-------|-------------|---------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Egyedi azonosító |
| user_id | INTEGER | FOREIGN KEY (nullable) | Küldő felhasználó ID |
| name | VARCHAR(255) | NOT NULL | Küldő neve |
| email | VARCHAR(255) | NOT NULL | Küldő email címe |
| subject | VARCHAR(255) | NOT NULL | Üzenet tárgya |
| message | TEXT | NOT NULL | Üzenet szövege |
| timestamp | DATETIME | DEFAULT CURRENT_TIMESTAMP | Küldés időpontja |
| status | VARCHAR(50) | DEFAULT 'new' | Státusz (new/read/replied) |

### Indexek:

- `user.username` - UNIQUE index (bejelentkezés gyorsítása)
- `user.email` - UNIQUE index (duplikáció ellenőrzés)
- `contact_message.status` - INDEX (admin felület szűrés)
- `contact_message.timestamp` - INDEX (időrendi rendezés)

## 10. Implementációs terv

### Web Frontend:

A webes felület Bootstrap 5, HTML5, CSS3 és JavaScript ES6+ nyelven készül. A template-ek Jinja2 motor-t használnak a backend adatok dinamikus megjelenítéséhez.

**Komponens struktúra:**

- **Partials:** Újrafelhasználható makrók (navbar, head)
- **Layouts:** Oldal template-ek kategóriánként
- **Static assets:** CSS (custom.css), játékok, képek

**Téma implementáció:**

```css
/* Színes téma */
body[data-theme="colored"] {
  --bg-gradient: linear-gradient(...);
  --navbar-bg: rgba(255, 255, 255, 0.1);
  --text-color: white;
}

/* Sötét téma */
body[data-theme="dark"] {
  --bg-color: #121212;
  --navbar-bg: #1e1e1e;
  --text-color: #e0e0e0;
}

/* Világos téma */
body[data-theme="light"] {
  --bg-color: #f5f5f5;
  --navbar-bg: white;
  --text-color: #333;
}
```

**JavaScript funkciók:**

- AJAX kérések fetch API-val
- Toast értesítések Bootstrap Toast komponenssel
- Téma váltás és localStorage mentés
- Form validáció és submit kezelés

### Backend implementáció:

**Flask alkalmazás struktúra:**

```python
# app.py fő részei

from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Alkalmazás konfiguráció
app = Flask(__name__,
            template_folder='../frontend/templates',
            static_folder='../frontend/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/users.db'
app.secret_key = 'jatekos_projekt_secret_key'

# ORM modellek
class User(db.Model):
    # ...mezők és kapcsolatok

class ContactMessage(db.Model):
    # ...mezők és kapcsolatok

# Route-ok
@app.route('/')
def home():
    # Kezdőlap logika

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Bejelentkezés logika

@app.route('/beallitasok')
def beallitasok():
    # Beállítások oldal (session ellenőrzés)

# AJAX végpontok
@app.route('/update-settings', methods=['POST'])
def update_settings():
    # JSON válasz
```

**Kódolási konvenciók:**

- PEP 8 Python stílus útmutató
- Függvények: snake_case
- Osztályok: PascalCase
- Változók: snake_case
- Kommentek magyar nyelven
- Docstring-ek fontos függvényeknél

### Unity játék integráció:

**WebGL Build folyamat:**

1. Unity Editor-ban fejlesztés
2. Build Settings → WebGL platform
3. Build és export `frontend/WebCarGame/` mappába
4. Loader script és assets automatikusan generálódnak

**Beágyazás HTML-be:**

```html
<iframe src="{{ iframe_src }}" width="960" height="600" allowfullscreen>
</iframe>
```

**Flask route játékhoz:**

```python
@app.route('/play/<game_name>')
def play_game(game_name):
    iframe_src = url_for('static', filename=f'games/{game_name}/index.html')
    return render_template('game_embed.html', iframe_src=iframe_src)
```

## 11. Tesztterv

### Tesztelési stratégia:

**1. Unit tesztek (Backend):**

- Felhasználó regisztráció validáció
- Jelszó hashelés és ellenőrzés
- Adatbázis modellek kapcsolatai
- AJAX végpontok válaszai

**2. Integrációs tesztek:**

- Frontend-backend kommunikáció
- Adatbázis CRUD műveletek
- Session kezelés és jogosultságok
- Template renderelés adatokkal

**3. Funkcionális tesztek:**

| Teszt             | Lépések                                                               | Elvárt eredmény                            |
| ----------------- | --------------------------------------------------------------------- | ------------------------------------------ |
| Regisztráció      | 1. Regisztrációs űrlap<br>2. Adatok kitöltése<br>3. Submit            | Sikeres regisztráció, átirányítás login-ra |
| Bejelentkezés     | 1. Login oldal<br>2. Helyes adatok<br>3. Submit                       | Session létrehozás, dashboard átirányítás  |
| Téma váltás       | 1. Beállítások oldal<br>2. Téma választás<br>3. Mentés                | Téma változás, localStorage frissítés      |
| Kapcsolatfelvétel | 1. Kapcsolat oldal<br>2. Űrlap kitöltés<br>3. Küldés                  | Üzenet DB-be mentés, toast értesítés       |
| Admin üzenetek    | 1. Admin bejelentkezés<br>2. Üzenetek oldal<br>3. Státusz változtatás | Sikeres státusz frissítés                  |
| Játék indítás     | 1. Kategória választás<br>2. Játék kiválasztás<br>3. Play gomb        | WebGL betöltés, játék elindul              |

## 12. Telepítési terv

### Fejlesztői telepítés:

**Előfeltételek:**

- Python 3.8 vagy újabb
- Git verziókezelő
- Modern webböngésző
- Unity Editor (játék fejlesztéshez, opcionális)

**Lépések:**

1. **Repository klónozása:**

```powershell
git clone https://github.com/patrikusz/jatekos_projekt.git
cd jatekos_projekt
```

2. **Virtual environment létrehozása:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# vagy
.venv\Scripts\activate.bat  # Windows CMD
# vagy
source .venv/bin/activate    # Linux/macOS
```

3. **Függőségek telepítése:**

```powershell
cd backend
pip install -r requirements.txt
```

4. **Adatbázis inicializálása:**

```powershell
# Az első futtatáskor automatikusan létrejön
python app.py
```

5. **Alkalmazás indítása:**

```powershell
# backend mappában
python app.py

# Böngészőben megnyitni:
# http://127.0.0.1:5000/
```

### Production telepítés:

**Szerver követelmények:**

- Linux/Windows server
- Python 3.8+
- Nginx vagy Apache webszerver
- WSGI server (Gunicorn vagy uWSGI)

**Deployment lépések:**

1. **Kód telepítése szerverre:**

```bash
git clone https://github.com/patrikusz/jatekos_projekt.git
cd jatekos_projekt
```

2. **Virtual environment és függőségek:**

```bash
python3 -m venv .venv
source .venv/bin/activate
cd backend
pip install -r requirements.txt
pip install gunicorn  # WSGI server
```

3. **Környezeti változók:**

```bash
export FLASK_ENV=production
export SECRET_KEY='<erős_random_kulcs>'
```

4. **Gunicorn indítása:**

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

5. **Nginx konfiguráció:**

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/jatekos_projekt/frontend/static;
    }
}
```

### Docker telepítés (opcionális):

**Dockerfile:**

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "backend/app.py"]
```

**Docker Compose:**

```yaml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./backend/instance:/app/backend/instance
```

## 13. Karbantartási terv

### Folyamatos üzemeltetés:

Az alkalmazás folyamatos üzemeltetése és karbantartása magában foglalja:

- Programhibák elhárítása
- Felhasználói visszajelzések alapján módosítások
- Biztonsági frissítések alkalmazása
- Új funkciók hozzáadása
- Teljesítmény optimalizáció

### Karbantartási típusok:

**1. Corrective Maintenance (Javító karbantartás):**

- Felhasználók által jelentett hibák kijavítása
- Session problémák megoldása
- Adatbázis integritás javítása
- UI/UX hibák korrigálása
- WebGL játék betöltési hibák

**2. Adaptive Maintenance (Adaptív karbantartás):**

- Új böngésző verziókkal való kompatibilitás
- Flask és függőségek frissítése
- Bootstrap verzió upgrade-ek
- Unity WebGL API változások követése
- Biztonsági szabványok frissítése

**3. Perfective Maintenance (Tökéletesítő karbantartás):**

- Új játékok hozzáadása
- Scoreboard és rekordok implementálása
- Barát rendszer fejlesztése
- Kommentelési funkció hozzáadása
- Teljesítmény optimalizáció
- Új témák létrehozása

**4. Preventive Maintenance (Megelőző karbantartás):**

- Kód refaktorálás
- Adatbázis optimalizáció
- Biztonsági audit
- Dependency frissítések
- Backup rendszer ellenőrzése

### Rendszeres karbantartási feladatok:

**Napi:**

- Logfájlok ellenőrzése
- Hibajelentések áttekintése
- Adatbázis kapcsolat monitoring

**Heti:**

- Biztonsági frissítések ellenőrzése
- Teljesítmény metrikák áttekintése
- Felhasználói visszajelzések feldolgozása

**Havi:**

- Adatbázis backup készítése
- Dependency-k frissítése
- Kód review és refaktorálás
- Dokumentáció frissítése

**Negyedéves:**

- Teljes biztonsági audit
- Teljesítmény optimalizáció
- Nagy funkció release-ek
- Felhasználói survey és UX fejlesztések

### Backup stratégia:

**Adatbázis backup:**

- Napi automatikus backup (SQLite fájl másolása)
- Heti full backup archiválása
- 30 napos backup retention policy
- Backup teszt és restore gyakorlatok

**Kód backup:**

- Git verziókezelő (GitHub)
- Branch stratégia (main, develop, feature/\*)
- Tag-ek release-ekhez
- Pull request review folyamat

### Support és hibaelhárítás:

**Hibabejelentés:**

- GitHub Issues használata
- Email: admin@jatekosprojekt.hu (példa)
- Kapcsolat űrlap a weboldalon

**Prioritási szintek:**

- **Critical:** Teljes rendszer leállás (< 1 óra válaszidő)
- **High:** Fő funkció nem működik (< 4 óra válaszidő)
- **Medium:** Kisebb funkció hiba (< 24 óra válaszidő)
- **Low:** Kozmetikai hiba, javítási javaslat (< 1 hét)

### Verziókezelés:

**Semantic Versioning (x.y.z):**

- **Major (x):** Jelentős változások, backwards incompatible
- **Minor (y):** Új funkciók, backwards compatible
- **Patch (z):** Hibajavítások

**Példa:**

- v1.0.0 - Első stabil release
- v1.1.0 - Scoreboard funkció hozzáadása
- v1.1.1 - Session bug javítás
- v2.0.0 - Új authentikáció rendszer

### Monitoring és logging:

**Logolás:**

- Flask beépített logging
- Hiba üzenetek fájlba írása
- Felhasználói aktivitás naplózása (login, logout)

**Monitoring metrikák:**

- Aktív felhasználók száma
- Átlagos oldal betöltési idő
- Játék indítások száma
- Üzenetek száma és státusza
- Hiba rate (4xx, 5xx válaszok)

---

**Dokumentum vége**

Készítette: Kovács Patrik, Nagy Erik, Bocskai László  
Utolsó módosítás: 2025. november 11.  
Verzió: 1.0.0
