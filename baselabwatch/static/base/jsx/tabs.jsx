
class TabbedPage extends React.Component {
  // props:
    // tabs : [[title, content], ...]
  constructor() {
    super();
    this.state = {
      activeTab: 0
    }
    this.handleTabClick = this.handleTabClick.bind(this);
  }
  handleTabClick(id) {
    this.setState({
      activeTab: id
    })
  }
  render() {
    return (
      <div>
        <TabNavBar 
          tabs={this.props.tabs.map((item) => item[0])} 
          activeTab={this.state.activeTab}
          handleTabClick={this.handleTabClick}
        />
        <TabContentArea 
          tabs={this.props.tabs.map((item) => item[1])} 
          activeTab={this.state.activeTab}
        />
      </div>
    )
  }
}

class TabNavBar extends React.Component {
  // props:
    // tabs : [title, ...]
    // activeTab : active tab
    // handleClick : parent tab handling
  render() {
    let tabHeaders = this.props.tabs.map((tabContent, index) => <TabButton 
      id={index} title={tabContent} active={this.props.activeTab === index}
      key={index} handleTabClick={this.props.handleTabClick}
    />)
    return (
      <ul className="nav nav-tabs" role="tablist">
        {tabHeaders}
      </ul>
    )
  }
}

class TabButton extends React.Component {
  // props:
    // id: tab id
    // title: tab title
    // active: is this tab active?
    // handleTabClick : what to do on click
  render() {
    const tabId = "tab-" + this.props.id;
    const hrefClass = this.props.active ? 'nav-link active' : 'nav-link';
    return (
      <li className="nav-item">
        <a 
          className={hrefClass} 
          id={tabId} 
          role="tab" 
          aria-controls={tabId}
          aria-expanded={() => {this.props.active.toString()}}
          data-toggle="tab"
          href="#"
          onClick={() => {this.props.handleTabClick(this.props.id)}}
        >{this.props.title}</a>
      </li>
    )
  }
}

class TabContentArea extends React.Component {
  // props:
    // tabs : [content, ...]
    // activeTab : active tab
  render() {
    return (
      <div className="tab-content">
        {this.props.tabs.map((item, index) => 
          <TabContent content={item} activeTab={this.props.activeTab} id={index} key={index}/>
        )}
      </div>
    )
  }
}

class TabContent extends React.Component {
  // props:
    // content : actual content of tab
    // id : tab id
    // activeTab : active tab
  render() {
    const tabId = "tab-" + this.props.id;
    const divClass = this.props.activeTab === this.props.id ? "tab-pane fade show active" : "tab-pane fade"
    return (
      <div className={divClass}>
        {this.props.content}
      </div>
    )
  }
}