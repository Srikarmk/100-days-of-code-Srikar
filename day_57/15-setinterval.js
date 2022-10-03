function hello(name){
    console.log(`Hello ${name}`)
}

const interval = setInterval(hello,2000,'Srikar')
clearInterval(interval)
