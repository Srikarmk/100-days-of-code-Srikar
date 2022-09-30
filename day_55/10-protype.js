function person(fname,lname){
    this.fname=fname
    this.lname=lname
}

const person1 = new person('Sheldon','Cooper')
const person2= new person('Leonard','Hofstader')
person.prototype.getFullName = function (){
    return `${this.fname} ${this.lname}`
}

console.log(person2.getFullName())

