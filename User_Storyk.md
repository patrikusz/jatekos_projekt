# 📝 Backlog – Weboldal Funkciók

**Projekt:** Játékos Projekt  
**Verzió:** 1.1.0  
**Utolsó frissítés:** 2025. november 11.

---

## 📁 Projekt Struktúra Referencia

```
jatekos_projekt/
├── backend/          # Flask backend (app.py, models, API)
├── frontend/         # Templates, static fájlok, WebCarGame
├── jatekok/          # Unity CarGame forráskód
└── dokumentáció/     # kovspec.md, user_storyk.md, README.md
```

---

# language: hu

######################################

# 1. Menü (Navigációs sáv)

######################################

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
| Menüelem |
| Kezdőlap |
| Kapcsolat |
| Bejelentkezés |

@prioritas:Magas
@szerzo:Anna

######################################

# 2. Kapcsolat oldal

######################################

Feature: Kapcsolat oldal
Mint felhasználó
Azért, hogy üzenetet küldhessek az oldal üzemeltetőinek
Szeretném, ha lenne egy Kapcsolat oldal űrlappal

Background:
Given a weboldal betöltődött

Scenario: Kapcsolat űrlap megjelenítése
Then az oldal tartalmaz egy űrlapot a következő mezőkkel:
| Mező |
| Név |
| Email |
| Üzenet |

Scenario: Adatbevitel validálása
When a felhasználó hibás email címet ad meg
Then a rendszer figyelmeztető üzenetet jelenít meg

Scenario: Sikeres üzenetküldés
When a felhasználó helyesen kitölti az űrlapot és elküldi
Then megjelenik egy visszajelzés, hogy az üzenet sikeresen elküldve

@prioritas:Kozepes
@szerzo:Bence

######################################

# 3. Bejelentkezés (Login)

######################################

Feature: Bejelentkezés
Mint regisztrált felhasználó
Azért, hogy elérjem a személyes funkciókat
Szeretnék be tudni jelentkezni az oldalra

Background:
Given a weboldal betöltődött

Scenario: Bejelentkezési űrlap megjelenítése
Then az oldal tartalmaz egy űrlapot az alábbi mezőkkel:
| Mező |
| Email |
| Jelszó |
| Emlékezz rám |

Scenario: Helytelen jelszó kezelése
When a felhasználó helytelen jelszót ad meg
Then a rendszer hibaüzenetet jelenít meg: "Helytelen jelszó"

Scenario: Sikeres bejelentkezés
When a felhasználó helyesen adja meg az emailt és jelszót
Then a rendszer átirányítja a felhasználót a főoldalra

@prioritas:Magas
@szerzo:Gergő

######################################

# 4. Sötét mód (Dark mode)

######################################

Feature: Sötét mód (Dark mode)
Mint felhasználó
Azért, hogy kényelmesebb legyen a használat sötét környezetben
Szeretném, ha válthatnék világos és sötét mód között

Background:
Given a weboldal betöltődött

Scenario: Sötét mód váltás
When a felhasználó átvált sötét módra
Then az oldal sötét színsémára vált

Scenario: Világos mód visszaállítása
When a felhasználó visszavált világos módra
Then az oldal világos színsémára vált

Scenario: Beállítás megőrzése
When a felhasználó újra megnyitja az oldalt
Then az oldal megőrzi az utoljára választott módot (localStorage alapján)

@prioritas:Kozepes
@szerzo:Dóra

######################################

# 5. Reszponzív design

######################################

Feature: Reszponzív design
Mint látogató
Azért, hogy kényelmesen tudjam használni az oldalt minden eszközön
Szeretném, ha a weboldal reszponzív módon jelenne meg

Background:
Given a weboldal betöltődött

Scenario: Az oldal elrendezése alkalmazkodik a képernyőmérethez
When a felhasználó különböző eszközről nyitja meg az oldalt
Then az oldal elemei megfelelően igazodnak a képernyő méretéhez

Scenario: A tartalom olvasható marad mobilon
When a felhasználó mobilnézetben megtekinti az oldalt
Then a szöveg és gombok jól láthatóak és kattinthatóak

Scenario: Nincs vízszintes görgetés
Then az oldal nem igényel vízszintes görgetést mobil eszközön

@prioritas:Magas
@szerzo:Eszter

---

######################################

# 5. Rekordok tábla

######################################

Feature: Rekordok tábla
Mint játékos
Azért, hogy lássam a legjobb eredményeket
Szeretném, ha lenne egy rekordok tábla a játékban

