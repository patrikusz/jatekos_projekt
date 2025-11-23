# 🎮 Játékos Projekt — Követelményspecifikáció (KovSpec)

**Verzió:** 1.2.0  
**Dátum:** 2025. november 23.  
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

## 3. Funkcionális és Nem-funkcionális Követelmények

| Modul           | ID  | Név                         | V.  | Kifejtés                                                                                             |
| --------------- | --- | --------------------------- | --- | ---------------------------------------------------------------------------------------------------- |
| Navigáció       | K1  | Menü (Navigációs sáv)       | 1.0 | Fix, reszponzív menü a főoldal tetején, tartalmazza: Kezdőlap, Barátaim, Beállítások, Bejelentkezés. |
| Tartalom        | K2  | Kezdőlap                    | 1.0 | Legyen egy kezdőlap, ahol bemutatjuk az oldalt és megjelenítjük a játék kategóriákat.                |
| Tartalom        | K3  | Játék kategóriák            | 1.0 | A játékok legyenek kategóriákba rendezve: Akció, Logikai, Verseny, Sport, Retro.                     |
| Tartalom        | K4  | Játék részletek oldal       | 1.0 | Minden játékhoz legyen külön oldal leírással és indítási lehetőséggel.                               |
| Játék           | K5  | Játék indítása              | 1.0 | A felhasználók el tudják indítani a játékokat a böngészőben.                                         |
| Játék           | K6  | Unity CarGame integráció    | 1.0 | A Unity WebGL játék beágyazva legyen a weboldalba és működjön zökkenőmentesen.                       |
| Játék           | K7  | Játék menü                  | 1.0 | Játék közben elérhető menü: Pause, Resume, Restart, Exit opcióval.                                   |
| Játék           | K8  | Scoreboard rendszer         | 1.0 | Játék közben overlay scoreboard, játék végén részletes pontszám és toplista.                         |
| Játék           | K9  | Rekordok tárolása           | 1.0 | A legjobb pontszámok mentése és megjelenítése top10 listában.                                        |
| Játék           | K10 | Teljes képernyő mód         | 1.0 | Toggle gomb a játékok teljes képernyős megjelenítéséhez.                                             |
| Játék           | K11 | Játék mozgás és vezérlés    | 1.0 | A karakterek irányítása billentyűzettel, valós idejű mozgás és ütközésdetektálás.                    |
| Játék           | K12 | Játék kamera rendszer       | 1.0 | A kamera automatikusan kövesse a játékos karakterét, sima animációval.                               |
| Játék           | K13 | Játék hang és zene          | 1.0 | Hanghatások eseményekhez, háttérzene, ki/bekapcsolható a beállításokban.                             |
| Játék           | K14 | Játék modellek és textúrák  | 1.0 | 3D modellek megfelelő textúrázással, optimalizált teljesítménnyel.                                   |
| Autentikáció    | K15 | Regisztráció                | 1.0 | Email, név, jelszó alapú regisztráció, egyediség ellenőrzéssel.                                      |
| Autentikáció    | K16 | Bejelentkezés               | 1.0 | Email és jelszó alapú bejelentkezés, bcrypt hash, session kezelés.                                   |
| Autentikáció    | K17 | Kijelentkezés               | 1.0 | Biztonságos kijelentkezés, session törlése.                                                          |
| Autentikáció    | K18 | Jelszó módosítása           | 1.0 | Bejelentkezett felhasználók módosíthassák jelszavukat a beállításokban.                              |
| Felhasználó     | K19 | Profil megtekintése         | 1.0 | A felhasználók lássák saját profiljukat: név, email, beállítások.                                    |
| Felhasználó     | K20 | Beállítások oldal           | 1.0 | Név, email módosítása, téma váltás, animációk be/kikapcsolása, fiók törlés.                          |
| Felhasználó     | K21 | Téma rendszer               | 1.0 | 3 téma közül választás: Színes, Sötét, Világos mód.                                                  |
| Felhasználó     | K22 | Animációk vezérlése         | 1.0 | Felhasználók ki/bekapcsolhatják az oldal animációit.                                                 |
| Felhasználó     | K23 | Fiók törlése                | 1.0 | Jelszóval és megerősítéssel véglegesen törölhető a felhasználói fiók.                                |
| Közösség        | K24 | Barátok hozzáadása          | 1.0 | Email cím alapán barátok hozzáadása az oldalon belül.                                               |
| Közösség        | K25 | Barátlista megjelenítése    | 1.0 | A felhasználó lássa barátainak listáját olvasatlan üzenetek számával.                                |
| Közösség        | K26 | Chat rendszer               | 1.0 | Barátok között privát chat, üzenetküldés és fogadás valós időben.                                    |
| Közösség        | K27 | Chat értesítések            | 1.0 | Toast értesítés új üzenetekről, bárhol az oldalon, böngésző értesítés támogatással.                  |
| Design          | K28 | Dropdown menü z-index       | 1.1 | Dropdown menü megfelelő rétegzése, z-index optimalizálás.                                            |
| Design          | K29 | Játék oldal tisztítás       | 1.1 | Zavaró elemek eltávolítása a játék beágyazási oldalról.                                              |
| Kommunikáció    | K30 | Kapcsolat oldal             | 1.0 | Űrlap kapcsolatfelvételhez: név, email, tárgy, üzenet mezőkkel.                                      |
| Kommunikáció    | K31 | Kapcsolati űrlap validálás  | 1.0 | Email formátum validálása, kötelező mezők ellenőrzése.                                               |
| Kommunikáció    | K32 | Admin üzenetek kezelése     | 1.0 | Admin lássa az összes beérkezett üzenetet, státusz változtatással (új/olvasott/megválaszolt).        |
| Design          | K33 | Reszponzív design           | 1.0 | Az oldal mobilon, tableten és számítógépen is tökéletesen jelenjen meg.                              |
| Design          | K34 | Egységes dizájn nyelv       | 1.0 | Glass morphism kártyák, gradient gombok, egységes színvilág.                                         |
| Design          | K35 | Kategória ikonok            | 1.0 | Minden játék kategóriának saját emoji ikonja legyen.                                                 |
| Design          | K36 | Toast notification rendszer | 1.0 | Egységes visszajelzés rendszer sikeres és sikertelen műveletekhez.                                   |
| Navigáció       | K37 | Görgetés közbeni menü       | 1.0 | A menü fix pozícióban maradjon görgetés közben.                                                      |
| Navigáció       | K38 | Vissza az elejére gomb      | 1.0 | Hosszú oldalakon gomb az oldal tetejére való visszaugráshoz.                                         |
| Navigáció       | K39 | Keresés funkció             | 1.0 | Játékok keresése név alapján a kezdőlapon.                                                           |
| Tartalom        | K40 | GYIK oldal                  | 1.0 | Gyakran Ismételt Kérdések oldal accordion formátumban.                                               |
| Tartalom        | K41 | Súgó oldal                  | 1.0 | Részletes útmutató az oldal funkcióinak használatához.                                               |
| Technikai       | K42 | Gyors betöltés              | 1.0 | Az oldal 2 másodpercen belül betöltődjön.                                                            |
| Technikai       | K43 | Böngésző támogatás          | 1.0 | Működjön Chrome, Edge, Firefox legújabb verzióiban.                                                  |
| Technikai       | K44 | Adatbázis séma              | 1.0 | SQLite adatbázis User, ContactMessage, Friendship, ChatMessage táblákkal.                            |
| Technikai       | K45 | Session kezelés             | 1.0 | Biztonságos session alapú bejelentkezés Flask-ben.                                                   |
| Technikai       | K46 | Jelszó biztonság            | 1.0 | Bcrypt hash használata jelszavak tárolásához.                                                        |
| Technikai       | K47 | XSS védelem                 | 1.0 | Input validálás és sanitizálás minden felhasználói bevitelnél.                                       |
| Technikai       | K48 | HTTPS támogatás             | 1.0 | Az oldal HTTPS-en keresztül is elérhető legyen production környezetben.                              |
| Technikai       | K49 | WebGL támogatás             | 1.0 | Unity WebGL játékok futtatása modern böngészőkben.                                                   |
| Technikai       | K50 | LocalStorage használat      | 1.0 | Téma és animáció beállítások tárolása böngészőben.                                                   |
| Fejlesztés      | K51 | Projekt struktúra           | 1.0 | Tiszta elválasztás: backend/, frontend/, jatekok/ mappák.                                            |
| Fejlesztés      | K52 | Verziókezelés               | 1.0 | Git használata, semantic versioning (x.y.z).                                                         |
| Fejlesztés      | K53 | Dokumentáció                | 1.0 | Követelményspecifikáció, user story-k, README fájlok.                                                |
| Fejlesztés      | K54 | Kód minőség                 | 1.0 | Tiszta, refaktorált kód, ismétlődések elkerülése.                                                    |
| Tesztelés       | K55 | Manuális tesztek            | 1.0 | UI/UX tesztelés különböző eszközökön és böngészőkben.                                                |
| Tesztelés       | K56 | Automatizált tesztek        | 1.0 | Backend unit tesztek pytest-tel.                                                                     |
| Tesztelés       | K57 | E2E tesztek                 | 1.0 | End-to-end funkcionális tesztek Selenium-mal.                                                        |
| Hozzáférhetőség | K58 | ARIA szerepek               | 1.0 | Megfelelő ARIA címkék a képernyőolvasók támogatásához.                                               |
| Hozzáférhetőség | K59 | Fókusz kezelés              | 1.0 | Billentyűzettel való navigáció támogatása.                                                           |
| Hozzáférhetőség | K60 | Kontraszt arányok           | 1.0 | Színek kontrasztja megfeleljen a WCAG irányelveknek.                                                 |
| Skálázhatóság   | K61 | API teljesítmény            | 1.0 | Scoreboard és chat API ~1000 kérés/perc kezelése.                                                    |
| Skálázhatóság   | K62 | Adatbázis optimalizálás     | 1.0 | Indexek és query optimalizálás a gyors adatlekéréshez.                                               |

