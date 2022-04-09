
#Skill Assessment - Question 1

import requests
list = ["server", "Date", "x-country-code", "connection", "content-length"]
r = requests.get('http://www.zabandaneshgahi.com/')
for i in range(len(list)):
    try:
        if i in range(len(list)):
            print(r.headers[list[i]])
    except KeyError:
        print (list[i], "is not available")
        pass



#initial code
'''
import requests
r = requests.get('http://www.zabandaneshgahi.com/')
#return response headers
print(r.headers['server'])
print(r.headers['Date'])
# print(r.headers['x-country-code'])
print(r.headers['connection'])
print(r.headers['content-length'])

'''
#initial code 2
'''
import requests
list = ["server", "Date", "x-country-code", "connection", "content-length"]
r = requests.get('http://www.zabandaneshgahi.com/')
for i in range(len(list)):
    print(r.headers[list[i]])
'''

