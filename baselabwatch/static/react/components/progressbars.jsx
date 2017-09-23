
class ProgressBar extends React.Component {
  // props:
    // type : (color of bar) success/primary/warning/danger etc
    // percentage : 0-100 of how full it is
    // content : message inside
  render = () => {
    return (
      <div className="progress">
        <div className={"progress-bar bg-" + this.props.type} style={{"width": "" + this.props.percentage + "%", "margin": 0}}>
          {this.props.content}
        </div>
      </div>
    );
  }
}