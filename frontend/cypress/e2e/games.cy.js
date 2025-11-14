describe('Game Categories', () => {
  describe('Akció Category', () => {
    beforeEach(() => {
      cy.visit('/akcio')
    })

    it('should display action games', () => {
      cy.get('h1').contains('Akció Játékok').should('be.visible')
      cy.contains('Shadow Strike').should('be.visible')
      cy.contains('Cyber Warriors').should('be.visible')
      cy.contains('Dragon Assault').should('be.visible')
    })

    it('should display game cards with descriptions', () => {
      cy.get('.card').should('have.length.at.least', 3)
      cy.contains('Légy a végső harcos').should('be.visible')
    })

    it('should have play buttons on game cards', () => {
      cy.get('.btn').filter(':contains("Játék")').should('have.length.at.least', 3)
    })
  })

  describe('Logikai Category', () => {
    beforeEach(() => {
      cy.visit('/logikai')
    })

    it('should display puzzle games', () => {
      cy.get('h1').contains('Logikai Játékok').should('be.visible')
      cy.contains('Puzzle Master').should('be.visible')
    })
  })

  describe('Verseny Category', () => {
    beforeEach(() => {
      cy.visit('/verseny')
    })

    it('should display racing games', () => {
      cy.get('h1').contains('Verseny Játékok').should('be.visible')
      cy.contains('Speed Racer').should('be.visible')
    })
  })

  describe('Sport Category', () => {
    beforeEach(() => {
      cy.visit('/sport')
    })

    it('should display sports games', () => {
      cy.get('h1').contains('Sport Játékok').should('be.visible')
      cy.contains('Football Pro').should('be.visible')
    })
  })

  describe('Retro Category', () => {
    beforeEach(() => {
      cy.visit('/retro')
    })

    it('should display retro games', () => {
      cy.get('h1').contains('Retro Játékok').should('be.visible')
      cy.contains('Pac-Man Reborn').should('be.visible')
    })
  })
})
