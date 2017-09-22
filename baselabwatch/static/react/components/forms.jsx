
class Form extends React.Component {
  // props:
    // url : url to OPTIONS/GET to find form contents
    // className : this html class
    // idName : this html id
  constructor() {
    super();
    this.state = {
      formData: {}
    };
  }

  // Overload methods:
  handleSubmit = () => {}
  renderForm = () => {}

  componentDidMount() {
    let method = 'GET';
    $.ajax({
      method: method,
      url: this.props.url
    }).done((data) => this.loadForm(data, method));
    method = 'OPTIONS';
    $.ajax({
      method: method,
      url: this.props.url
    }).done((data) => this.loadForm(data, method));
  }
  loadForm = (data, verb) => {
    let newFormData = this.state.formData;
    if (verb === 'GET') {
      for (let fieldName in data) {
        if (fieldName in newFormData) {
          newFormData[fieldName].value = data[fieldName];
        } else {
          newFormData[fieldName] = {value: data[fieldName]};
        }
      }
    } else if (verb === 'OPTIONS' && data.actions) {
      let acceptedMethod = null;
      if ('PUT' in data.actions) {
        acceptedMethod = 'PUT';
      } else if ('POST' in data.actions) {
        acceptedMethod = 'POST';
      } else {
        throw "Unknown accepted method";
      }
      const fields = data.actions[acceptedMethod]
      for (let fieldName in fields) {
        if (fieldName in newFormData) {
          newFormData[fieldName].options = fields[fieldName];
        } else {
          newFormData[fieldName] = {options: fields[fieldName]};
        }
      }
    }
    this.setState({formData: newFormData});
    console.log(this.state)
    // let newFormData = this.state.formData;
    // if (!(data in newFormData)) {
    //   this.state.formData[name] = {};
    // }
    // let data = this.state.formData[name];
    // data[stateKey] = stateValue;
    // newFormData[name] = data;
    // this.setState({
    //   formData: newFormData
    // });
  }
  render() {
    return (
      <form className={this.props.className || null} id={this.props.idName} onSubmit={this.handleSubmit}>
        {this.renderForm()}
      </form>
    )
  }
}


class VerticalFormGroup extends React.Component {
  // props:
    // optionsData : what OPTIONS[key] returned
    // getData : what GET[key] returned

  render() {
    return (
      <div className="form-group">
        <label htmlFor={this.props.field}>{}</label>
      </div>
    )
  }
}