---

## 4. Technikai Architektúra

### 4.1 Projekt Struktúra

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

### 4.2 Technológiai Stack

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

### 4.3 Adatbázis Séma

**User táblázat:**

- id (PK), username (unique), password (hash)
- name, email (unique)
- theme (colored/dark/light)
- animations_enabled (boolean)

**ContactMessage táblázat:**

- id (PK), user_id (FK), name, email
- subject, message, timestamp
- status (new/read/replied)

**Friendship táblázat:**

- id (PK), user_id (FK), friend_id (FK)
- created_at (timestamp)

**ChatMessage táblázat:**

- id (PK), sender_id (FK), receiver_id (FK)
- message (text), timestamp
- is_read (boolean)

---

## 5. Mérföldkövek és Prioritások

- **Alpha (2025-11-17):** Alapfunkciók — Menü, Login, Kapcsolat, Játék indítás
- **Beta (2025-11-24):** Scoreboard, Rekordok, Friends, Beállítások, Chat
- **Final Demo (December 2025):** Teljes funkcionalitás, prezentáció, tesztelt rendszer

---

## 6. Telepítési és Fejlesztési Útmutató

### 6.1 Előfeltételek

- Python 3.8+
- Git
- Unity Editor (játék fejlesztéshez)

### 6.2 Telepítés

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

### 6.3 Unity Játék Fejlesztés

1. Nyisd meg a Unity Editort
2. Open Project: `jatekok/cargame_unity/`
3. Fejlesztés után WebGL build: File → Build Settings → WebGL → Build
4. Build kimenet: `frontend/WebCarGame/`

---

## 7. Tesztelési Stratégia

- **Manuális tesztek:** Böngésző kompatibilitás, UI/UX tesztek
- **Automatizált tesztek:** Backend unit tesztek (pytest)
- **E2E tesztek:** Selenium alapú funkcionális tesztek
- **Load tesztek:** Apache JMeter / Locust

---

## 8. Karbantartás és Support

- **Bug jelentés:** GitHub Issues
- **Dokumentáció:** README.md, kovspec.md, user_storyk.md
- **Code review:** Pull request alapú
- **Verziókezelés:** Semantic versioning (x.y.z)

---
