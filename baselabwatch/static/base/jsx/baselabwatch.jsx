const leftNavBarLinks = [
    "School", "Students", "Profile"
]

class MainContent extends LabWatchWebsite {
  constructor() {
    super();

    this.renderSchoolPage = this.renderSchoolPage.bind(this);
  }
  renderSchoolPage() {
    const example = [
      ["Settings", <div>content</div>],
      ["Limits", <div>morecontent</div>],
      ["Payment", <div>morecontent2</div>],
    ];
    return (<div>
      <TabbedPage tabs={example}/>
    </div>)
  }
  renderMainPage() {
    if (this.state.currentPage === 0) {
      return this.renderSchoolPage();
    } else {
      return (<h1>Something went wrong...</h1>)
    }
  }
}