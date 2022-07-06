import React, {useState, useEffect} from 'react';

import FileItem from './fileItem'


const FilesList = ({history, cookies, category, accountName}) => {
	console.log(accountName)
	const [typeMedia, setTypeMedia] = useState("")
	const filesList = history.files? history.files: history

	useEffect(() => {
	if (category === "stories") {
		setTypeMedia("instagram")

	}
	else {
		setTypeMedia("youtube")
	}
	}
	)
	return(
		<ul class="p-4  pt-4 ">
		{filesList.map((folder) => {return <FileItem accountName={accountName} cookies={cookies} fileDetail={folder} typeMedia={typeMedia} category={category}/>})}
		</ul>
	)
}

export default FilesList
