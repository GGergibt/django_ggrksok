import React from 'react';

import FileItem from './fileItem'


const FilesList = ({history}) => {
	return(
		<ul class=" list-style-none m-0 p-0 center my-20 mb-10">
		{history.map((folder) => {return <FileItem fileDetail={folder} typeMedia="youtube"/>})}
		</ul>
	)
}

export default FilesList
