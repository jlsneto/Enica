import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Form from "./Form";
const App = () => (
  <React.Fragment>
          <Form endpoint="api/categorias/" />
    <DataProvider endpoint="api/categorias/"
                  render={data => <Table data={data} />} />

  </React.Fragment>
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;