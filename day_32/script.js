let red=document.getElementById("red")
let yellow=document.getElementById("yellow")
let green=document.getElementById("green")
let clear =document.getElementById("reset")
let squares=document.getElementsByClassName("square")

const count={red:0,yellow:0,green:0}

green.onclick=()=>{
  count.green+=1
  green.innerHTML=count.green
}

red.onclick=()=>{
  count.red+=1
  red.innerHTML=count.red
}

yellow.onclick=()=>{
  count.yellow+=1
  yellow.innerHTML=count.yellow
}

reset.onclick=()=>{
  count.green=0
  count.red=0
  count.yellow=0
  red.innerHTML=''
  yellow.innerHTML=''
  green.innerHTML=''
}
