class LabWatchWebsite extends React.Component {
  // Props:
    // leftLinks: left bar links
  constructor() {
    super();
    this.state = {
      currentPage: 0
    }

    this.handleLeftNavClick = this.handleLeftNavClick.bind(this);
    this.renderMainPage = this.renderMainPage.bind(this);
  }
  handleLeftNavClick(id) {
    this.setState({
      currentPage: id
    })
  }
  renderMainPage() {
    return (<div><h1>Loading Page...</h1></div>)
  }
  render() {
    return (
      <div className="row">
        <nav className="col-sm-3 col-md-2 d-none d-sm-block bg-light sidebar" id="left-nav-bar">
          <LeftNavBar links={this.props.leftLinks} handleClick={this.handleLeftNavClick} />
        </nav>
        <main className="col-sm-9 ml-sm-auto col-md-10 pt-3" role="main" id="main-content-pane">
          {this.renderMainPage()}
        </main>
      </div>
    )
  }
}