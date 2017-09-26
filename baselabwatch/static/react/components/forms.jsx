class Form extends React.Component {
  // props:
  // url : url to OPTIONS/GET to find form contents
  // className : this html class
  // id : this html id
  // overrideSuccess : new success method
  // overrideFail : new fail method
  constructor() {
    super();
    this.state = {
      formData: {},
      errors: {}
    };
  }

  // Overload methods:
  renderForm = () => { }
  onSubmitSuccess = (data) => {
    if (this.props.overrideSuccess) {
      this.props.overrideSuccess(data);
    }

    this.setState({
      success: true,
      errors: {}
    })
    setTimeout(() => {
      this.setState({
        success: false
      });
    }, 3000)
    if (this.state.method === 'POST') {
      this.clearForm();
    }
  }

  onSubmitFail = (data) => {
    if (this.props.overrideSuccess) {
      this.props.overrideFail(data);
    }
    this.setState({
      errors: data.responseJSON
    })
    this.setState({
      fail: true
    })
  }

  clearForm = () => {
    for (let fieldName in this.state.formData) {
      this.updateFormDataState(fieldName, "value", "");
    }

  }
  onChange = (event) => {
    this.updateFormDataState(event.target.name, "value", event.target.value);
  }
  handleSubmit = (event) => {
    event.preventDefault();
    $.ajax({
      method: this.state.method,
      url: this.props.url,
      data: this.serializeForm()
    })
      .done((data) => {
        this.onSubmitSuccess(data);
      })
      .fail((data) => {
        this.onSubmitFail(data);
      });
  }
  serializeForm = () => {
    let formContents = {};
    Object.keys(this.state.formData).map((k, i) => {
      formContents[k] = this.state.formData[k].value
    })
    return formContents;
  }
  updateFormDataState(field, key, value) {
    let newFormData = this.state.formData;
    let data = this.state.formData[field];
    data[key] = value;
    newFormData[field] = data;
    this.setState({
      formData: newFormData
    });
  }
  componentDidMount() {
    $.ajax({
      method: 'GET',
      url: this.props.url
    }).done((data) => this.loadForm(data, 'GET'));
    $.ajax({
      method: 'OPTIONS',
      url: this.props.url
    }).done((data) => this.loadForm(data, 'OPTIONS'));
  }
  loadForm = (data, verb) => {
    let newFormData = this.state.formData;
    if (verb === 'GET') {
      for (let fieldName in data) {
        if (isNaN(fieldName)) { // to protect against list views
          if (fieldName in newFormData) {
            newFormData[fieldName].value = data[fieldName];
          } else {
            newFormData[fieldName] = { value: data[fieldName] };
          }
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
      this.setState({ method: acceptedMethod })
      const fields = data.actions[acceptedMethod]
      for (let fieldName in fields) {
        if (fieldName in newFormData) {
          newFormData[fieldName].options = fields[fieldName];
        } else {
          newFormData[fieldName] = { options: fields[fieldName] };
        }
      }
    }
    this.setState({ formData: newFormData });
  }
  render() {
    let formRender = null;
    const formData = this.state.formData;
    let proceed = true;
    const length = Object.keys(formData).length;
    Object.keys(formData).map((k, i) => { if (isNaN(k)) { proceed = ("options" in formData[k] && proceed) } })

    if (proceed && length > 0) {
      formRender = this.renderForm();
    }

    return (
      <form id={this.props.id} className={this.props.className || null} id={this.props.idName} onSubmit={this.handleSubmit}>
        {formRender}
      </form>
    )
  }
}

class SubmitInput extends React.Component {
  // props:
  // label: what to display on button
  // success : true/false success?
  // fail : true/false fail?
  // modal : true/false
  // if modal:
  // onSubmit : method for submission
  render() {
    let feedback = null;
    const modalClassName = this.props.modal ? ' is-modal' : '';
    if (this.props.success) {
      feedback = (
        <span className={"ajax-notification text-success" + modalClassName}>
          <i className="fa fa-check" aria-hidden="true"></i> Updated
        </span>
      )
    } else if (this.props.fail) {
      feedback = (
        <span className={"ajax-notification text-danger" + modalClassName}>
          <i className="fa fa-times" aria-hidden="true"></i> Failed. Try Again
        </span>
      )
    }
    if (!this.props.modal) {
      return (
        <div>
          <input type="submit" value={this.props.label} className="btn btn-success" />
          {feedback}
        </div>
      )
    } else {
      return (
        <div>
          {feedback}
          <button type="button" className="btn btn-primary" onClick={this.props.onSubmit}>{this.props.label}</button>
        </div>
      )
    }
  }
}

class HiddenInput extends React.Component {
  // props:
  // formData : what formData[key] in Form.state.formData
  // name : field name
  render() {
    const valueLoaded = !!("value" in this.props.formData)

    // defaults
    let value;

    if (valueLoaded) {
      value = this.props.formData.value || "";
    } else {
      value = "";
    }

    <input
      type="hidden"
      name={this.props.name}
      value={value}
    />
  }
}

class SelectInput extends React.Component {
  // props:
  // formData : what formData[key] in Form.state.formData
  // name : field name
  // moreClasses : more classes
  // errors: if there are errors to display
  render() {
    const optionsLoaded = !!("options" in this.props.formData)
    const valueLoaded = !!("value" in this.props.formData)

    // defaults
    let className = "form-control" + (this.props.errors ? " is-invalid" : "");
    let label;
    let helptext;
    let readOnly;
    let options;

    if (optionsLoaded) {
      label = this.props.formData.options.react_meta.label || this.props.formData.options.label;
      helptext = this.props.formData.options.react_meta.help_text || null;
      readOnly = this.props.formData.options.react_meta.read_only || false;
      options = this.props.formData.options.choices.map(
        (value) => <option value={value.value} key={value.value}>{value.display_name}</option>
      )
    } else {
      label = null;
      helptext = null;
      readOnly = false;
      options = null;
    }

    return (
      <div className="form-group">
        <label htmlFor={this.props.name}>{label}</label>
        <select
          readOnly={readOnly}
          onChange={readOnly ? null : this.props.onChange}
          name={this.props.name}
          className={className}
        >
          {options}
        </select>
        <small className="form-text text-muted">{helptext}</small>
        <div className="invalid-feedback">
          {this.props.errors}
        </div>
      </div>
    );
  }
}

class FileInput extends React.Component {
  // note: since no serializer actually uses
  // a file input, this isn't designed to work with one
  constructor() {
    super();
    this.state = {
      fileName: "Select an XML file",
      file: null,
    }
  }
  formChanged = () => {
    const file = $('#fileUploadInput')[0].files[0];
    this.setState({
      fileName: file.name,
      file: file,
    })
  }

  render() {
    return (
      <div className="input-group">
        <label className="input-group-btn">
          <span className="btn btn-primary" style={{height: '100%'}}>
            Browse&hellip; 
            <input type="file" id="fileUploadInput" style={{display: 'none'}}
              onChange={() => this.formChanged()} name="spreadsheet"
            />
          </span>
        </label>
        <input type="text" value={this.state.fileName} className="form-control" style={{height: '100%'}} readOnly={true} />
        <div className="invalid-feedback">
          {this.props.errors}
        </div>
      </div>
    )
  }
}

class TextInput extends React.Component {
  // props:
  // formData : what formData[key] in Form.state.formData
  // name : field name
  // moreClasses : more classes
  // errors: if there are errors to display

  render() {
    const optionsLoaded = !!("options" in this.props.formData)
    const valueLoaded = !!("value" in this.props.formData)

    // defaults
    let type;
    let placeholder;
    let className = "form-control" + (this.props.errors ? " is-invalid" : "");
    let value;
    let label;
    let helptext;
    let readOnly;

    if (optionsLoaded) {
      type = this.props.formData.options.type;
      placeholder = this.props.formData.options.react_meta.placeholder || null;
      label = this.props.formData.options.react_meta.label || this.props.formData.options.label;
      helptext = this.props.formData.options.react_meta.help_text || null;
      readOnly = this.props.formData.options.react_meta.read_only || false;
    } else {
      type = "text";
      placeholder = null;
      label = null;
      helptext = null;
      readOnly = false;
    }

    if (valueLoaded) {
      value = this.props.formData.value || "";
    } else {
      value = "";
    }

    return (
      <div className="form-group">
        <label htmlFor={this.props.name}>{label}</label>
        <input
          readOnly={readOnly}
          onChange={readOnly ? null : this.props.onChange}
          type={type}
          name={this.props.name}
          className={className}
          placeholder={placeholder}
          value={value}
        />
        <small className="form-text text-muted">{helptext}</small>
        <div className="invalid-feedback">
          {this.props.errors}
        </div>
      </div>
    )
  }
}