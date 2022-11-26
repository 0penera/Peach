import requests

# httpbin.org  request test website

#----------------------------------------------------------------
'''checking status and headers, etc'''
# r = requests.get('https://xkcd.com')

# print(dir(r))
# print(help(r))
# print(r.status_code)
# print(r.ok)
# print(r.headers)
# print(r.content)
# print(r.text)

#---------------------------------------------------------------
'''download images'''
# r = requests.get('https://imgs.xkcd.com/comics/paper_title.png')

# with open('C:\\Users\\bokseon hwang\\Documents\\gitsinbook\\Peach\\comic.png', 'wb') as f:
#     f.write(r.content)


#---------------------------------------------------------------
'''request.get method with parameters'''
# payload = {'page': 2, 'COUNT': 25}
# r = requests.get('https://httpbin.org/get', params=payload)

# print(r.text)
# print(r.url)

#-----------------------------------------------------------------
'''request.post'''
# payload = {'username': 'corey', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)

# r_dict = r.json()

# print(r_dict['form'])

#------------------------------------------------------------------
'''request.get  passing auth'''

# r = requests.get('http://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
# print(r.text)


#-------------------------------------------------------------------
'''request.get  timeout method (if timeout then stop requesting/ shoud add 'timeout' every request'''

r = requests.get('http://httpbin.org/delay/3', auth=('corey', 'testing'), timeout=2)
print(r)