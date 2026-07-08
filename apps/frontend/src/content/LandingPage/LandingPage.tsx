import React from 'react';
import {
  Breadcrumb,
  BreadcrumbItem,
  Button,
  Tabs,
  Tab,
  TabList,
  TabPanels,
  TabPanel,
  Grid,
  Column,
} from '@carbon/react';

export default function LandingPage() {
  return (
    <Grid className='landing-page' fullWidth>
      <Column lg={16} md={8} sm={4} className='landing-page__banner'>
        <Breadcrumb noTrailingSlash aria-label='Page navigation'>
          <BreadcrumbItem>
            <a href='/login'>Login here to Get Started</a>
          </BreadcrumbItem>
        </Breadcrumb>
        <h1 className='landing-page__heading'>Design &amp; build with Carbon</h1>
      </Column>
      <Column md={4} lg={7} sm={4} className='landing-page__tab-content'>
        <h2 className='landing-page__subheading'>What is Carbon?</h2>
        <p className='landing-page__p'>
          Carbon is IBM’s open-source design system for digital products and experiences. With the IBM Design Language
          as its foundation, the system consists of working code, design tools and resources, human interface
          guidelines, and a vibrant community of contributors.
        </p>
        <Button>Learn more</Button>
      </Column>
      <Column lg={16} md={8} sm={4} className='landing-page__r3'>
        <Grid>
          <Column md={4} lg={4} sm={4}>
            <h3 className='landing-page__label'>The Principles</h3>
          </Column>
          <Column md={4} lg={4} sm={4}>
            Carbon is Open
          </Column>
          <Column md={4} lg={4} sm={4}>
            Carbon is Modular
          </Column>
          <Column md={4} lg={4} sm={4}>
            Carbon is Consistent
          </Column>
        </Grid>
      </Column>
    </Grid>
  );
}
