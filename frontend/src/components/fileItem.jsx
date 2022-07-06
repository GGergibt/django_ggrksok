import React, {useState, useEffect} from 'react';
import fileDownload from 'js-file-download'

import {Link} from 'react-router-dom';

import './cssComponents/history.css'
const styles = {
	li: {
  	 	display: 'flex',
		justifyContent: 'space-between',
		alignItems: 'center',
		padding: '.5rem 1rem',
		border: '1px solid #ccc',
		borderRadius: '4px',
		marginBottom: '.5rem'
	
	},
	input: {
		marginRight: '1rem'
	}
}


const FileItem = ({fileDetail, typeMedia, cookies, category, accountName}) => {

	const [count, setCount] = useState('')
	useEffect(() => {if (fileDetail.max) {setCount(fileDetail.max)}}, [fileDetail.max])

	// console.log(count, init)
	const fileName = fileDetail.folder_name? fileDetail.folder_name: fileDetail
	const basePath = "http://localhost:8000/media"
	const pathMedia = fileDetail.folder_name? `${basePath}/${typeMedia}/${fileName}`: `${basePath}/${typeMedia}/${accountName}/${fileName}`

	const clickHandler = async () => {
		// setCount(fileDetail.max)

		// const fileNameWithoutEx = fileDetail.folder_name.split(".")[0]

		// const requestDetails = {
		// 	method: 'POST'}

		// const apiResponse = fetch(`http://localhost:8000/install/youtube/video?url=https://www.youtube.com/watch?v=${fileNameWithoutEx}&query_format=${category}`, requestDetails).then(apiResponse => apiResponse.json())

		const response = await fetch(pathMedia).then((response) => response.blob())
		console.log(response)
		fileDownload(response, fileName)
		if (response) {
			if (cookies.token) {
				// c
				const requestDetails = {
					method: 'POST',
					headers: {
					      'Content-Type': 'application/json',
					      'token': cookies.token
					},
					body: JSON.stringify({
						destination_folder: `/home/gosha/projects/react_ggrksok/backend/media/${typeMedia}/${fileDetail.folder_name? fileName:    accountName}`, 
						folder_name: fileDetail.folder_name? fileName: accountName,
						category: category
				})
			}
			const response = await fetch("http://localhost:8000/install/add_info_from_auth_user", requestDetails).then((response) => response.json())
			console.log(response)
		        console.log(fileDetail)
		     	setCount(count+1)

			}
		}


	}
	const checkIdFileUser = accountName? fileName.includes("id")? true: false: false

	return (
		<>
		<li>
			<span>
				{fileName.includes(".mp4") || fileName.includes(".webm") || fileName.includes(".jpg")? <button type="button" className="py-2 px-4 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white" onClick={clickHandler}>{fileName}</button>:fileName.includes("json") || 	checkIdFileUser?  '': <Link className="py-2 px-4 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white" to={`/show_folder/${fileName}`}>{fileName}</Link>}
				 {/* Количество Скачиваний : {fileDetail.max} */}
				{accountName? '': `Количество скачиваний: ${count}`}

			</span>

		</li>
		{/* <div> */}
		{/* </div> */}
		</>
	)
}

export default FileItem
