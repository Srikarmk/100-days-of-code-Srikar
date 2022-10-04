//get element by id
// const first= document.getElementById('main-heading')
// console.log(first)

// get Elements by class 
// const lt=document.getElementsByClassName('list-item')
// console.log(lt)

// get Elements by tagname  
// const tag=document.getElementsByTagName('li')
// console.log(tag)

//querySelector()
// const item=document.querySelector('li')
// console.log(item)

//querySelectorAll()
// const sen=document.querySelectorAll('li')
// console.log(sen)


const item = document.querySelector('li')

item.innerHTML="Ford"

const title= document.getElementById("main-heading")

title.style.color='pink' 

title.style.fontSize='2.5em'

//creating elements 

const ul=document.querySelector('ul')

const li = document.createElement('li')

ul.append(li)
li.innerText='Mustang'
li.setAttribute('class','list-item')
