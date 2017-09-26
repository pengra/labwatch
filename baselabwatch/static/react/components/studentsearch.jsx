// https://getbootstrap.com/docs/4.0/components/modal/

class EditStudentForm extends Form {
  renderForm = () => {
    const formData = this.state.formData;
    return (<div>
      <TextInput 
      name="student_id" 
      formData={formData.student_id} 
      onChange={this.onChange}
      errors={this.state.errors.student_id}
      key="student_id"
    />
    <TextInput 
      name="first_name" 
      formData={formData.first_name} 
      onChange={this.onChange}
      errors={this.state.errors.first_name}
      key="first_name"
    />
    <TextInput 
      name="last_name" 
      formData={formData.last_name} 
      onChange={this.onChange}
      errors={this.state.errors.last_name}
      key="last_name"
    />
    <TextInput 
      name="nick_name" 
      formData={formData.nick_name} 
      onChange={this.onChange}
      errors={this.state.errors.nick_name}
      key="nick_name"
    />
    <TextInput 
      name="email" 
      formData={formData.email} 
      onChange={this.onChange}
      errors={this.state.errors.email}
      key="email"
    />
    <TextInput 
      name="teacher" 
      formData={formData.teacher} 
      onChange={this.onChange}
      errors={this.state.errors.teacher}
      key="teacher"
    />
    <SelectInput
      name="grade"
      formData={formData.grade}
      onChange={this.onChange}
      errors={this.state.errors.grade}
      key="grade"
    />
    </div>)
  }
}

class EditStudentModal extends Modal {
  constructor() {
    super();
    this.state = {
      id: 'student-edit-form'
    }
  }
  handleSubmit = (event) => {
    event.preventDefault();
    this.child.handleSubmit(event);
  }
  onSuccess = (data) => {
    this.setState({
      success: true,
      fail: false
    })
    setTimeout(() => {
      this.setState({
        success: false
      });
    }, 3000)
  }
  onFail = (data) => {
    this.setState({
      success: false,
      fail: true
    })
    setTimeout(() => {
      this.setState({
        fail: false
      });
    }, 3000)
  }
  renderModalContent = () => {
    if (this.props.pk) {
      return (
        <EditStudentForm 
          ref={instance => {this.child = instance}}
          url={"/base/api/v1/students/" + this.props.pk + '/'} 
          id={this.state.id}
          overrideSuccess={this.onSuccess}
          overrideFail={this.onFail}
        />
      )
    } else {
      return null;
    }
    
  }
}

class StudentSearchForm extends React.Component {
  // props:
    // helptext : small text
    // url : search endpoint
  constructor() {
    super();
    this.state = {
      results: [],
      pk: null,
    }
  }
  handleSubmit = (event) => {
    event.preventDefault();
    const query = $('#query-box').val();
    if (query.length === 0) {
      return;
    }
    $.ajax({
      method: 'GET',
      url: this.props.url,
      data: {
        search: query
      }
    }).done((data) => this.setState({results: data}));
  }
  updatePk = (value) => {
    this.setState({
      pk: value
    });
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
                  onMouseOver={() => this.updatePk(data.pk)}
                >Details/Edit</button></td>
            </tr>
          )}
        </tbody>
      </table>
      
    );
  }
  renderModal = () => {
    return (
      <EditStudentModal 
        id="student-edit-modal" 
        title="Edit a Student" 
        url={this.props.url + this.state.pk + '/'} 
        pk={this.state.pk}
      />
    )
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
          {this.renderModal()}
      </div>
    )
  }
}