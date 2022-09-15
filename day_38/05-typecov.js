console.log(5+'3')
console.log(5-'3')
console.log('3'-'2')
console.log('3'*'2')
console.log('3'*null)//0
console.log('3'+true)
console.log('Srikar'-'M') //Nan
console.log(5+undefined) //Nan
console.log(true+'3')
console.log(3-'true') //Nan
console.log(Number(false))
console.log(Number(null))
console.log(Number(''))
console.log(Number('3'))
console.log(parseInt('4'))
console.log(parseFloat('3.14'))
console.log(String(500))
console.log((500).toString())
// console.log((null).toString())//won't work on null and undef
console.log(Boolean(10)) // null , undef , '' , 0 , NaN - false
