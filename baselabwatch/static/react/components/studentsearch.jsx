// https://getbootstrap.com/docs/4.0/components/modal/

class EditStudentModal extends Modal {

}

class StudentSearchForm extends React.Component {
  // props:
    // helptext : small text
    // url : search endpoint
  constructor() {
    super();
    this.state = {
      results: [],
    }
  }
  handleSubmit = (event) => {
    event.preventDefault();
    const query = $('#query-box').val();
    if (query.length === 0) {
      return;
    }
    console.log(this.props.url)
    $.ajax({
      method: 'GET',
      url: this.props.url,
      data: {
        search: query
      }
    }).done((data) => this.setState({results: data}));
  }
  renderResults = () => {
    const results = this.state.results;
    return (
      <table className="table">
        <thead>
          <tr>
            <th>Student ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {results.map((data) => 
            <tr key={data.student_id}>
              <td>{data.student_id}</td>
              <td>{data.first_name}</td>
              <td>{data.last_name}</td>
              <td>
                <button 
                  className="btn btn-primary" 
                  data-toggle="modal" 
                  data-target="#student-edit-modal"
                >Details/Edit</button></td>
            </tr>
          )}
        </tbody>
      </table>
      
    );
  }
  render = () => {
    return (
      <div className="search-component">
        <form className="row" onSubmit={this.handleSubmit}>
          <div className="col-10">
            <input type="text" name="query" className="form-control" id="query-box" />
            <small className="form-text text-muted">
              Search by: First/Last/Nick name, email, student ID, grade or teacher.
            </small>
          </div>
          <div className="col-2">
            <input type="submit" value="Search" className="btn btn-primary btn-block" />
          </div>
        </form>
        <div className="search-results">
          <div className="col-12">
            {this.renderResults()}
          </div>
        </div>
        <EditStudentModal id="student-edit-modal" />
      </div>
    )
  }
}