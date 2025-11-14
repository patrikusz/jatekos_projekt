describe('Navigation', () => {
  describe('Public Navigation (Not logged in)', () => {
    beforeEach(() => {
      cy.visit('/')
    })

    it('should have working logo link to home', () => {
      cy.visit('/akcio')
      cy.get('.navbar-brand').click()
      cy.url().should('eq', Cypress.config().baseUrl + '/')
    })

    it('should display help link', () => {
      cy.contains('Súgó').should('be.visible')
    })

    it('should navigate to help page', () => {
      cy.get('a').contains('Súgó').click()
      cy.url().should('include', '/help')
    })

    it('should have login button', () => {
      cy.contains('Bejelentkezés').should('be.visible')
    })

    it('should navigate to login page', () => {
      cy.get('a').contains('Bejelentkezés').click()
      cy.url().should('include', '/login')
    })
  })

  describe('Authenticated Navigation', () => {
    beforeEach(() => {
      // Register and login user
      cy.visit('/register')
      const timestamp = Date.now()
      const username = `testuser${timestamp}`
      const email = `test${timestamp}@test.com`
      
      cy.get('input[name="name"]').type('Test User')
      cy.get('input[name="email"]').type(email)
      cy.get('input[name="username"]').type(username)
      cy.get('input[name="password"]').type('testpass123')
      cy.get('button[type="submit"]').click()
      
      // Wait for redirect to home
      cy.url().should('eq', Cypress.config().baseUrl + '/')
      
      // Now login
      cy.visit('/login')
      cy.get('input[name="username"]').type(username)
      cy.get('input[name="password"]').type('testpass123')
      cy.get('button[type="submit"]').click()
      
      // Wait for successful login
      cy.url().should('eq', Cypress.config().baseUrl + '/')
    })

    it('should display user menu when logged in', () => {
      cy.contains('Menü').should('be.visible')
    })

    it('should navigate to settings from dropdown', () => {
      cy.contains('Menü').click()
      cy.contains('Beállítások').click()
      cy.url().should('include', '/beallitasok')
    })

    it('should navigate to friends page from dropdown', () => {
      cy.contains('Menü').click()
      cy.contains('Barátaim').click()
      cy.url().should('include', '/baratok')
    })

    it('should navigate to help page from dropdown', () => {
      cy.contains('Menü').click()
      cy.get('.dropdown-menu').contains('Súgó').click()
      cy.url().should('include', '/help')
    })

    it('should navigate to contact page from dropdown', () => {
      cy.contains('Menü').click()
      cy.contains('Kapcsolat').click()
      cy.url().should('include', '/kapcsolat')
    })

    it('should navigate to FAQ from dropdown', () => {
      cy.contains('Menü').click()
      cy.contains('GYIK').click()
      cy.url().should('include', '/gyik')
    })
  })
})
