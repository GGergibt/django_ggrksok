import React, {useState, useEffect} from 'react';

import FileItem from './fileItem'


const FilesList = ({fileNames, cookies, category, accountName}) => {
	//accountName необязательное поле. Только для отображения сторис
	const [typeMedia, setTypeMedia] = useState("")
	const filesList = fileNames.files? fileNames.files: fileNames

	useEffect(() => {
	if (category === "stories") {
		setTypeMedia("instagram")

	}
	else {
		setTypeMedia("youtube")
	}
	}
	)
	console.log(filesList)
	return(
		<ul className="list-none ml-6 max-h-[350px] pt-4 overflow-y-scroll"> 
			{filesList.length > 0? filesList.map((folder) => {return <FileItem accountName={accountName} cookies={cookies} fileDetail={folder} typeMedia={typeMedia} category={category}/>}) : <p>Нет скачиваний</p>}
		</ul>
	)
}

export default FilesList
