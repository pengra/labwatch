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
      )
    }

    return (
      <ul className="navbar-nav mr-auto" id="title-nav-bar-list">
        {renderedLinks}
      </ul>
    )
  }
}