Background:
Given a játék véget ért

Scenario: A rekordok megjelenítése
Then a rekordok tábla listázza a játékos nevét, pontszámát és dátumát

Scenario: A rekordok rendezése
When a felhasználó rendezést választ pontszám szerint
Then a rekordok pontszám szerint sorrendben jelennek meg

Scenario: Csak a legjobb rekordok megjelenítése
Then maximum 10 rekord látható a táblában

@prioritas:Kozepes
@szerzo:Balazs

---

######################################

# 6. Teljes képernyő nagyítás

######################################

Feature: Teljes képernyőre nagyítás
Mint felhasználó
Azért, hogy jobban belemerülhessek a játékba
Szeretném teljes képernyőn futtatni a játékot

Background:
Given a játék elindult

Scenario: Teljes képernyő mód aktiválása
When a felhasználó a "Teljes képernyő" gombra kattint
Then a játék teljes képernyős módba vált

Scenario: Kilépés teljes képernyő módból
When a felhasználó ismét a "Teljes képernyő" gombra kattint
Then a játék visszavált normál nézetre

@prioritas:Kozepes
@szerzo:Mark

---

######################################

# 7. Kedvenc játékaim fül

######################################

Feature: Kedvenc játékaim fül
Mint regisztrált felhasználó
Azért, hogy gyorsan elérjem a kedvenc játékaimat
Szeretném, ha lenne egy "Kedvenc játékaim" fül az oldalon

Background:
Given a felhasználó bejelentkezett

Scenario: Játék hozzáadása a kedvencekhez
When a felhasználó a játék melletti kedvenc gombra kattint
Then a játék megjelenik a "Kedvenc játékaim" fülön

Scenario: Kedvenc törlése
When a felhasználó eltávolítja a játékot a listából
Then az már nem látható a kedvencek között

Scenario: Csak bejelentkezett felhasználó láthatja
When a látogató nincs bejelentkezve
Then a "Kedvenc játékaim" fül nem elérhető

@prioritas:Kozepes
@szerzo:Nori

---

######################################

# 8. Friends

######################################

Feature: Friends (Barátok)
Mint felhasználó
Azért, hogy közösen tudjunk játszani és versenyezni
Szeretném, ha barátokat tudnék hozzáadni és látni őket

Background:
Given a felhasználó bejelentkezett

Scenario: Barát hozzáadása
When a felhasználó megad egy érvényes e-mail címet
Then az új barát megjelenik a barátlistában

Scenario: Barát törlése
When a felhasználó törli a barátot
Then a barát eltűnik a listából

Scenario: Barát státusz megjelenítése
Then minden barát mellett látszik, hogy online vagy offline

@prioritas:Kozepes
@szerzo:Peti

---

######################################

# 9. Keresőmező kiemelése

######################################

Feature: Keresőmező kiemelése
Mint látogató
Azért, hogy könnyen megtaláljam a keresési lehetőséget
Szeretném, ha a keresőmező kiemelkedne vizuálisan

Background:
Given a weboldal betöltődött

Scenario: A keresőmező megjelenik a fejlécben
Then a keresőmező jól látható helyen található

Scenario: A keresőmező kiemelése fókusz esetén
When a felhasználó a keresőmezőbe kattint
Then a keresőmező színe vagy szegélye megváltozik

Scenario: Keresőmező mobilnézetben is látható
When a felhasználó mobil eszközről nyitja meg az oldalt
Then a keresőmező elérhető és jól látható marad

@prioritas:Kozepes
@szerzo:Lilla

---

######################################

# 10. Kommentelési lehetőség

######################################

Feature: Kommentelési lehetőség
Mint regisztrált felhasználó
Azért, hogy megoszthassam a véleményem
Szeretnék kommentelni a játékokhoz

Background:
Given a felhasználó bejelentkezett

Scenario: Komment írása
When a felhasználó beír egy szöveget és elküldi
Then a komment megjelenik a játék alatti listában

Scenario: Komment üresen nem küldhető
When a felhasználó üresen küldi el a mezőt
Then hibaüzenetet kap, hogy töltse ki

Scenario: Kommentek listázása dátum szerint
Then a kommentek a legújabbtól a legrégebbi felé rendeződnek

@prioritas:Kozepes
@szerzo:Kristof

---

######################################

# 11. Görgetés közbeni menü

######################################

Feature: Görgetés közbeni menü
Mint látogató
Azért, hogy könnyen navigáljak
Szeretném, ha a menü görgetés közben is látható maradna

