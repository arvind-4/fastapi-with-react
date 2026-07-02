import { Header, HeaderContainer, HeaderName, HeaderNavigation, HeaderMenuButton, HeaderMenuItem } from '@carbon/react';
import React from 'react';
import { Link } from 'react-router-dom';

const TutorialHeader = () => (
  <HeaderContainer
    render={({
      isSideNavExpanded,
      onClickSideNavExpand,
    }: {
      isSideNavExpanded: boolean;
      onClickSideNavExpand: () => void;
    }) => (
      <Header>
        <HeaderMenuButton aria-label='Open menu' onClick={onClickSideNavExpand} isActive={isSideNavExpanded} />
        <HeaderName element={Link} to='/'>
          Auth Login
        </HeaderName>
        <HeaderNavigation>
          <HeaderMenuItem element={Link} to='/login'>
            Login
          </HeaderMenuItem>
          <HeaderMenuItem element={Link} to='/register'>
            Register
          </HeaderMenuItem>
        </HeaderNavigation>
      </Header>
    )}
  />
);

export default TutorialHeader;
