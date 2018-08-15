describe("Enica Economize!", () => {
  const categoria = {
    "descricao": "Comida",
      "is_despesa":true
}
  before(() => {
    cy.exec("npm run dev");
  });
  it("should be able to fill a web form", () => {
    cy.visit("/");
    cy
      .get('input[name="descricao"]')
      .type(categoria.descricao)
      .should("have.value", categoria.descricao);
    cy.get('[type="checkbox"]').check([categoria.is_despesa])
      .should("be.checked")
    cy.get("form").submit();
  });
  // more tests here

    // insert after the first "it" block in ./cypress/integration/app_spec.js
  it("should be able to see the table", () => {
    cy.visit("/");
    cy.get("tr").contains(`${categoria.descricao}`);
  });
});