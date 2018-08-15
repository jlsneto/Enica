import React, { Component } from "react";
import PropTypes from "prop-types";
class Form extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired
  };
  state = {
    descricao: "",
    is_despesa: ""
  };
  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };
  handleSubmit = e => {
    e.preventDefault();
    const { descricao, is_despesa } = this.state;
    const categoria = { descricao, is_despesa }
    console.log(categoria);
    const conf = {
      method: "post",
      body: JSON.stringify(categoria),
      headers: new Headers({ "Content-Type": "application/json" })
    };
    fetch(this.props.endpoint, conf).then(response => console.log(response));
  };
  render() {
    const { descricao, is_despesa} = this.state;
    return (
      <div className="column">
        <form onSubmit={this.handleSubmit}>
          <div className="field">
            <label className="label">Descricao</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="descricao"
                onChange={this.handleChange}
                value={descricao}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">Despesa</label>
            <div className="control">
              <input
                className="checkbox"
                type="checkbox"
                name="is_despesa"
                onChange={this.handleChange}
                value='true'
                required
              />
            </div>
          </div>
          <div className="control">
            <button type="submit" className="button is-info">
              Send message
            </button>
          </div>
        </form>
      </div>
    );
  }
}
export default Form;