#1. Use GET request to get data from a server
#Download a file using HTTP request
import os
print(os.getcwd())  #answer: shows the directly 

#Write the commands to download the txt file in the given link.
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
r = requests.get(URL)
#print(r.headers)
path = os.path.join(os.getcwd(), 'example1.txt')  #os.getcwd() means in the same directory
with open(path, 'wb') as f:
    f.write(r.content)

#2. Use GET request to send data to a server in the header in URL
#Get Request with URL Parameters
url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
r.url #answer: 'http://httpbin.org/get?name=Joseph&ID=123'
print("request body:", r.request.body)  #answer: request body: None
print(r.status_code)   #answer: 200
print(r.text)  
#answer:
# {
#   "args": {
#     "ID": "123", 
#     "name": "Joseph"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate, br", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.29.0", 
#     "X-Amzn-Trace-Id": "Root=1-66d691f2-5ab618875a48c85708d8913f"
#   }, 
#   "origin": "169.63.179.135", 
#   "url": "http://httpbin.org/get?name=Joseph&ID=123"
# }

r.headers['Content-Type']  #answer:'application/json'
#As the content 'Content-Type' is in the JSON format we can use the method json(), it returns a Python dict:
r.json()
#answer
# {'args': {'ID': '123', 'name': 'Joseph'},
#  'headers': {'Accept': '*/*',
#   'Accept-Encoding': 'gzip, deflate, br',
#   'Host': 'httpbin.org',
#   'User-Agent': 'python-requests/2.29.0',
#   'X-Amzn-Trace-Id': 'Root=1-66d691f2-5ab618875a48c85708d8913f'},
#  'origin': '169.63.179.135',
#  'url': 'http://httpbin.org/get?name=Joseph&ID=123'}


#The key args has the name and values:
r.json()['args']  #answer: {'ID': '123', 'name': 'Joseph'}


#3. Use POST request to send data to the server
#Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST:
url_post='http://httpbin.org/post'
#To make a POST request we use the post() function, the variable payload is passed to the parameter  data :
r_post=requests.post(url_post,data=payload)
#compare POST and GET requests output
print("POST request URL:",r_post.url )   #answer:OST request URL: http://httpbin.org/post
print("GET request URL:",r.url)         #answer: GET request URL: http://httpbin.org/get?name=Joseph&ID=123

print("POST request body:",r_post.request.body)  #answer:POST request body: name=Joseph&ID=123
print("GET request body:",r.request.body)   #answer: GET request body: None

#we can view the form:
r_post.json()['form']  #answer: {'ID': '123', 'name': 'Joseph'}