Background:
Given a weboldal betöltődött

Scenario: Menü rögzítése az oldal tetején
Then a menü fix pozícióban marad görgetés közben

Scenario: Menü nem takarja ki a tartalmat
Then a fő tartalom a menü alatt jelenik meg

Scenario: Menü mobilon összecsukódik
When a felhasználó lefelé görget
Then a menü automatikusan összecsukódik

@prioritas:Magas
@szerzo:Kata

---

######################################

# 12. Vissza az elejére gomb

######################################

Feature: Vissza az elejére gomb
Mint látogató
Azért, hogy gyorsan visszatérhessek az oldal tetejére
Szeretném, ha lenne egy "Vissza az elejére" gomb

Background:
Given a weboldal betöltődött

Scenario: A gomb megjelenítése
When a felhasználó legörget az oldal aljára
Then megjelenik a "Vissza az elejére" gomb

Scenario: A gomb funkciója
When a felhasználó a gombra kattint
Then az oldal visszagördül a tetejére

@prioritas:Kozepes
@szerzo:Tamas

---

######################################

# 13. Refaktoriálás

######################################

Feature: Refaktorálás
Mint fejlesztő
Azért, hogy a kód olvashatóbb és hatékonyabb legyen
Szeretném refaktorálni az alkalmazás bizonyos részeit

Background:
Given a működő kódbázis

Scenario: Ismétlődő kód eltávolítása
When a fejlesztő átszervezi a kódot
Then az ismétlődő részek megszűnnek

Scenario: Funkciók változatlanul működnek
Then a tesztek sikeresen lefutnak refaktorálás után

@prioritas:Magas
@szerzo:Gergő

---

######################################

# 14. Játékban scoreboard

######################################

Feature: Játékban Scoreboard
Mint játékos
Azért, hogy lássam a pontszámomat és a fejlődésemet
Szeretném, ha a játék közben megjelenne egy scoreboard

Background:
Given a játék elindult

Scenario: Pontszám megjelenítése
Then a scoreboard mutatja az aktuális pontszámot

Scenario: Pontszám frissítése
When a játékos pontot szerez
Then a scoreboard értéke azonnal frissül

Scenario: Pontszám rögzítése a játék végén
When a játék véget ér
Then a scoreboard pontszám mentésre kerül

@prioritas:Magas
@szerzo:Ádám

---

######################################

# 15. Beállítások

######################################

Feature: Beállítások
Mint felhasználó
Azért, hogy személyre szabjam a játékélményt
Szeretném, ha a játékban különböző beállításokat módosíthatnék

Background:
Given a játék elindult

Scenario: Beállítások módosítása
When a felhasználó módosítja a hangerőt vagy nyelvet
Then a változtatás azonnal érvénybe lép

Scenario: Beállítások mentése
Then a rendszer elmenti a beállításokat localStorage-be

Scenario: Alapértelmezett visszaállítása
When a felhasználó a "Visszaállítás" gombra kattint
Then a beállítások alapértékre állnak vissza

@prioritas:Magas
@szerzo:Dóra

---

######################################

# 16. Profil

######################################

Feature: Profil
Mint regisztrált felhasználó
Azért, hogy kezeljem a saját adataimat
Szeretném megtekinteni és szerkeszteni a profilomat

Background:
Given a felhasználó bejelentkezett

Scenario: Profil megtekintése
Then a profil oldalon megjelenik a név, email és profilkép

Scenario: Profil szerkesztése
When a felhasználó módosítja a nevét és elmenti
Then a változás megjelenik a profil oldalon

@prioritas:Kozepes
@szerzo:Réka

---

######################################

# 17 Játékról leírás

######################################

Feature: Játékról leírás
Mint látogató
Azért, hogy megértsem a játék célját
Szeretném elolvasni a játék rövid leírását

Background:
Given a játék oldala megnyílt

Scenario: Leírás megjelenítése
Then a játék alatt megjelenik egy rövid ismertető szöveg

Scenario: Leírás formázása
Then a leírás jól olvasható formázással jelenik meg

@prioritas:Alacsony
@szerzo:Bence

---

######################################

# 18. Kezdőlap

######################################

Feature: Kezdőlap
Mint látogató
Azért, hogy megismerjem az oldalt
Szeretném, ha a kezdőlapon bemutatásra kerülne a fő tartalom

Background:
Given a weboldal betöltődött

Scenario: Kezdőlap tartalma
Then a kezdőlapon megjelenik a bemutató szöveg és képek

