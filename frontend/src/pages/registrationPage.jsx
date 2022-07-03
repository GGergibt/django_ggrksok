import React from 'react';

import {Link} from 'react-router-dom';

import RegistrationForm from '../components/registrationForm'


const RegistrationPage = ({addToken}) => {
	return (
		<>

		<main className="container">
			<RegistrationForm addToken={addToken}/>
		</main>
		</>
	)
}

export default RegistrationPage


