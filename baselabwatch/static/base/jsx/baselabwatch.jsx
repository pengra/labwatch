const leftNavBarLinks = [
  "School", "Students", "Profile"
]

class MainContent extends LabWatchWebsite {
  constructor() {
    super();

    this.renderSchoolPage = this.renderSchoolPage.bind(this);
    this.renderStudentsPage = this.renderStudentsPage.bind(this);
    this.renderProfilePage = this.renderProfilePage.bind(this);
  }
  renderSchoolPage() {
    const example = [
      ["Settings", <div>content</div>],
      ["Limits", <div>morecontent</div>],
      ["Payment", <div>morecontent2</div>],
    ];
    return (<div>
      <TabbedPage tabs={example} />
    </div>)
  }
  renderStudentsPage() {
    const example = [
      ["Create", <div>content</div>],
      ["Find/Edit", <div>morecontent</div>],
      ["Upload", <div>morecontent2</div>],
    ];
    return (<div>
      <TabbedPage tabs={example} />
    </div>)
  }
  renderProfilePage() {
    return (<div>
      <h1>Edit your Profile</h1>
    </div>)
  }
  renderMainPage() {
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