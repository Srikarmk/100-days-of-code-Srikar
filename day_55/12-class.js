class Animal{
    has_fur=false
    has_scales=true
    constructor(){
        console.log("Animal is TIGER")
    }
    eat(){
        console.log("Animal eats")
    }
    sleep(){
        console.log("Animal sleeps")
    }
}


const animal= new Animal()
animal.eat()
animal.sleep()