import {React, useEffect, useState} from 'react'

import './cssComponents/history.css';

import FilesList from './filesList';

const HistoryForm = ({cookies}) => {
	const [category, setCategory] = useState("videoYtb")

	const [history, setHistory] = useState(false)
	// useEffect(() => {
	// 	if (history) {
	// 	history.map((folderName) => {
	// 		return (<h1> {folderName.folder_name}</h1>)
	// 	})}
	// }, [history])

	const getUsersHistory = async () => {
		const requestOptions = {
			method: 'GET',
			headers: {
				'accept': 'application/json',
				'token': cookies.token
			}
		}
		const responseApi = await fetch(`http://localhost:8000/install/most_popular?category=${category}`, requestOptions).then((responseApi) => responseApi.json())
		console.log(responseApi)
		setHistory(responseApi)
	}
	useEffect(() => {const response = getUsersHistory()
	}, [category])

	return (
		<>
			<div className=" flex ml-6 pb-6 justify-center mx-auto  " role="group">
		  <button type="button" onClick={() => {setCategory("videoYtb")}} type="button" class="py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-l-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
			  Видео Youtube
		  </button>
		  <button type="button" onClick={() => {setCategory("audioYtb")}} type="button" class="py-2 px-4 text-sm font-medium text-gray-900 bg-white border-t border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
			 Аудио Youtube
		  </button>
		  <button type="button" onClick={() => {setCategory("stories")}} type="button" class="py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-r-md border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
			  Сторис
		  </button>

		</div>
			<div className="flex justify-center">

			{history? <FilesList category={category} cookies={cookies} history={history}/>: <p>Нет скачиваний</p>}
			</div>
			{/* <h1>{history? history.map((folder) => {return (<button class="py-2 px-4 text-sm font-medium text-gray-900">{folder.folder_name}</button>)}) : <h1></h1>}</h1> */}
		</>
	)
}

export default HistoryForm
