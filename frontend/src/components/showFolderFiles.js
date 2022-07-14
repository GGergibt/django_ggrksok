import {React, useState, useEffect} from 'react';

import {Link, useParams} from 'react-router-dom';

import FilesList from './filesList'


const ShowFolder = ({cookies}) => {
	const folderName = useParams().account_name
	console.log(folderName)
	const [apisResponse, setApisResponse] = useState(false)
	const [init, setInit] = useState('')
	const getFiles = async () => {
		const response = await fetch(`http://localhost:8000/install/instagram/get/${folderName}`).then((response) => response.json())
		setApisResponse(response)
		console.log(response.files)
		response.files.map((file) => {console.log(file)})

	}
	// useEffect(
	// 	showFiles, [init]
	// )
	// useEffect(() => {getFiles()}, [init])

	return (
		<>
			<div class="container">
			 {/* <button onClick={getFiles}> Список сторис</button> */} 
				<h1 className="flex justify-center"> {folderName}</h1>
			{/* {apisResponse? apisResponse.files.map((files) => {return <Link download target="_blank" to={`/instagram/${folderName}/${files}`}>{files}</Link>}): <h1></h1>} */}
			 {apisResponse? <FilesList fileNames={apisResponse} cookies={cookies} category={"stories"} accountName={folderName}/> : getFiles()? '' : 'no files'}

		</div>
		</>

	)

}

export default ShowFolder
