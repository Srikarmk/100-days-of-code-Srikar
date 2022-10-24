/*
Commands: 

tsc.cmd -> to compile 
tsc.cmd --watch -> to keep watch on compilation 
tsc.cmd --init -> initializes a config file
*/


//Basic types
let id:number=5
let myName:string="Srikar"
let over18:boolean=true
let something:any='cool'

let nums:number[]=[1,2,3,4]
let strs:any[]=[1,true,'Srikar']

//Tuples

let tup:[number,string,boolean]=[1,'Sri',true]

//Tuple Arrays 

let tuparr:[number,string][]

tuparr=[
    [1,'Srikar'],
    [2,'Suraj'],
    [3,'Koushik']
    
]

//Unions 

let pid:string|number

pid ='22'

//Enums
enum directions{
    Up=3,
    Down,
    Left,
    Right
}

console.log(directions.Down)

//Objects

type User={
    id:number,
    name:string
}

let user:User={
    id:1,
    name:'Srikar'
}

//Type assertion - Similar to typecasting 

let cid : any =true
let customerId=<number>cid

let custId=cid as number

//Functions 

function add(x:number,y:number):number{
    return x+y
} 

console.log(add(2,3))

//Void 

function message(message : number|string):void{
    console.log(message)
}

message("Srikar")

//Interfaces 

interface UserInterface{
    readonly uid:number //cannot reassign cuz it's readonly
    fname:string
    age?:number  //? indicates optional
}

let fuser:UserInterface={
    uid:1,
    fname:'Srikar'
}


//Interfaces vs type assertion 

// type personid=number|string
// const p1:personid=1
// interface persid = number|string ->won't work (cannot use interface with primitives / unions )

