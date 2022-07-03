import React from 'react'

import HistoryForm from '../components/historyForm'


const HistoryPage = ({cookies}) => {
	return(
		<div>
			<HistoryForm cookies={cookies}/>
		</div>
	)
}

export default HistoryPage
