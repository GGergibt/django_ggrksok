import React from 'react';
import LoginForm from '../components/loginForm'

import {Link} from 'react-router-dom'

const LoginPage = ({addToken}) => {
	return (
		<>

		<main className="container">
			<LoginForm addToken={addToken}/>
		</main>

		</>
	)
}

export default LoginPage
