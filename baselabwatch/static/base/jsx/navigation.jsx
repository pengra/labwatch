class TitleNavBarLink extends React.Component {
  render() {
    let hrefClass = this.props.active ? "nav-link active" : "nav-link";
    return (
      <li className="nav-item">
        <a className={hrefClass} href={this.props.href}>{this.props.text}</a>
      </li>
    )
  }
}

class TitleNavBar extends React.Component {
  render() {
    const links = this.props.links;
    let renderedLinks = Array(links.length);
    for (let i = 0; i < links.length; i++) {
      const active = links[i].name == this.props.currentApp;
      renderedLinks.push(
        <TitleNavBarLink 
          text={links[i].title} 
          href={links[i].url} 
          active={active}
          key={i} />
      );
    }
    return (
      <ul className="navbar-nav mr-auto" id="title-nav-bar-list">
        {renderedLinks}
      </ul>
    )
  }
}

class LeftNavBarLink extends React.Component {
  constructor() {
    super();
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    return this.props.handleClick(this.props.id);
  }
  render() {
    let hrefClass = this.props.active ? "nav-link active" : "nav-link";
    return (
      <li className="nav-item">
        <a className={hrefClass} onClick={this.handleClick} href="#">{this.props.text}</a>
      </li>
    )
  }
}

class LeftNavBar extends React.Component {
  constructor() {
    super();
    this.state = {
      activeIndex: 0
    }
    this.handleClick = this.handleClick.bind(this);
  }  
  handleClick(id) {
    this.setState({
      activeIndex: id
    });
    this.render();
  }
  render() {
    const links = this.props.links;
    let renderedLinks = Array(links.length);
    for (let i = 0; i < links.length; i++) { 
      const active = i === this.state.activeIndex;
      renderedLinks.push(
        <LeftNavBarLink 
          text={links[i]}
          key={i}
          id={i}
          active={active}
          handleClick={this.handleClick}
          />
      );
    }
    return (
      <ul className="nav nav-pills flex-column" id="left-nav-bar-list">
        {renderedLinks}
      </ul>
    )
  }
}