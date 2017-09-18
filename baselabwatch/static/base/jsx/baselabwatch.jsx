const leftNavBarLinks = [
    "School", "Students", "Profile"
]

class MainContent extends LabWatchWebsite {
  renderMainPage() {
    return (<div><h1>Here we go! {this.state.currentPage}</h1></div>)
  }
}