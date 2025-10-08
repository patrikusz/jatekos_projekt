import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import './styles/LoginForm.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" exact component={LoginForm} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;