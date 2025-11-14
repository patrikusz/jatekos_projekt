describe('Login Page', () => {
  beforeEach(() => {
    cy.visit('/login')
  })

  it('should display the login form', () => {
    cy.get('h2').contains('Bejelentkezés').should('be.visible')
    cy.get('input[name="username"]').should('be.visible')
    cy.get('input[name="password"]').should('be.visible')
    cy.get('button[type="submit"]').should('be.visible')
  })

  it('should show error with empty credentials', () => {
    cy.get('button[type="submit"]').click()
    // Check for validation or error message
    cy.get('input[name="username"]:invalid').should('exist')
  })

  it('should allow user to type username and password', () => {
    cy.get('input[name="username"]')
      .type('testuser')
      .should('have.value', 'testuser')
    
    cy.get('input[name="password"]')
      .type('testpassword')
      .should('have.value', 'testpassword')
  })

  it('should have a link to registration page', () => {
    cy.get('a').contains('Regisztráció').should('be.visible')
  })

  it('should navigate to register page when clicking register link', () => {
    cy.get('a').contains('Regisztráció').click()
    cy.url().should('include', '/register')
  })

  it('should show password field as password type', () => {
    cy.get('input[name="password"]')
      .should('have.attr', 'type', 'password')
  })
})
