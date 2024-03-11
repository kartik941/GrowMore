const url = 'https://real-time-finance-data.p.rapidapi.com/search?query=Tata&language=en';
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'f1787aa681mshe3821ad5ec4f6d6p1eaa44jsn593e9508c60c',
		'X-RapidAPI-Host': 'real-time-finance-data.p.rapidapi.com'
	}
};

	fetch(url, options)
    .then(response => response.json())
    .then(Data => {
        console.log(Data)
        let tabledata = ""
        let count = 0
        Data.data.stock.map((values)=>{

            count = count+1
            tabledata+=`<tr >
            <th scope="row">${count}</th>
            <td>${values.name}</td>
            <td>${values.symbol}</td>
            <td>${values.price}</td>
          </tr>`
        })
        
    document.getElementById("mar-data").innerHTML = tabledata;
    })

    .catch(error => console.log(error));

