# Cypress Tesztek - Jatekos Projekt

## Áttekintés

Ez a mappa tartalmazza a Jatekos projekt Cypress E2E (end-to-end) tesztjeit.

## Telepítés

```bash
cd frontend
npm install
```

## Tesztek futtatása

### Interaktív módban (Cypress UI):
```bash
npm run cypress:open
```

### Headless módban (CI/CD-hez):
```bash
npm test
# vagy
npm run cypress:run
```

### Headed módban:
```bash
npm run test:headed
```

### Chrome böngészőben:
```bash
npm run test:chrome
```

## Teszt Fájlok

- **home.cy.js** - Főoldal tesztek (navigáció, kategóriák megjelenítése)
- **login.cy.js** - Bejelentkezési oldal tesztek (form validáció, navigáció)
- **register.cy.js** - Regisztrációs oldal tesztek (form mezők, validáció)
- **games.cy.js** - Játék kategóriák és részletek tesztek
- **navigation.cy.js** - Általános navigációs tesztek

## Custom Commands

A `cypress/support/commands.js` fájlban egyéni parancsok találhatók:

- `cy.login(username, password)` - Bejelentkezés
- `cy.register(username, email, password)` - Regisztráció

## Konfiguráció

A Cypress konfiguráció a `cypress.config.js` fájlban található:
- Base URL: http://localhost:5000
- Viewport: 1280x720
- Videó felvétel: engedélyezve
- Screenshot hiba esetén: engedélyezve

## Előfeltételek a tesztek futtatásához

Győződj meg róla, hogy a backend szerver fut a `http://localhost:5000` címen:

```bash
cd backend
python app.py
```

## CI/CD Integráció

A tesztek futtathatók CI/CD pipeline-ban a következő paranccsal:

```bash
npm run cypress:run
```

Ez headless módban futtatja a teszteket és generál videókat és screenshotokat a hibákról.
