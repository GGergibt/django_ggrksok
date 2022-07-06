import React, {useState, useEffect, useRef} from 'react'
import {Link} from 'react-router-dom';
import '../index.css';
import './cssComponents/index.css'

import fileDownload from 'js-file-download';

import ShowFolder from './showFolderFiles';


const styles = {
	form: {
		marginBottom: '1rem',
		  alignItems: 'center',
		  justifyContent: 'center'
		},
	div: {
          alignItems: 'center',
          justifyContent: 'center'
		
	},
	input: {
		width: '100%',
		padding: '6px 10px',
		margin: '10px 10py',
		border: '1px solid #ddd',
		boxSizing: 'border-box',
		display: 'block',
		color: "blue", 

	}
}

function UrlForm({cookies}) {
	const [value, setValue] = useState('')
	const [typeDownload, setType] = useState('')

	const [url,  setUrl] = useState(false)
	const checkUrl = () => {
		typeDownload === "instagram"?  setUrl(value.includes("https://www.instagram.com")): setUrl(value.includes("https://www.youtube.com"))
	} 
	const [apiResponse,  setApiResponse] = useState(false)
	const [awaitResponse,  setAwaitResponse] = useState(false)
	const [video, setVideo] = useState(false)
	// const sendInfoIfAuth = () => {
	// 	console.log("hello")
	// }
	const sendInfoIfAuth = async () => {
		// if (cookies.token) {
		// 	console.log(apiResponse !=='j', cookies.token)
		// }

		if (apiResponse) {
			if (cookies.token) {
				console.log("hello")
				// c
				const requestDetails = {
					method: 'POST',
					headers: {
					      'Content-Type': 'application/json',
					      'token': cookies.token
					},
					body: JSON.stringify({
						...apiResponse
				})
			}
			const response = await fetch("http://localhost:8000/install/add_info_from_auth_user", requestDetails).then((response) => response.json())
			console.log(response)

			}
		}
	}


	useEffect(checkUrl, [value, typeDownload])
	useEffect(() => {const result = sendInfoIfAuth()}, [apiResponse])




	const submitHandler = async (event) => {
		event.preventDefault()
		setAwaitResponse(true)
		// cookies.token? console.log("hello"): console.log(":w")
		// if (cookies.token) {
		// 		}
		// 		)
		// 	}
		// 	const response = await fetch('')
		// }


		if (value.trim()) {
			// console.log(event.target.value)
			//
			const requestOptions = {
				method: 'POST',
				    };
			if (typeDownload !== 'instagram') {
				console.log(typeDownload)
				const response = await fetch(`http://localhost:8000/install/youtube/video?url=${value}&query_format=${typeDownload}`, requestOptions).then((response) => response.json())
				setApiResponse(response)

				const responseApi = await fetch(`http://localhost:8000/media/youtube/${response.folder_name}`).then((responseApi) => responseApi.blob())
				setAwaitResponse(false)
				setVideo(responseApi)
				console.log(responseApi)

				// sendInfoIfAuth()
				console.log(response.folder_name)

			}
			else {
				const response = await fetch(`http://localhost:8000/install/instagram/install_stories/${value}`, requestOptions).then((response) => response.json())
				setApiResponse(response)
				setAwaitResponse(false)
				console.log(response.folder_name)
			}
		}
	}
	function valueHandler(event) {
		event.preventDefault()
		// setType(value)
		console.log(value)
	}
	return (
		<>
			<form className="" onSubmit={submitHandler}>
				<input  style={styles.input} value={value} onChange={event => setValue(event.target.value)}/>
				<select class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" onChange={(event) => {setType(event.target.value)}}>
					<option selected> Категория скачивания </option>
					{/* <option value="instagram">instagram</option> */}
					<option value="best">youtube</option>
					<option value="bestaudio">youtubeAudio</option>
				</select>
			</form>
			<form onSubmit={submitHandler}>
				{url? <button className="button py-2 px-4 text-sm bg-white hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white" type="submit"> Загрузить на сервер</button> : <h1></h1>}
			</form>
			{apiResponse? typeDownload === 'best' || typeDownload === 'bestaudio'? <button onClick={() => {fileDownload(video, apiResponse.folder_name)}} >Скачать</button>: <Link to={`/show_folder/${apiResponse.folder_name}`}> Сторис</Link> : <h1></h1>}
			{/* {apiResponse? typeDownload === 'best' || typeDownload === 'bestaudio'? <Link to={video} target="_blank" download>Загрузить</Link>: <Link to={`/show_folder/${apiResponse.folder_name}`}> Сторис</Link> : <h1></h1>} */}
			{awaitResponse & apiResponse? <h1>load</h1> : <h1> </h1>}
			{url & apiResponse?<h1>  </h1>: typeDownload === 'instagram'? <h1> Введите username </h1>:typeDownload==='best'|| typeDownload === 'bestaudio'? <h1> youtube  url должен начинаться с https://www.youtube.com </h1>: <h1></h1>}
		</>
	)

}


export default UrlForm
