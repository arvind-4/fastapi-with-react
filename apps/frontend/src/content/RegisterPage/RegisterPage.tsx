import React from 'react';
import { TextInput, Button, Link } from '@carbon/react';

import './_register-page.css';
export default function RegisterPage() {
  return (
    <div className='register-body'>
      <div className='container'>
        <div className='row'>
          <div className='col-sm-9 col-md-7 col-lg-5 mx-auto'>
            <div className='card border-0 shadow rounded-3 my-5'>
              <div className='card-body p-4 p-sm-5'>
                <h5 className='card-title text-center mb-5 fw-light fs-5'>Register Here</h5>
                <form>
                  <label>Username</label>
                  <div className='my-3'>
                    <TextInput type='text' placeholder='Enter Your Username...' />
                  </div>
                  <label>Email address</label>
                  <div className='my-3'>
                    <TextInput type='email' placeholder='Enter Your Email...' />
                  </div>
                  <label>Password</label>
                  <div className='my-3'>
                    <TextInput type='password' placeholder='Enter Your Password...' />
                  </div>

                  <div className='text-center'>
                    <Button classNameName='btn btn-primary btn-login text-uppercase fw-bold' type='submit'>
                      Register
                    </Button>
                  </div>
                  <hr className='my-4' />
                  <div className='text-center'>
                    <p className='mb-2'>Already have an account?</p>
                    <a href='/login'>
                      <Button kind='ghost' classNameName='btn btn-primary btn-login text-uppercase fw-bold'>
                        Login Here.
                      </Button>
                    </a>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
