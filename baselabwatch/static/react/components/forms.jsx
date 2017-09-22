class Form extends React.Component {
  // props:
    // url : url to OPTIONS to find form contents
    // ajax : use ajax?
  // Assumes you're using AJAX for form submission
  constructor() {
    super();

    this.state = {
      form: "loading form...",
      formData: {},
      optionsRetrieved: false,
      getRetrieved: false
    }

    this.ajaxSuccess = this.ajaxSuccess.bind(this);
    this.ajaxFail = this.ajaxFail.bind(this);
    this.ajaxSubmit = this.ajaxSubmit.bind(this);
    this.handleInputUpdate = this.handleInputUpdate.bind(this);
    this.getFormData = this.getFormData.bind(this);
    this.populateForm = this.populateForm.bind(this);
    this.loadForm = this.loadForm.bind(this);
    this.updateFormDataState = this.updateFormDataState.bind(this);
  }
  
  // ajax/form submission
  // OVERLOAD THESE FUNCTIONS
  ajaxSuccess() {}
  ajaxFail() {}
  ajaxSubmit() {}

  // inputUpdate
  handleInputUpdate(name, newValue) {
    this.updateFormDataState(name, "value", newValue);
  }

  // loading form
  componentDidMount() {
    this.getFormData();
  }
  updateFormDataState(name, stateKey, stateValue) {
    if (!(this.state.getRetrieved || this.state.optionsRetrieved)) {
      let newFormData = this.state.formData;
      if (!(data in newFormData)) {
        this.state.formData[name] = {};
      }
      let data = this.state.formData[name];
      data[stateKey] = stateValue;
      newFormData[name] = data;
      this.setState({
        formData: newFormData
      });
    }
  }
  loadForm(formOptions) {
    const thisForm = formOptions.actions;
    let formRender = [];
    if ('PUT' in thisForm) {
      let index = 0;
      for (let key in thisForm.PUT) {
        if (!key.startsWith('_')) {
          this.updateFormDataState(key, "value", null);
          formRender.push(
            <VerticalFormGroup 
              onInputChange={this.handleInputUpdate}
              formData={this.state.formData[key]}
              optionsData={thisForm.PUT[key]}
              id={index}
              key={index}
              name={key}
            />
          )
          index++;
        }
      }
    } else {
      formRender = <div>Form has no PUT method!</div>
    }
    this.setState({
      form: formRender,
      optionsRetrieved: true
    });
  }
  populateForm(formContents) {
    for (let key in formContents) {
      this.updateFormDataState(key, "value", formContents[key]);
    }
    this.setState({
      getRetrieved: true
    })
  }
  getFormData() {
    $.ajax({
      method: 'OPTIONS',
      url: this.props.url
    })
    .done((data) => this.loadForm(data));
    $.ajax({
      method: 'GET',
      url: this.props.url
    })
    .done((data) => this.populateForm(data))
  }

  // rendering
  render() {
    if (this.props.ajax) {
      return (<div className="ajax-form">{this.state.form}</div>);
    } else {
      return (<form>{this.state.form}</form>);
    }
  }
}

// Read:
// https://facebook.github.io/react/docs/forms.html
class VerticalFormGroup extends React.Component {
  // TODO: figure out how to retrieve state from Form as properties
  // Most likely just just have props=seperate components and read from
  // them here directly.

  // props: (left alone since django generation)
    // onInputChange : method to call when something changes
    // formData={this.state.formData[key]}
    // optionsData={thisForm.PUT[key]}
    // id : id of this form group
    // key={index}
    // name={key}
  // optionsData properties:
    // optionsData.type : string representation of one of the inputs defined below
    // optionsData.name : name of form
    // optionsData.required : input required?
    // optionsData.read_only : REMAP TO TO DISABLED
    // optionsData.label : label of this input
    // optionsData.react_data : style/remap properties:
      // optionsData.react_data.label : override current label with this label
      // optionsData.react_data.invalidFeedback : error message if they left it blank
      // optionsData.react_data.hidden : hide form?
      // optionsData.react_data.placeholder : placeholder of content
      // optionsData.react_data.read_only : is it readonly? (if readonly and disabled are true, displays as readonly and is disabled)
      // optionsData.react_data.secondary_label : bottom text below form
      // optionsData.react_data.display : what to display instead of value
  // formData:
    // formData.value : value of content
    // formData.validationLevel : 0 = fail 1 = success 2 = nothing 
  constructor(props) {
    super(props)
    
    const optionsData = this.props.optionsData;
    const reactData = optionsData.react_meta;
    const formData = this.props.formData;
    const formID = "form-group-id-" + this.props.id;
    const hidden = reactData.hidden || false;

    this.otherprops = {
      "divWrapperClass": (hidden ? "hiden" : "form-group"),
      "formGroupID": formID,
      "label": formData.value,
      "type": (hidden ? "hidden" : optionsData.type),
      "inputClass": ("form-control" + (reactData.read_only ? "-plaintext" : "")),
      "disabled": optionsData.read_only,
      "required": optionsData.required,
      "name": optionsData.name,
      "value": (reactData.display || formData.value),
      "validationLevel": (formData.validationLevel || reactData.invalidFeedback || 2),
      "hidden": (reactData.hidden || false),
      "placeholder": (reactData.placeholder || ""),
      "readonly": (reactData.read_only || null),
      "secondaryLabel": (reactData.secondary_label || null),
      "label": reactData.hidden ? null : (reactData.label ? 
        <label htmlFor={formID}>{reactData.label}</label> : 
        <label htmlFor={formID}>{optionsData.label}</label>),
    }
  }
  handleInputChange = (event) => {
    let newValue;
    if (this.otherprops.type === 'checkbox') {
      newValue = event.target.checked;
    } else if (this.otherprops.type === 'text') {
      // TODO: fix this. Can't type
      newValue = event.target.value;
    } else {
      throw "Invalid input type";
    }
    this.otherprops.onInputChange(this.otherprops.name, newValue)
  }
  render = () => {
    return (
      <div className={this.otherprops.divWrapperClass}>
        {this.otherprops.label}
        <input 
          type={this.otherprops.type} 
          className={this.otherprops.inputClass}
          name={this.otherprops.name} 
          id={this.otherprops.formGroupID} 
          placeholder={this.otherprops.placeholder}
          disabled={this.otherprops.disabled}
          readOnly={this.otherprops.readonly}
          value={this.otherprops.value || ""}
          onChange={this.handleInputChange}
        />
        {this.otherprops.secondaryLabel}
      </div>
    )
  }
}
