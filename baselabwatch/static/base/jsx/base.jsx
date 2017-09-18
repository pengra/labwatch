class TitleNavBarLink extends React.Component {
  render() {
    return (
      <li className="nav-item">
        <a className="nav-link" href="#">{this.props.text}</a>
      </li>
    )
  }
}

class TitleNavBar extends React.Component {
  render() {
    const links = this.props.links;
    let renderedLinks = Array(links.length);
    for (let i = 0; i < links.length; i++) {
      renderedLinks.push(
        <TitleNavBarLink text={links[i]} key={i} />
      )
    }

    return (
      <ul className="navbar-nav mr-auto" id="title-nav-bar-list">
        {renderedLinks}
      </ul>
    )
  }
}