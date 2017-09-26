
class Modal extends React.Component {
  // props:
    // id : modal id
    // title : modal title
    // url : form submission url
    // pk : primary key to focus
  constructor() {
    super();
    this.state = {
      success: false,
      fail: false,
    }
  }
  handleSubmit = (event) => {}
  

  render = () => {
    return (
      <div>
        <div className="modal fade" id={this.props.id}>
          <div className="modal-dialog modal-lg">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title" id="exampleModalLabel">{this.props.title}</h5>
                <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div className="modal-body">
                {this.renderModalContent()}
              </div>
              <div className="modal-footer">
                <SubmitInput 
                  label="Save"
                  success={this.state.success}
                  fail={this.state.fail}
                  modal={true}
                  onSubmit={this.handleSubmit}
                />
                <button type="button" className="btn btn-secondary" data-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}