import React, {useState} from 'react';
import fileDownload from 'js-file-download'

import './cssComponents/history.css'
const styles = {
	li: {
  	 	display: 'flex',
		// justifyContent: 'space-between',
		// alignItems: 'center',
		// padding: '.5rem 1rem',
		// border: '1px solid #ccc',
		// borderRadius: '4px',
		// marginBottom: '.5rem'
	
	},
	input: {
		marginRight: '1rem'
	}
}


const FileItem = ({fileDetail, typeMedia}) => {
	const clickHandler = () => {

		const response = fetch(`http://localhost:8000/media/${typeMedia}/${fileDetail.folder_name}`).then((response) => response.blob())
		console.log(response)
		fileDownload(response, fileDetail.folder_name)


	}

	return (
		<>
		<li class="justify-content-center ">
		<button  class="py-2 px-4 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white" onClick={clickHandler}>{fileDetail.folder_name}</button>
			Количество Скачиваний : {fileDetail.max}

		</li>
		{/* <div> */}
		{/* </div> */}
		</>
	)
}

export default FileItem
