class App extends React.Component {
  renderNotAuthenticated() {
    return <Intro />
  }
  renderAuthenticated() {
    console.log(this.props.playlistsUrl)
    return <div>
      <Greeting greeting={this.props.isAuthenticated} />
    </div>
  }
  render() {
    if (!this.props.isAuthenticated) {
      return this.renderNotAuthenticated()
    }
    else {
      return this.renderAuthenticated();
    }
  }
}

class Intro extends React.Component {
  render() {
    return <div className="uk-margin-top uk-text-center">
      <h1 className="uk-text-success ">Spotiweekly</h1>
      <p>
        Are you tired of creating new playlists from your discovery weekly? First create new playlists and after that passing songs one by one? Say no more!
        Spotiweekly is here to help you!
      </p>
    </div>
  }
}

class Greeting extends React.Component {
  render() {
    return <h1>{String(this.props.greeting)}</h1>;
  }
}

ReactDOM.render(<App isAuthenticated={isAuthenticated} playlistsUrl={allPlaylists} />, document.getElementById("root"))
