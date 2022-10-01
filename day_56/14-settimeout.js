// function hello(){
//     console.log("Hello Srikar")
// }

// setTimeout(hello,3000)

function hello(name){
    console.log(`Hello ${name}`)
}

const timeset=setTimeout(hello,3000,"Srikar")
clearTimeout(timeset)
