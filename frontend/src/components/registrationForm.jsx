import React, {useState, useEffect} from 'react'

const RegistrationForm = ({addToken}) => {
    const [username, setUsername] = useState('')
    // const [usernameCheck, setUsernameCheck] = useState(false)
    const [email, setEmail] = useState('')
    const [isEmailValid, setIsEmailValid] = useState(false)
    const [password, setPassword] = useState('')
    const [isPasswordValid, setIsPasswordValid] = useState(true)
    const [isPasswordExists, setIsPasswordExists] = useState(false)
    const [passwordConfirm, setPasswordConfirm] = useState('')
    useEffect(() => {
	    const validateEmail = email.includes('@') && email.includes('.')
	    const checkPasswordExists = password? true: false
	    setIsPasswordExists(checkPasswordExists)
	    if (checkPasswordExists) {
		    const validatePassword = password === passwordConfirm
		    setIsPasswordValid(validatePassword)
	    }
	    setIsEmailValid(validateEmail)
}, [email, password, passwordConfirm])
   const submitHandler = async (event) => {
	   event.preventDefault()
	   if (isEmailValid & isPasswordValid & isPasswordExists) {
		   const requestDetails = {
		    method: 'POST',
		    headers: { 'Content-Type': 'application/json' },

		    body: JSON.stringify({
			    name: username,
			    email: email,
			    password: password})
	   }
	   const response = await fetch("http://localhost:8000/users/create/", requestDetails).then((response) => response.json())
           addToken(response.token)

   }
   }


 



    return(
	      <div className="form">
		  <div className="form-body">
			  <div className="username relative z-0 w-full mb-6 mt-6 group  ">
			  <label className="form__label peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6" htmlFor="firstName">First Name </label>
			      <input onChange={(event) => {setUsername(event.target.value)}} className="form__input block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" type="text" id="firstName" placeholder="First Name"/>
		      </div>
		      <div className="email relative z-0 w-full mb-6 group">
			  <label className="form__label peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6" htmlFor="email">Email </label>
			      <input onChange={(event) => {setEmail(event.target.value)}} type="email" id="email" className="form__input block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" placeholder="Email"/>

		      </div>
		      <div className="password relative z-0 w-full mb-6 group">
			  <label className="form__label peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6" htmlFor="password">Password </label>
			  <input onChange={(event) => {setPassword(event.target.value)}} className="form__input block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" type="password"  id="password" placeholder="Password"/>
		      </div>
		      <div className="confirm-password relative z-0 w-full mb-6 group">
			  <label className="form__label peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6" htmlFor="confirmPassword">Confirm Password </label>
			  <input onChange={(event) => {setPasswordConfirm(event.target.value)}} className="form__input block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer" type="password" id="confirmPassword" placeholder="Confirm Password"/>
		      </div>
		  </div>
		   <form onSubmit={submitHandler}>
		  <div className="footer" >
			  {isEmailValid? <h1></h1>: <h1>Почтовый адрес должен содержать символы  @ и .</h1>}
			  {isPasswordValid? <h1></h1>: <h1>Пароли не совпадают</h1>}
			  {isPasswordExists? <h1></h1>: <h1> Введите пароль</h1>}
			  { isEmailValid && isPasswordValid && isPasswordExists? <button type="submit" class="btn">Register</button>: <h1></h1>  }
			  
          </div>
		   </form>
      </div>
    )
}


export default RegistrationForm
