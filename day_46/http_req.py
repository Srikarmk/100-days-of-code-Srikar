# import requests

# req=requests.get('https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures#object-oriented-programming')

# print(req.status_code)

import requests
import time 

while True:
    req=requests.get('https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures#object-oriented-programming')
    if req.status_code!=200:
        print('error')
    else:
        print('success')
    time.sleep(2)

    #http status codes 