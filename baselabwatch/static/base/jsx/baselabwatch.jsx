const leftNavBarLinks = [
  "School", "Students", "Profile"
]

class SchoolAdminForm extends Form {
  // Overload methods:
  renderForm = () => {
    const formData = this.state.formData;
    return (
    <div>
      <TextInput 
        name="name" 
        formData={formData.name} 
        onChange={this.onChange}
        errors={this.state.errors.name}
        key={"name"}
      />
      <div style={{height: 100}}>
        <img src={formData.school_image.value} height="100%"/>
      </div>
      <TextInput 
        name="school_image" 
        formData={formData.school_image} 
        onChange={this.onChange}
        errors={this.state.errors.school_image}
        key={"school_image"}
      />
      <TextInput 
        name="auth_code" 
        formData={formData.auth_code} 
        onChange={this.onChange}
        key={"auth_code"}
      />
      <SubmitInput label="Save" success={this.state.success} fail={this.state.fail}/>
    </div>
    )
  }
}

class LimitsPage extends React.Component {
  constructor() {
    super();
    this.state = {

    }
  }
  componentDidMount = () => {
    $.ajax({
      method: 'GET',
      url: '/base/api/v1/subscriptions/' + subscriptionID + '/',
    })
    .done((data) => {
      this.setState(data)
    })
    .fail((data) => {
    });
  }
  render = () => {
    return (
      <div style={{marginTop: "2%"}}> 
        <div className="row" style={{display: "flex", alignItems: "center", marginTop: "2%"}}>
          <div className="col-2" style={{textAlign: "right"}}>
            <div>
              <strong>Student IDs Available:</strong>
            </div>
          </div>
          <div className="col-10">
            <ProgressBar 
              percentage={100 - ((this.state.current_student_ids * 100) / this.state.max_student_ids)} 
              type="success" 
              content={"" + (this.state.max_student_ids - this.state.current_student_ids) + " IDs Available"}
            />
          </div>
        </div>
        <div className="row" style={{marginTop: "2%"}}>
          <div className="col-3">
            <div className="card text-white bg-success mb-3">
              <div className="card-header">Student Rewards</div>
              <div className="card-body">
                <h4 className="card-title">You're signed up for Student Rewards</h4>
                <p className="card-text">Students will see rewards on logins and at special URLs.</p>
              </div>
            </div>
          </div>
          <div className="col-3">
            <div className="card text-white bg-success mb-3">
              <div className="card-header">Data Intelligence</div>
              <div className="card-body">
                <h4 className="card-title">You're signed up for Data Intelligence</h4>
                <p className="card-text">LabWatch will recomend actions based on historical data.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

class PageContent extends React.Component {
  handleSubmit = (event) => {
   
  }
  render = () => {
    return (
      <main className="tab-content">
        <div className="row">
          <div className="col-12">
            <h2>{this.props.title}</h2>
          </div>
        </div>
        <div className="row">
          <div className="col-12">
            {this.props.content}
          </div>
        </div>
      </main>
    )
  }
}

class MainContent extends LabWatchWebsite {
  renderSchoolPage = () => {
    const schoolPageContent = [
      [
        "Settings", 
        <PageContent title="School Administration" content={<SchoolAdminForm url={"/base/api/v1/schools/" + schoolID + '/'} id="school-admin-form"/>}/>
      ],
      [
        "Limits", 
        <PageContent title="Subscription Administration" content={<LimitsPage />} />
      ],
      [
        "Payment", 
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
        </main>
      ],
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
      <Form url={"/base/api/v1/profiles/" + profileID} />
      <Form url={"/base/api/v1/users/" + userID} />
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