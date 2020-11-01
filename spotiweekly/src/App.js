import './App.css';
import Navbar from './components/Navbar.jsx';
import Authentication from './components/Authentication.jsx'

function App() {
  return (
    <div className="App">
      <Navbar value="kek"/>
      <Authentication />
    </div>
  );
}

export default App;