Scenario: Navigáció a fő funkciókhoz
Then a felhasználó a kezdőlapról elérheti a játékot, kapcsolatot és bejelentkezést

@prioritas:Magas
@szerzo:Anna

---

######################################

# 19. Kapcsolat oldal

######################################

Feature: Kapcsolat oldal
Mint felhasználó
Azért, hogy kapcsolatba léphessek az üzemeltetőkkel
Szeretném, ha lenne egy kapcsolat oldal, ahol üzenetet küldhetek

Background:
Given a weboldal betöltődött

Scenario: Űrlap megjelenítése
Then az oldal tartalmaz egy nevet, emailt és üzenetmezőt

Scenario: Adatellenőrzés
When a felhasználó hibás email formátumot ad meg
Then hibaüzenetet kap, hogy érvénytelen az email cím

Scenario: Sikeres beküldés

---

######################################

# 20. Játék

######################################

Feature: Játék
Mint játékos
Azért, hogy szórakozzak és pontokat szerezzek
Szeretném elindítani a játékot a weboldalon

Background:
Given a játék oldal betöltődött

Scenario: Játék elindítása
When a felhasználó a "Játék indítása" gombra kattint
Then a játék elindul és láthatóvá válik

Scenario: Játék futása
Then a játékban mozgó elemek és pontgyűjtés működnek hibamentesen

@prioritas:Magas
@szerzo:Gergő

---

######################################

# 21. Játék menü

######################################

Feature: Játék menü
Mint játékos
Azért, hogy irányíthassam a játékot közben
Szeretném, ha lenne egy játék menü szünet, újrakezdés és kilépés opcióval

Background:
Given a játék elindult

Scenario: Menü megnyitása
When a felhasználó a menü gombra kattint
Then a játék megáll és a menü megjelenik

Scenario: Játék folytatása
When a felhasználó a "Folytatás" gombra kattint
Then a játék onnan folytatódik, ahol abbahagyta

Scenario: Játék újraindítása
When a felhasználó az "Újrakezdés" gombot választja
Then a játék újrakezdődik alaphelyzetről

@prioritas:Magas
@szerzo:Nóri

---

######################################

# 22. Játékban mozgás

######################################

Feature: Játékban mozgás
Mint játékos
Azért, hogy irányíthassam a karaktert
Szeretném, ha a karakterem mozogna a játékban

Background:
Given a játék elindult

Scenario: Karakter irányítása
When a felhasználó megnyomja a mozgásra szolgáló billentyűt
Then a karakter elmozdul az adott irányba

Scenario: Mozgás folyamatos frissítése
Then a karakter mozgása valós időben frissül

Scenario: Ütközés kezelése
When a karakter akadályba ütközik
Then a játék reagál (pl. pontlevonás, életerő csökkenés)

@prioritas:Magas
@szerzo:Márk

---

######################################

# 23. Játékban kamera

######################################

Feature: Játékban kamera
Mint játékos
Azért, hogy mindig lássam a karakterem mozgását
Szeretném, ha a kamera automatikusan követné őt

Background:
Given egy játék folyamatban van

Scenario: Kamera követi a karaktert
When a karakter elmozdul a pályán
Then a kamera középpontja a karakter pozíciójára igazodik

Scenario: Kamera mozgása sima
Then a kamera mozgása animáltan, rángatás nélkül történik

Scenario: Fix nézet váltása
When a felhasználó bekapcsolja a fix kameranézetet
Then a kamera pozíciója nem követi tovább a karaktert

@prioritas:Kozepes
@szerzo:Dóra

---

######################################

# 24. Játék modellek

######################################

Feature: Játék modellek
Mint játékos
Azért, hogy vizuálisan élvezetes legyen a játék
Szeretném, ha a játék 3D modelleket tartalmazna

Background:
Given a játék betöltése folyamatban van

Scenario: Modellek betöltése
Then a 3D modellek betöltődnek a jelenetbe

Scenario: Textúrák megjelenítése
Then minden modell megfelelő textúrával jelenik meg

Scenario: Optimalizált teljesítmény
Then a játék nem akad a modellek betöltése közben

@prioritas:Kozepes
@szerzo:Bálint

---

######################################

# 25. Játék manager

######################################

Feature: Játék Manager
Mint fejlesztő
Azért, hogy kezeljem a játék állapotait
Szeretnék egy központi Játék Manager modult

Background:
Given a játék modulként betöltődött

