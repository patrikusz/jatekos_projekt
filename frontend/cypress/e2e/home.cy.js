describe('Home Page', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should load the home page successfully', () => {
    cy.get('h1').contains('Online Játékok').should('be.visible')
  })

  it('should display the navigation bar', () => {
    cy.get('nav').should('be.visible')
    cy.get('.navbar-brand').should('be.visible')
  })

  it('should display search bar', () => {
    cy.get('input[name="q"]').should('be.visible')
    cy.get('button[type="submit"]').contains('Keresés').should('be.visible')
  })

  it('should display game categories', () => {
    cy.contains('Akció').should('be.visible')
    cy.contains('Logikai').should('be.visible')
    cy.contains('Verseny').should('be.visible')
    cy.contains('Sport').should('be.visible')
    cy.contains('Retro').should('be.visible')
  })

  it('should navigate to a game category when clicked', () => {
    cy.contains('Akció').click()
    cy.url().should('include', '/akcio')
  })
})
