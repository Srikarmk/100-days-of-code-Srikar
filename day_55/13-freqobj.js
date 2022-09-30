let freq={}
const name="Srikar"

for (const char of name){
    if (char in freq){
        freq[char]+=1
    }
    else{
        freq[char]=1
    }
}

console.log(freq)