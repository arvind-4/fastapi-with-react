import './app.scss';
import { Content, Theme } from '@carbon/react';
import TutorialHeader from './components/TutorialHeader/TutorialHeader';
import { Route, Switch } from 'react-router-dom';
import LandingPage from './content/LandingPage/LandingPage';
import RepoPage from './content/RepoPage/RepoPage';

import LoginPage from './content/LoginPage/LoginPage';
import RegisterPage from './content/RegisterPage/RegisterPage';
import React from 'react';

export default function App() {
  return (
    <React.Fragment>
      <Theme theme='g100'>
        <TutorialHeader />
      </Theme>
      <Content>
        <Switch>
          <Route exact path='/' component={LandingPage} />
          <Route exact path='/login' component={LoginPage} />
          <Route exact path='/register' component={RegisterPage} />
          <Route exact path='/repo' component={RepoPage} />
        </Switch>
      </Content>
    </React.Fragment>
  );
}
