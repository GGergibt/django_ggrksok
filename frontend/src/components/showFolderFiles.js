import {React, useState, useEffect} from 'react';

import {Link, useParams} from 'react-router-dom';


const ShowFolder = () => {
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
	const showFiles = () => {
		console.log("ii")
		apisResponse? apisResponse.files.map((files) => {return <Link download target="_blank" to={`/instagram/mishe_mozh/${files}`}>{files}</Link>}): console.log("hwllo")

	}
	// useEffect(showFiles, [apisResponse])

	return (
		<>
		<div> 
			<h1>fafhafhdf</h1>
			<div class="container">
			<button onClick={getFiles}> hhhh </button>
			{apisResponse? apisResponse.files.map((files) => {return <Link download target="_blank" to={`/instagram/${folderName}/${files}`}>{files}</Link>}): <h1></h1>}

		</div>
		</div>
		</>

	)

}

export default ShowFolder
