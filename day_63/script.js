async function fetchData(){
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '261e502eadmshb384a38b034b2a8p14fdb2jsnfa9d66377695',
            'X-RapidAPI-Host': 'covid-19-statistics.p.rapidapi.com'
        }
    };
    
    const res = await fetch('https://covid-19-statistics.p.rapidapi.com/reports/total?date=2020-10-17', options)
        
    const record = await res.json()
    console.log(record.data)
    document.getElementById("date").innerHTML="Date : " +record.data.date
    document.getElementById("active").innerHTML="Active Cases : " +record.data.active
    document.getElementById("deaths").innerHTML="Deaths : " +record.data.deaths
    document.getElementById("recovered").innerHTML="Recovered : " +record.data.recovered


}

fetchData()