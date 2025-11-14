describe('Register Page', () => {
  beforeEach(() => {
    cy.visit('/register')
  })

  it('should display the registration form', () => {
    cy.get('h2').contains('Regisztráció').should('be.visible')
    cy.get('input[name="name"]').should('be.visible')
    cy.get('input[name="email"]').should('be.visible')
    cy.get('input[name="username"]').should('be.visible')
    cy.get('input[name="password"]').should('be.visible')
    cy.get('button[type="submit"]').should('be.visible')
  })

  it('should show error with empty fields', () => {
    cy.get('button[type="submit"]').click()
    // Check for validation
    cy.get('input[name="username"]:invalid').should('exist')
  })

  it('should allow user to fill all registration fields', () => {
    const timestamp = Date.now()
    const username = `testuser${timestamp}`
    const email = `test${timestamp}@example.com`
    
    cy.get('input[name="name"]')
      .type('Test User')
      .should('have.value', 'Test User')
    
    cy.get('input[name="email"]')
      .type(email)
      .should('have.value', email)
    
    cy.get('input[name="username"]')
      .type(username)
      .should('have.value', username)
    
    cy.get('input[name="password"]')
      .type('TestPass123!')
      .should('have.value', 'TestPass123!')
  })

  it('should have a link to login page', () => {
    cy.get('a').contains('Bejelentkezés').should('be.visible')
  })

  it('should navigate to login page when clicking login link', () => {
    cy.get('a').contains('Bejelentkezés').click()
    cy.url().should('include', '/login')
  })

  it('should validate email format', () => {
    cy.get('input[name="email"]')
      .type('invalidemail')
      .should('have.attr', 'type', 'email')
  })

  it('password fields should be of type password', () => {
    cy.get('input[name="password"]')
      .should('have.attr', 'type', 'password')
  })
})
