class App extends React.Component {
  render() {
    return (!this.props.isAuthenticated) ? <Intro /> : <Playlists url={this.props.playlistsUrl} />
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

class Playlists extends React.Component {
  render() {
    console.log(this.props.url)

    return <div>
      <h2 className="uk-text-center">Your Playlists</h2>
    </div>
  }
}

ReactDOM.render(
  <App isAuthenticated={isAuthenticated} playlistsUrl={allPlaylists} />,
  document.getElementById("root")
)
