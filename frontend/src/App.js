import './App.css';
import UrlForm from './components/formComponent'
import { Routes, Route, Link } from 'react-router-dom'
import {useState, React} from 'react'
import {useCookies} from 'react-cookie'

import SomePage from './pages/somePage';
import RegistrationPage from './pages/registrationPage';
import LoginPage from './pages/loginPage';
import HistoryPage from './pages/historyPage'
import ShowFolder from './components/showFolderFiles'

import Layout from './components/Layout'

function App() {
  const [isAuth, setIsAuth] = useState(false)
  const [tokenCookie, setTokenCookie] = useCookies(false)

  const  addToken = (response) => {
	  const expiresDate = new Date(response.expires)
	  setTokenCookie("token", response.token, {expires: expiresDate} )
  }

  return (
	  <>
		  <div>
			

		  </div>
		  <Routes>
			  <Route path="/" element={<Layout cookies={tokenCookie}/>}>
				  <Route index element={<UrlForm cookies={tokenCookie}/>}/>
				  <Route path="registration/" element={<RegistrationPage addToken={addToken}/>}/>
				  <Route path="login/" element={<LoginPage addToken={addToken}/>}/>
				  <Route path="history/" element={<HistoryPage cookies={tokenCookie}/>} />
				  <Route path="show_folder/:account_name" element={<ShowFolder/>} />
			</Route>
		  </Routes>


	  </>

	  
  );
}

export default App;
