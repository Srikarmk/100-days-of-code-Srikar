#SHA - Secure hash algorithm -used to generate a secure value 
'''https://www.pcmag.com/encyclopedia/term/sha#:~:text=(Secure%20Hash%20Algorithm)%20A%20family,Standards%20%26%20Technology%20(NIST).'''
from hashlib import sha256 

text="SRA"
print(sha256(text.encode('ascii')).hexdigest())