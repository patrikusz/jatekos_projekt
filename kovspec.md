# 🎮 Játékos Projekt — Követelményspecifikáció (KovSpec)

**Verzió:** 1.1.0  
**Dátum:** 2025. november 11.  
**Szerzők:** Patrik, Erik, László

---

## 1. Projekt Célja

A Játékos Projekt egy modern, reszponzív, online játék platform, ahol a felhasználók:

- Játékokat játszhatnak különböző kategóriákban (Akció, Logikai, Verseny, Sport, Retro)
- Ranglistát és scoreboard-ot láthatnak
- Kedvenceiket és barátaikat kezelhetik
- Biztonságos autentikációval regisztrálhatnak, bejelentkezhetnek, módosíthatják beállításaikat
- Kapcsolatot vehetnek fel az adminnal
- Testreszabhatják a témát és a felhasználói élményt

**Cél:** Egy interaktív, felhasználóbarát és akadálymentes játékplatform létrehozása oktatási és bemutató céllal.

---

## 2. Stakeholderek

- **Felhasználók:** regisztrált játékosok, vendégek
- **Admin:** üzenetek kezelése, statisztikák, moderáció
- **Fejlesztők:** frontend és backend implementáció
- **Tesztelők:** QA, e2e tesztek, hibajavítás

---

## 3. Funkcionális követelmények

- **F1: Menü (Navigációs sáv)**  
  Fix, reszponzív menü a főoldal tetején, tartalmazza: Kezdőlap, Kapcsolat, Bejelentkezés.  
  **Prioritás:** Magas

- **F2: Kapcsolat oldal**  
  Űrlap: név, email, tárgy, üzenet. Validálás és adatbázisba mentés.  
  **Prioritás:** Közepes

- **F3: Bejelentkezés / Regisztráció**  
  Email + jelszó, egyediség ellenőrzés, bcrypt hash, session kezelés.  
  **Prioritás:** Magas

- **F4: Sötét / Világos / Színes témák**  
  3 téma, animációk ki/bekapcsolása, localStorage persistencia.  
  **Prioritás:** Közepes

- **F5: Játék kategóriák**  
  Akció, Logikai, Verseny, Sport, Retro.  
  **Prioritás:** Magas

- **F6: Scoreboard**  
  Top10 scoreboard, játék közben overlay, végén részletes.  
  **Prioritás:** Magas

- **F7: Rekordok**  
  Mentett pontok listája, rendezés.  
  **Prioritás:** Közepes

- **F8: Kedvenc játékaim**  
  Felhasználói lista, csak bejelentkezett felhasználóknak.  
  **Prioritás:** Közepes

- **F9: Friends (Barátok)**  
  Hozzáadás, törlés, státusz online/offline.  
  **Prioritás:** Közepes

- **F10: Kommentelési rendszer**  
  Csak regisztrált felhasználóknak, XSS szűrés, max 1000 karakter.  
  **Prioritás:** Közepes

- **F11: Teljes képernyő mód**  
  Toggle gomb, zökkenőmentes váltás.  
  **Prioritás:** Közepes

- **F12: Vissza az elejére gomb**  
  Scroll-up gomb a hosszú oldalakhoz.  
  **Prioritás:** Alacsony

- **F13: Játék menü**  
  Pause, Resume, Restart, Exit.  
  **Prioritás:** Magas

- **F14: Játék mechanika**  
  Mozgás, kamera, ütközések, hang, modellek.  
  **Prioritás:** Magas

- **F15: Beállítások oldal**  
  Név, email, jelszó, téma, animációk, fiók törlés.  
  **Prioritás:** Közepes

- **F16: Admin üzenetek**  
  Üzenetek kezelése, státusz, statisztikák.  
  **Prioritás:** Közepes

---

## 4. Nem-funkcionális követelmények

- **N1: Teljesítmény**  
  Oldal < 2s, játék 30–60 FPS

- **N2: Biztonság**  
  HTTPS, bcrypt, session, CSRF, XSS védelem

- **N3: Hozzáférhetőség**  
  ARIA szerepek, fókusz, kontraszt, akadálymentesség

- **N4: Skálázhatóság**  
  Scoreboard / rekordok API ~1000 req/min

- **N5: Fennmaradás**  
  Felhasználói adatok DB-ben, beállítások localStorage-ban

---

## 5. User Story-k

### 5.1 Menü (Navigációs sáv)

**Mint:** látogató  
**Azért, hogy:** gyorsan elérjem az oldal fő részeit  
**Szeretném:** ha a weboldalon egy jól strukturált menü lenne

**Acceptance Criteria:**

- Menü fix a tetején
- Reszponzív mobilnézet
- Menüelemek: Kezdőlap, Kapcsolat, Bejelentkezés

---

### 5.2 Kapcsolat oldal

