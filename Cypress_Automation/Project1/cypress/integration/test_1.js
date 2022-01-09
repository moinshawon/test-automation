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
    cy.visit("https://moinshawon.github.io/")                               // default assertion: get req 200
    cy.url().should('include', 'moinshawon')                                // asserting url has that text
    cy.get('h1').should('include.text', 'MOINUL ISLAM')                     // accerting h1 has that text // implicit assertion
    cy.get('#part-time > :nth-child(1) > :nth-child(2) > a').should($h => { // saving the text of that element in $h parameter 
        console.log($h.text())                                              // print in the console
        expect($h.text()).to.eq(" Enosis Solutions")                        // assert that $h has valid text // explicit assertion
    })
    cy.get('#part-time > :nth-child(1) > :nth-child(2) > a').should('have.text', " Enosis Solutions") // doing prev work differently
    cy.get('#part-time').find('a').first().should('have.text', " Enosis Solutions") // the css selector is a bad practice so, i tried to do this
})

it('saving value of an element and using it for future work', function(){
    cy.visit("https://moinshawon.github.io/")
    cy.get('section.bottom-bar > h5').then($lblValue => {
        cy.wrap($lblValue).as('copyrightWord')                                // wrap makes the word an element
    })
    cy.get('@copyrightWord').then(a => {                                      // need to use function bcz cypress execute normal code first then function
        console.log(a.text())                                                 // will print the value that was saved in the variable
    })
})

it('working on multiple elements in cypress', function(){
    const listOfNavItem = [
        "Model S",
        "Model X",
        "Model 3",
        "Roadster",
        "Want to go Mars?"
    ]

    cy.visit("https://moinshawon.ml/tesla-bootstrap/")
    cy.get(".mx-auto").find('li').should('have.length', 5)
    cy.get(".mx-auto").find('li').each((item, index, list) => {               // element, num of list, whole list loop thought 5 times
        // console.log(list)                                                  // print the whole list 5 times as it will loop through
        console.log(item.text())                                              // print single item each in loop
        cy.wrap(item).should('contain.text', listOfNavItem[index])            // assert element contains text 'Model S'
        console.log(index)                                                    // print the idx of the list
        expect(Cypress.$(item).text()).to.eq(listOfNavItem[index])            // assert element's text to eq 'Model S'
    })
})
