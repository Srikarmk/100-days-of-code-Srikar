function greet(name){
    console.log(`Hello ${name}`)
}

function name(greetfn){
    peru="Srikar"
    greet(peru)
}

name(greet)

//callback function - a func that is passed as args to another func 
//HOF - a func that accepts a func as parameter
