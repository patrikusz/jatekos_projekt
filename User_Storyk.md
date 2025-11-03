# 📝 Backlog – Weboldal Funkciók

## 1. Menü (Navigációs sáv)
**User Story**  
Mint látogató, szeretném, hogy a weboldalon egy jól strukturált menü legyen, amin keresztül gyorsan elérhetem az oldal fő részeit (pl. Kezdőlap, Kapcsolat, Bejelentkezés).

**Acceptance Criteria**
- Menü fixen jelenjen meg az oldal tetején.
- Legyen reszponzív mobilnézetben is.
- Menüelemek: Kezdőlap, Kapcsolat, Bejelentkezés.

**Prioritás**: Magas  
**Szerző**: Anna

Gherkin nyelven:
Feature: Menü (Navigációs sáv)
  Mint látogató
  Azért, hogy gyorsan elérjem az oldal fő részeit
  Szeretném, ha a weboldalon egy jól strukturált menü jelenne meg

  Background:
    Given a weboldal betöltődött

  Scenario: A menü megjelenik az oldal tetején
    Then a menü fixen jelenik meg az oldal tetején

  Scenario: A menü reszponzív mobilnézetben
    When a felhasználó mobil eszközről nyitja meg az oldalt
    Then a menü megfelelően jelenik meg reszponzív elrendezésben

  Scenario: A menüelemek megjelenítése
    Then a menü tartalmazza a következő elemeket:
      | Menüelem      |
      | Kezdőlap      |
      | Kapcsolat     |
      | Bejelentkezés |

  @prioritas:Magas
  @szerzo:Anna


---

## 2. Kapcsolat oldal
**User Story**  
Mint felhasználó, szeretnék egy Kapcsolat oldalt, ahol elküldhetem az üzenetemet az oldal üzemeltetőinek.

**Acceptance Criteria**
- Tartalmazzon nevet, emailt és üzenet mezőt.
- Validálja a bevitt adatokat (pl. email formátum).
- Sikeres beküldés után jelenjen meg visszajelzés.

**Prioritás**: Közepes  
**Szerző**: Bence

---

## 3. Login (Bejelentkezés)
**User Story**  
Mint regisztrált felhasználó, szeretnék be tudni jelentkezni, hogy elérhessem a személyes funkciókat.

**Acceptance Criteria**
- Email és jelszó mezők.
- Hibakezelés: helytelen jelszó esetén hibaüzenet.
- "Emlékezz rám" opció.
- Sikeres bejelentkezés után átirányítás a főoldalra.

**Prioritás**: Magas  
**Szerző**: Gergő

---

## 4. Sötét mód (Dark mode)
**User Story**  
Mint felhasználó, szeretnék sötét módot kapcsolni, hogy kényelmesebb legyen a használat sötét környezetben.

**Acceptance Criteria**
- Lehessen váltani világos és sötét mód között.
- A választás maradjon meg (pl. localStorage segítségével).
- A váltás animáció nélkül történjen.

**Prioritás**: Közepes  
**Szerző**: Dóra

---
