def unpacked_d(name,age,gender):
    strr=f"I am {name} , I am {age} years old ,I am a {gender}"
    return strr

dictt={
    'name':input(),
    'age':input(),
    'gender':input()
}
print(unpacked_d(**dictt)) 