import React from 'react';
import { TextInput, Button } from '@carbon/react';

import { baseUrl } from '../../constants';

import './login.css';
export default function LoginPage() {
  async function handleSubmit(evt: React.FormEvent<HTMLFormElement>) {
    evt.preventDefault();
    const formData = new FormData(evt.currentTarget);
    const data = {
      username: formData.get('username'),
      password: formData.get('password'),
    };
    console.log(data);
    const res = await fetch(`${baseUrl}/users/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    console.log('Tes status: ', res.status);
    if (res.status === 200) {
      const response = await res.json();
      // const cookies = new Cookies();
      // cookies.set('auth', response.access_token);
      window.location.href = '/';
    } else {
      alert('Invalid Credentials');
    }
  }
  return (
    <div className='container-fluid ps-md-0'>
      <div className='row g-0'>
        <div className='d-none d-md-flex col-md-4 col-lg-6 bg-image' />
        <div className='col-md-8 col-lg-6'>
          <div className='login d-flex align-items-center py-5'>
            <div className='container'>
              <div className='row'>
                <div className='col-md-9 col-lg-8 mx-auto'>
                  <h3 className='login-heading mb-4'>Welcome back!</h3>
                  <form onSubmit={handleSubmit}>
                    <div className='form mb-3'>
                      <label className='py-2'>Username</label>
                      <TextInput type='email' name='username' placeholder={'Enter Your Username...'} />
                    </div>
                    <div className='form mb-3'>
                      <label className='py-2'>Password</label>
                      <TextInput type='password' name='password' placeholder={'Enter Your Password...'} />
                    </div>
                    <div className='py-4 text-center'>
                      <Button
                        classNameName='btn btn-lg btn-primary btn-login text-uppercase fw-bold mb-2'
                        type='submit'
                      >
                        Sign in
                      </Button>
                      <br />
                      <div className='pt-3 text-center'>
                        Don't have an Account?{' '}
                        <a className='small' href='/register'>
                          Register Here.
                        </a>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