Scenario: Játék indítása
When a felhasználó új játékot indít
Then a Játék Manager inicializálja a szükséges komponenseket

Scenario: Játék szüneteltetése
When a játékos a "Szünet" menüpontra kattint
Then a Játék Manager leállítja a játék frissítését

Scenario: Játék vége kezelése
When a játék befejeződik
Then a Játék Manager értesíti a scoreboardot és naplózza az eredményt

@prioritas:Magas
@szerzo:Kristóf

---

######################################

# 26. Játék hangja

######################################

Feature: Játék hangja
Mint játékos
Azért, hogy élvezetesebb legyen a játék
Szeretném, ha hanghatások és háttérzene lennének

Background:
Given a játék elindult

Scenario: Hanghatások eseményekhez
When a karakter pontot szerez vagy akadályba ütközik
Then megfelelő hanghatás lejátszásra kerül

Scenario: Háttérzene lejátszása
Then a játék alatt halk háttérzene szól

Scenario: Hang kikapcsolása
When a felhasználó a beállításokban kikapcsolja a hangot
Then sem hanghatás, sem zene nem hallható

@prioritas:Kozepes
@szerzo:Eszter

---

######################################

# 27. Játékban tesztek

######################################

Feature: Játékban tesztek
Mint fejlesztő
Azért, hogy a játék stabil és hibamentes maradjon
Szeretnék automatizált teszteket a játék funkcióira

Background:
Given egy tesztkörnyezet előkészítve

Scenario: Egységtesztek lefuttatása
When a fejlesztő elindítja a teszteket
Then minden logikai teszt sikeresen lefut

Scenario: Integrációs tesztek
Then a fő modulok (kamera, manager, scoreboard) integrációs tesztjei sikeresek

@prioritas:Magas
@szerzo:Gergő

---

######################################

# 28. Unity CarGame integráció

######################################

Feature: Unity CarGame integráció
Mint játékos
Azért, hogy böngészőben játszhassak a CarGame-mel
Szeretném, ha a Unity játék beágyazva lenne a weboldalba

Background:
Given a weboldal betöltődött

Scenario: Unity játék betöltése
When a felhasználó a CarGame oldalra navigál
Then a Unity WebGL build betöltődik a böngészőben

Scenario: Játék vezérlése
When a játékos a billentyűzettel vagy egérrel irányít
Then a CarGame megfelelően reagál az inputokra

Scenario: Teljes képernyő mód
When a felhasználó a teljes képernyő gombra kattint
Then a játék teljes képernyős módba vált

Scenario: Betöltési képernyő
Then betöltés közben megjelenik a Unity loading bar

@prioritas:Magas
@szerzo:Team

---

######################################

# 29. Projekt struktúra átrendezés

######################################

Feature: Projekt struktúra átrendezés
Mint fejlesztő
Azért, hogy a kód tisztább és karbantarthatóbb legyen
Szeretném átrendezni a projekt mappáit

Background:
Given a projekt mappák átrendezésre kerültek

Scenario: Backend és frontend szétválasztása
Then a backend/ mappa tartalmazza az app.py-t és az instance/-t
And a frontend/ mappa tartalmazza a templates/ és static/ mappákat

Scenario: Játékok külön mappába
Then a jatekok/ mappa tartalmazza a cargame_unity/ Unity projektet
And a frontend/WebCarGame/ tartalmazza a WebGL build-et

Scenario: Dokumentáció a gyökérben
Then kovspec.md, user_storyk.md, meeting.md és README.md a gyökérben van

Scenario: Útvonalak frissítése
Then az app.py helyesen hivatkozik a frontend mappákra
And az adatbázis útvonal backend/instance/users.db

@prioritas:Magas
@szerzo:Team

---

######################################

# 30. Téma rendszer továbbfejlesztése

######################################

Feature: Téma rendszer továbbfejlesztése
Mint felhasználó
Azért, hogy személyre szabhassam a megjelenést
Szeretném kiválasztani és menteni a kedvenc témámat

Background:
Given a felhasználó bejelentkezett

Scenario: 3 téma közül választás
When a felhasználó a beállításokban választ
Then a colored, dark vagy light téma aktiválódik

Scenario: Animációk ki/bekapcsolása
When a felhasználó kikapcsolja az animációkat
Then az oldal statikus marad, nincs animated-bg

Scenario: Beállítás perzisztencia
When a felhasználó kijelentkezik és újra bejelentkezik
Then a korábban választott téma és animáció beállítások megmaradnak

@prioritas:Kozepes
@szerzo:Patrik

---
