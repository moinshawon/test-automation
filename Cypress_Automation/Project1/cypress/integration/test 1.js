/// <reference types = "cypress"/>

it('gogole test', function(){
    cy.visit('https://www.google.com/')
    cy.get('.gLFyf').type('moinshawon{enter}')                      // .means class tag. hit enter by writing: {enter}
    // cy.get('[href="https://github.com/moinshawon"] > .LC20lb').click() // clicking somthing
    cy.contains('Change to English').click()
    cy.wait(4000)
    cy.contains('Videos').click()
});

it('moin er website test', function(){
    cy.visit("https://moinshawon.ml/")
    cy.get('h1').should('include.text', 'MOINUL ISLAM')
})


