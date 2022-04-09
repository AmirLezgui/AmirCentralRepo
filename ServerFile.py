
#final code

import requests
list = ['Strict-Transport-Security', 'preload', 'X-Frame-Options', 'X-XSS-Protection', 'Public-Key-Pins', 'Expect-CT', 'X-Content-Type-Options', 'Referrer-Policy', 'Cache-Control', 'Clear-Site-Data', 'Feature-Policy']


def main():

    ServerFile = open('ServerList.txt', 'r')

    for line in ServerFile:
        r = requests.get(line)
        h = r.headers
        for i in range(len(list)):

            try:
                if list[i] in h:
                    print(list[i], "exists in website", line, "and makes it secure")
            except KeyError:
                print(list[i], "is not available")

    ServerFile.close()


main()

'''
#inital Code

import requests
list = ['Strict-Transport-Security', 'preload', 'X-Frame-Options', 'X-XSS-Protection', 'Public-Key-Pins', 'Expect-CT', 'X-Content-Type-Options', 'Sec-Fetch-Site', 'Referrer-Policy', 'Cache-Control', 'Clear-Site-Data', 'Feature-Policy']

def main():
    ServerFile = open('ServerList.txt', 'r')
    for line in ServerFile:
        r = requests.get(line)
        for i in range(len(list)):
            if i == True:
                print(r.headers[list[i]], "exists in website", line, "and makes it secure")
            else:
                print(r.headers[list[i]], "is not available")

    ServerFile.close()

main()

'''

