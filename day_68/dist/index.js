"use strict";
/*
Commands:

tsc.cmd -> to compile
tsc.cmd --watch -> to keep watch on compilation
tsc.cmd --init -> initializes a config file
*/
//Basic types
let id = 5;
let myName = "Srikar";
let over18 = true;
let something = 'cool';
let nums = [1, 2, 3, 4];
let strs = [1, true, 'Srikar'];
//Tuples
let tup = [1, 'Sri', true];
//Tuple Arrays 
let tuparr;
tuparr = [
    [1, 'Srikar'],
    [2, 'Suraj'],
    [3, 'Koushik']
];
//Unions 
let pid;
pid = '22';
//Enums
var directions;
(function (directions) {
    directions[directions["Up"] = 3] = "Up";
    directions[directions["Down"] = 4] = "Down";
    directions[directions["Left"] = 5] = "Left";
    directions[directions["Right"] = 6] = "Right";
})(directions || (directions = {}));
console.log(directions.Down);
let user = {
    id: 1,
    name: 'Srikar'
};
//Type assertion - Similar to typecasting 
let cid = true;
let customerId = cid;
let custId = cid;
//Functions 
function add(x, y) {
    return x + y;
}
console.log(add(2, 3));
//Void 
function message(message) {
    console.log(message);
}
message("Srikar");
let fuser = {
    uid: 1,
    fname: 'Srikar'
};
//Interfaces vs type assertion 
// type personid=number|string
// const p1:personid=1
// interface persid = number|string ->won't work (cannot use interface with primitives / unions )
