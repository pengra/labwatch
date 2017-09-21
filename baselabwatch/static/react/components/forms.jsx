class Form extends React.Component {
  // props:
    // url : url to OPTIONS to find form contents
  // Assumes you're using AJAX for form submission
  constructor() {
    super();

    this.state = {
      form: "loading form...",
      formData: []
    }

    this.ajaxSuccess = this.ajaxSuccess.bind(this);
    this.ajaxFail = this.ajaxFail.bind(this);
    this.ajaxSubmit = this.ajaxSubmit.bind(this);
    this.handleInputUpdate = this.handleInputUpdate.bind(this);
    this.getFormData = this.getFormData.bind(this);
    this.loadForm = this.loadForm.bind(this);
  }
  
  // ajax/form submission
  // OVERLOAD THESE FUNCTIONS
  ajaxSuccess() {}
  ajaxFail() {}
  ajaxSubmit() {}

  // inputUpdate
  handleInputUpdate(id, newValue) {
    let newFormData = this.state.formData;
    newFormData[id].value = newValue;
    this.setState({formData: newFormData});
    console.log(newFormData);
  }

  // loading form
  componentDidMount() {
    this.getFormData();
  }
  loadForm(formOptions) {
    const thisForm = formOptions.actions;
    let formRender = [];
    if ('POST' in thisForm) {
      let index = 0;
      for (let key in thisForm.POST) {
        if (!key.startsWith('_')) {
          this.setState({
            formData: [...this.state.formData, {value: null}]
          })
          console.log(thisForm.POST[key])
          formRender.push(
            <VerticalFormGroup 
              type={thisForm.POST[key].type}
              hidden={thisForm.POST[key].react_meta.hidden}
              required={thisForm.POST[key].required}
              disabled={thisForm.POST[key].read_only}
              readOnly={thisForm.POST[key].react_meta.read_only}
              label={thisForm.POST[key].label}
              mutedLabel={thisForm.POST[key].react_meta.secondary_label}
              onInputChange={this.handleInputUpdate}
              value={this.state.formData[index].value}
              id={index}
              key={index}
              name={key}
            />
          )
          index++;
        }
      }
    } else {
      formRender = <div>Form has no POST method!</div>
    }
    this.setState({
      form: formRender
    });
  }
  getFormData() {
    $.ajax({
      method: 'OPTIONS',
      url: this.props.url
    })
    .done((data) => this.loadForm(data));
  }

  // rendering
  render() {
    return (<form>{this.state.form}</form>)
  }
}

// Read:
// https://facebook.github.io/react/docs/forms.html
class VerticalFormGroup extends React.Component {
  // props:
    // type : string representation of one of the inputs defined below
    // label : what is this form?
    // onInputChange : method to call when something changes
    // invalidFeedback : error message if they left it blank
    // id : id of this form group
    // hidden : hide form?
  // Input Specific Props:
    // name : name of form
    // placeholder : placeholder of content
    // type : type of form
      // if type == select: 
        // options: [["human friendly name", value] ... ]
        // value: default value (non human friendly name)
        // multiple: true/false (multiple select?)
    // value : value of content
    // validationLevel : 0 = fail 1 = success 2 = nothing 
    // required?
    // disabled?
    // readonly? (if readonly and disabled are true, displays as readonly and is disabled)
  constructor() {
    super()
    this.handleInputChange = this.handleInputChange.bind(this);
  }
  handleInputChange(event) {
    let newValue;
    if (this.props.type === 'checkbox') {
      newValue = event.target.checked;
    } else {
      throw InputInvalidException(this.props.type);
    }
    this.props.onInputChange(this.props.id, newValue)
  }
  render() {
    const formGroupID = "form-group-id-" + this.props.id;
    const divWrapperClass = this.props.hidden ? "hidden" : "form-group";
    const label = this.props.hidden ? "" : 
      <label htmlFor={formGroupID}>{this.props.label}</label>;
    const inputType = this.props.hidden ? "hidden" : this.props.type;

    let inputClassName = "form-control";

    // figure out disabled vs readonly
    let disabled = false;
    let read_only = false;
    if (this.props.disabled && this.props.readOnly) {
      inputClassName = "form-control-plaintext";
      disabled = true;
    } else if (this.props.disabled) {
      disabled = true;
    } else if (this.props.readOnly) {
      read_only = true
    }

    // secondary label
    let mutedLabel = "";
    if (this.props.mutedLabel) {
      mutedLabel = <small className="text-muted form-text">{this.props.mutedLabel}</small>
    }


    return (
      <div className={divWrapperClass}>
        {label}
        <input 
          type={inputType} 
          className={inputClassName}
          name={this.props.name} 
          id={formGroupID} 
          placeholder={this.props.placeholder}
          disabled={disabled}
          readOnly={read_only}
          value={this.props.value || ""}
          onChange={this.handleInputChange}
        />
        {mutedLabel}
      </div>
    )
  }
}


class _FormGroup extends React.Component {
  // props:
    // type : string representation of one of the inputs defined below
    // label : what is this form?
    // invalidFeedback : error message if they left it blank
  // Input Specific Props:
    // name : name of form
    // placeholder : placeholder of content
    // type : type of form
      // if type == select: 
        // options: [["human friendly name", value] ... ]
        // value: default value (non human friendly name)
        // multiple: true/false (multiple select?)
    // value : value of content
    // validationLevel : 0 = fail 1 = success 2 = nothing 
    // required?
    // disabled?
    // readonly?
  constructor() {
    super();
    this.commonInputBuild = this.commonInputBuild.bind(this);
    this.textInput = this.textInput.bind(this);
    this.selectInput = this.selectInput.bind(this);
  }
  commonInputBuild() {
    // cover text/number/password
    let inputClass = "form-control";
    
    if (this.props.validationLevel === 0) {
      inputClass += " is-invalid";
    } else if (this.props.validationLevel === 1) {
      inputClass += " is-valid";
    }

    return <input 
      className={inputClass}
      type={this.props.type} 
      required={this.props.required}
      disabled={this.props.disabled}
      readOnly={this.props.readonly}
      value={this.props.value}
      placeholder={this.props.placeholder}
    />
  }
  textInput() {
    return commonInputBuild();
  }
  selectInput() {
    const renderChoices = this.props.options.map((item, index) => <option key={index} value={item[1]}>{item[0]}</option>)
    return (
      <select 
        className="form-control" 
        multiple={this.props.multiple}
        required={this.props.required}
        disabled={this.props.disabled}
        readonly={this.props.readonly}
        value={this.props.value}
        name={this.props.name}
      >
        {renderChoices}
      </select>
    )
  }
  textAreaInput() {
    return (
      <textarea 
        className="form-control"
        required={this.props.required || false}
        disabled={this.props.disabled || false}
        readonly={this.props.readonly || false}
        placeholder={this.props.placeholder || ""}
        name={this.props.name}
      >
        {this.props.value || ""}
      </textarea>
    )
  }
  checkboxInput() {
    return (
      <div className="form-check">
        <input 
          type="checkbox" 
          required={this.props.required || false}
          disabled={this.props.disabled || false}
          readonly={this.props.readonly || false}
          placeholder={this.props.placeholder || ""}
          name={this.props.name}
        />
      </div>
    )
  }
  render() {
    return (
      <div className="form-group row">
        <label className="col-sm-2 col-form-label">{this.props.label}</label>
        <div className="col-sm-10">
          {this.commonInputBuild()}
          <div className="invalid-feedback">
            {this.props.invalidFeedback || "Invalid value."}
          </div>
        </div>
      </div>
    )
  }
}