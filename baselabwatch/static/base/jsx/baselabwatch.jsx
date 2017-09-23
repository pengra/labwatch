const leftNavBarLinks = [
  "School", "Students", "Profile"
]

class SchoolAdminForm extends Form {
  // Overload methods:
  handleSubmit = (event) => {}
  onChange = (event) => {
    this.updateFormDataState(event.target.name, "value", event.target.value)
  }
  renderForm = () => {
    const formData = this.state.formData;
    let formRender = ['name'];
    
    for (let field in formRender) {
      const fieldName = formRender[field];
      if (fieldName in formData) {
        formRender[field] = <TextInput 
          name={fieldName} 
          formData={formData[fieldName]} 
          onChange={this.onChange}
          key={field}
        />;
      } else {
        formRender[field] = null;
      }
    }
    
    return (
      <div>
        {formRender}
      </div>
    );
  }
}

class SchoolPageContent extends React.Component {
  handleSubmit = (event) => {

  }
  render = () => {
    return (
      <main className="tab-content">
        <div className="row">
          <div className="col-12">
            <h2>School Administration</h2>
          </div>
        </div>
        <div className="row">
          <div className="col-12">
            <SchoolAdminForm url={"http://127.0.0.1:8000/base/api/v1/schools/" + schoolID}/>
          </div>
        </div>
      </main>
    )
  }
}

class MainContent extends LabWatchWebsite {
  constructor() {
    super();

  }
  renderSchoolPage = () => {
    const schoolPageContent = [
      ["Settings", 
        <SchoolPageContent />
      ],
      ["Limits", 
      <main className="tab-content">
        <div className="row">
          <div className="col-12">
            <h2>Subscription Administration</h2>
          </div>
        </div>
        <div className="row">
          <div className="col-12">
            <Form url={"http://127.0.0.1:8000/base/api/v1/subscriptions/" + subscriptionID} />
          </div>
        </div>
      </main>
      ],
      ["Payment", 
      <main className="tab-content">
        <div className="row tab-header">
          <div className="col-12">
            <h2>Payment <span className="badge badge-success">Free Beta</span></h2>
          </div>
        </div>
        <div className="row">
          <div className="col-12">
            <div className="alert alert-primary">
              <h4 className="alert-heading">Free Beta!</h4>
              LabWatch is currently a free beta. We believe it'd be unfair to charge
              schools for a service that still has bugs. All participating schools are
              granted <strong>unlimited</strong> resources at no cost. Schools will be notified
              ahead of time when the free beta comes to an end. 
            </div>
          </div>
        </div>
      </main>],
    ];
    return (<div>
      <TabbedPage tabs={schoolPageContent} />
    </div>)
  }
  renderStudentsPage = () => {
    const example = [
      ["Create", <div>content</div>],
      ["Find/Edit", <div>morecontent</div>],
      ["Upload", <div>morecontent2</div>],
    ];
    return (<div>
      <TabbedPage tabs={example} />
    </div>)
  }
  renderProfilePage = () => {
    return (<div>
      <h1>Edit your Profile</h1>
      <Form url={"http://127.0.0.1:8000/base/api/v1/profiles/" + profileID} />
      <Form url={"http://127.0.0.1:8000/base/api/v1/users/" + userID} />
    </div>)
  }
  renderMainPage = () => {
    if (this.state.currentPage === 0) {
      return this.renderSchoolPage();
    } else if (this.state.currentPage === 1) {
      return this.renderStudentsPage();
    } else if (this.state.currentPage === 2) {
      return this.renderProfilePage();
    } else {
      return (<h1>This feature is currently under development.</h1>)
    }
  }
}