**Mint:** felhasználó  
**Azért, hogy:** üzenetet küldhessek az adminnak  
**Szeretném:** ha lenne kapcsolatfelvételi űrlap

**Acceptance Criteria:**

- Név, email, üzenet mező
- Validálja az email formátumot
- Visszajelzés a sikeres beküldés után

---

### 5.3 Bejelentkezés

**Mint:** regisztrált felhasználó  
**Azért, hogy:** hozzáférhessek a személyes funkciókhoz  
**Szeretném:** ha biztonságosan be tudnék jelentkezni

**Acceptance Criteria:**

- Email és jelszó mezők
- Hibakezelés (helytelen jelszó)
- „Emlékezz rám” opció
- Sikeres bejelentkezés után átirányítás a főoldalra

---

### 5.4 Sötét mód / Téma

**Mint:** felhasználó  
**Azért, hogy:** kényelmes legyen sötét környezetben  
**Szeretném:** ha válthatnék világos/sötét/színes témák között

**Acceptance Criteria:**

- Választás maradjon meg (localStorage)
- Animációk ki/bekapcsolása
- Váltás zökkenőmentes

---

### 5.5 Scoreboard & Rekordok

**Mint:** játékos  
**Azért, hogy:** lássam a legjobb eredményeket  
**Szeretném:** ha a top10 pontok és a saját rekordok elérhetők lennének

**Acceptance Criteria:**

- Overlay játék közben
- Mentés adatbázisba
- Rendezés és top10 lista

---

## 6. Technikai Architektúra

### 6.1 Projekt Struktúra

```
jatekos_projekt/
├── backend/              # Flask backend alkalmazás
│   ├── app.py           # Fő alkalmazás logika
│   ├── requirements.txt # Python függőségek
│   └── instance/        # Adatbázis (users.db)
├── frontend/            # Frontend alkalmazás
│   ├── static/         # CSS, JS, játékok
│   ├── templates/      # HTML sablonok
│   └── WebCarGame/     # Unity WebGL build
├── jatekok/            # Játékok forráskódja
│   └── cargame_unity/  # Unity projekt
├── kovspec.md          # Ez a fájl
├── meeting.md          # Meeting jegyzetek
├── user_storyk.md      # User story-k
└── README.md           # Telepítési útmutató
```

### 6.2 Technológiai Stack

**Backend:**

- Flask 2.x - Web framework
- Flask-SQLAlchemy - ORM
- SQLite - Adatbázis
- Werkzeug - Biztonság (bcrypt)

**Frontend:**

- HTML5, CSS3, JavaScript ES6+
- Bootstrap 5.3.2
- Jinja2 template engine

**Játék:**

- Unity Engine
- WebGL build
- C# szkriptek

### 6.3 Adatbázis Séma

**User táblázat:**

- id (PK), username (unique), password (hash)
- name, email (unique)
- theme (colored/dark/light)
- animations_enabled (boolean)

**ContactMessage táblázat:**

- id (PK), user_id (FK), name, email
- subject, message, timestamp
- status (new/read/replied)

---

## 7. Mérföldkövek és Prioritások

- **Alpha (2025-11-17):** Alapfunkciók — Menü, Login, Kapcsolat, Játék indítás
- **Beta (2025-11-24):** Scoreboard, Rekordok, Friends, Beállítások, Kommentek
- **Final Demo (December 2025):** Teljes funkcionalitás, prezentáció, tesztelt rendszer

---

## 8. Telepítési és Fejlesztési Útmutató

### 8.1 Előfeltételek

- Python 3.8+
- Git
- Unity Editor (játék fejlesztéshez)

### 8.2 Telepítés

```powershell
# 1. Repository klónozása
git clone https://github.com/patrikusz/jatekos_projekt.git
cd jatekos_projekt

# 2. Virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Függőségek telepítése
cd backend
pip install -r requirements.txt

# 4. Alkalmazás indítása
python app.py
```

### 8.3 Unity Játék Fejlesztés

1. Nyisd meg a Unity Editort
2. Open Project: `jatekok/cargame_unity/`
3. Fejlesztés után WebGL build: File → Build Settings → WebGL → Build
4. Build kimenet: `frontend/WebCarGame/`

---

## 9. Tesztelési Stratégia

- **Manuális tesztek:** Böngésző kompatibilitás, UI/UX tesztek
- **Automatizált tesztek:** Backend unit tesztek (pytest)
- **E2E tesztek:** Selenium alapú funkcionális tesztek
- **Load tesztek:** Apache JMeter / Locust

---

## 10. Karbantartás és Support

- **Bug jelentés:** GitHub Issues
- **Dokumentáció:** README.md, kovspec.md, user_storyk.md
- **Code review:** Pull request alapú
- **Verziókezelés:** Semantic versioning (x.y.z)

---
