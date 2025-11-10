# 🎮 Funkcióspecifikáció (Funkspec)

**Verzió:** 1.0.0  
**Dátum:** 2025. november 9.  
**Szerzők:** Patrik, Erik, László  

---

## 1. Rendszer Áttekintés

- Flask backend, reszponzív frontend, SQLite adatbázis  
- Modulok:  
  - Felhasználói rendszer: regisztráció, login, beállítások  
  - Téma modul: colored / dark / light  
  - Játék modul: 5 kategória, mozgás, kamera, hang, modellek  
  - Scoreboard & rekordok  
  - Kapcsolat & admin modul  

---

## 2. Modulok Funkcióleírása

### 2.1 Felhasználói rendszer
- Regisztráció: email egyediség, bcrypt hash, session  
- Login: email + jelszó, hibakezelés, „emlékezz rám”  
- Beállítások: név, email, jelszó, téma, animációk, fiók törlés  

### 2.2 Téma modul
- 3 téma: colored / dark / light  
- Animációk ki/bekapcsolása  
- localStorage-ban tárolt választás  

### 2.3 Játék modul
- Kategóriák: Akció, Logikai, Verseny, Sport, Retro  
- Mozgás, kamera, ütközés, modellek  
- Scoreboard overlay és végső eredmény  
- Teljes képernyő mód  

### 2.4 Scoreboard & Rekordok
- Top10 lista  
- Saját rekordok mentése és lekérdezése  
- Rendezés és statisztika  

### 2.5 Kapcsolat & Admin
- Űrlap: név, email, tárgy, üzenet  
- Admin üzenetek: státusz (new/read/replied), statisztikák, törlés  

---

## 3. Adatbázis Modellek

```python
class User(db.Model):
    id: int
    username: str
    password: str
    name: str
    email: str
    theme: str
    animations_enabled: bool

class ContactMessage(db.Model):
    id: int
    user_id: int
    name: str
    email: str
    subject: str
    message: str
    timestamp: datetime
    status: str
```
---

## 4. API Végpontok
- /login (GET/POST) — Bejelentkezés
- /register (GET/POST) — Regisztráció
- /logout (GET) — Kijelentkezés
- /beallitasok (GET/POST) — Beállítások oldala, módosítás
- /kapcsolat (GET/POST) — Kapcsolatfelvétel
- /admin/messages (GET/POST) — Admin üzenetek kezelése
