# 🎮 Játékos Projekt — Követelményspecifikáció (KovSpec)

**Verzió:** 1.0.0  
**Dátum:** 2025. november 9.  
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

## 6. Mérföldkövek és Prioritások

- **Alpha (2025-11-17):** Alapfunkciók — Menü, Login, Kapcsolat, Játék indítás  
- **Beta (2025-11-24):** Scoreboard, Rekordok, Friends, Beállítások, Kommentek  
- **Final Demo (December 2025):** Teljes funkcionalitás, prezentáció, tesztelt rendszer  

---
