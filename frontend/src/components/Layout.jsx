import {React, useEffect} from 'react'

import {Link, Outlet} from 'react-router-dom'

import './cssComponents/layout.css'







const Layout = ({cookies}) => {
	// console.log(cookies.token)
	useEffect(
	() => {console.log(cookies.token)},
	[cookies])
	const link = "/jj.mp4"

	return (
		<>
		  <header className="">



			  <div className="bg-gray-500 flex">
			  {/* <a href="/api"> home</a> */}
			  {/* <a href="/api/posts"> blog</a> */}
			  {<Link to="/" className="py-2 px-4 text-sm font-medium text-gray-900 rounded-l-lg hover:bg-gray-600 hover:text-blue-700 focus:z-10  focus:ring-blue-700 focus:text-red-700 dark:bg-gray-700 bg-gray-500 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
			  Home
		  </Link>}
			  {<Link to="/registration" className="py-2 px-4 text-sm font-medium text-gray-900  hover:bg-gray-600 hover:text-blue-700 focus:z-10 focus:ring-blue-700 bg-gray-500 focus:text-red-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
	           Зарегистрироваться 
		  </Link>}
			  {<Link to="/login" className="py-2 px-4 text-sm font-medium text-gray-900  rounded-r-md hover:bg-gray-600 hover:text-blue-700 focus:z-10   bg-gray-500 focus:text-red-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
			  Войти
		  </Link>}
			  {cookies.token? <Link to="/history" className="py-2 px-4 text-sm font-medium text-gray-900 rounded-r-md hover:bg-gray-600 hover:text-blue-700  focus:ring-blue-700 bg-gray-500 focus:text-red-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
				  История скачиваний
			  </Link> : <h1></h1>}
			  </div>
		  </header> 
			  <div className="container my-10 mx-auto w-2/5">
			<Outlet/>
			  </div>
			  </>

	)
} 

export default Layout
