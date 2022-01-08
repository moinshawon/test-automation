/// <reference types = "cypress"/>

it('find element and click', function(){
    cy.visit('https://www.google.com/')
    cy.get('.gLFyf').type('moinshawon{enter}')                              // .means class tag. hit enter by writing: {enter}
    // cy.get('[href="https://github.com/moinshawon"] > .LC20lb').click()   // clicking somthing
    cy.contains('Change to English').click()                                // changing language to English
    cy.wait(4000)
    cy.contains('Videos').click()                                           // Clickin the Video tab
});

it('saving value of an element and assert that', function(){
    cy.visit("https://moinshawon.github.io/")
    cy.url().should('include', 'moinshawon')                                // asserting url has that text
    cy.get('h1').should('include.text', 'MOINUL ISLAM')                     // accerting h1 has that text
    cy.get('#part-time > :nth-child(1) > :nth-child(2) > a').should($h => { // saving the text of that element in $h parameter 
        console.log($h.text())                                              // print in the console
        expect($h.text()).to.eq(" Enosis Solutions")                        // assert that $h has valid text
    })
    cy.get('#part-time > :nth-child(1) > :nth-child(2) > a').should('have.text', " Enosis Solutions") // doing prev work differently
    cy.get('#part-time').find('a').first().should('have.text', " Enosis Solutions") // the css selector is bad practice so, i tried to do this
})

it.only('saving value of an element and using it for future work', function(){
    cy.visit("https://mehruzsaif.github.io/Mission-2022/")
    cy.get('.fakibaj').then($lblValue => {
        console.log($lblValue)
        cy.wrap($lblValue).as('fakibazWord')                                // saving the value of that element in fakibazWord variable
    })
    cy.get('@fakibazWord').then(a => {                                      // need to use function bcz cypress execute normal code first then function
        console.log(a.text())                                               // will print the value that was saved in the variable
    })
})


