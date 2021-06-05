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

class Playlist extends React.Component {
  render() {
    return <tr>
      <td><img class="uk-preserve-width uk-border-circle" src={this.props.imageUrl} width="40" alt="" /></td>
      <td className="uk-table-link"><a className="uk-link-reset" href="">{this.props.name}</a></td>
    </tr>
  }
}

class Playlists extends React.Component {
  componentDidMount() {
    this.getPlaylists()
  }
  constructor(props) {
    super(props)
    this.state = {
      playlists: [],
      previous: undefined,
      next: undefined,
    };
  }
  getPlaylists() {
    fetch(this.props.url)
      .then(response => response.json())
      .then(data => this.setState({ playlists: data.items, previous: data.previous, next: data.next }));
  }
  render() {
    console.log(this.state.playlists)
    return <div>
      <h3 className="uk-margin-top uk-text-center uk-text-muted">Your playlists</h3>
      <table className="uk-table">
        <thead>
          <tr>
            <th className="uk-table-shrink">Image</th>
            <th className="uk-table-shrink uk-text-nowrap">Name</th>
          </tr>
        </thead>
        <tbody>
          {this.state.playlists.map((plist, index) => < Playlist key={plist.id} name={plist.name} imageUrl={plist.images[0].url} />)}
        </tbody>
      </table>
    </div>
  }
}

ReactDOM.render(
  <App isAuthenticated={isAuthenticated} playlistsUrl={allPlaylists} />,
  document.getElementById("root")
)
