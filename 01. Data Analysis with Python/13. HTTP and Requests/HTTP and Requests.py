#HTTP and Requests

import requests
import os 
from PIL import Image
from IPython.display import IFrame

# get the data from ibm website:
url='https://www.ibm.com/'
r=requests.get(url)
r.status_code  #answer: 200

print(r.request.headers)  
#answer:{'User-Agent': 'python-requests/2.29.0', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive', 'Cookie': '_abck=6BE330DC82120BD2C3969A72DDBA93AD~-1~YAAQr2QwF2g+qqORAQAAF4fstQxpkUZyltzhXd2NvUocNq+28Z5h48qhkluoBlZ9xdyrJfpRoAnJxSVDNnfeV5fB0qWxY/RR98qlTUnm/ivF3hR74LRUmxlkVVCjZXVuRPIOIxOFWWj/Y3RnxyFos1fKxGHjjHhPVdD3q2MmzVL845R/rXO6Yt4M6UqQOdYJ7MwUOWjcTYB2IQBhxs6XHTQGkuC0qQnZhWmCM1zKn0BgmanleYYcRK4XwsmNFjWOtVELxWtAMoWg/DtvzLmclhmbmeGoLCJpzIx3Tco87UWfrPYe+WhEesY82+F482Y+By9e3UWHE36pUS/+UYRKArDdCjUW4fZeBgL7mLBTIZ/saYF2xHU=~-1~-1~-1; bm_sz=DA5452B830017A20373557F67002EB9A~YAAQr2QwF2k+qqORAQAAF4fstRiJKz1bphDTIhKvyzFT4y1dNYUvlutNbpBYX8jmwEx/v5R8jQYE0mKZB6X/Goxvp+VLTGg2fNb9cskjvFJYYvoJrO+v72/DYaJ5nCmljhMVK1/Phheqs2yArc4l9IO6wtc+KBuf4aQe1aM3yg/HImFDfhRicP4ev9cTV8oYs2TO+vV88IWm0Wbok6WSEs0AW2Rcqyx5t92ppVggsMNvnZqg6nUzuLZhJLx/Sg6xCgNImen6zJFR1ZacQ1e57/MfhYCRsBZyPHK64X+Ch4Drb8srPt6q4kv6ESf1LGsOBWAmOrOY468o0+R4tCYOZpbhpYw2icwjBXcZ~4534324~3158582'}

print("request body:", r.request.body)  #request body: None

#way2:You can view the HTTP response header using the attribute headers. This returns a python dictionary of HTTP response headers.
header=r.headers
print(r.headers)
#answer:
#{'Content-Security-Policy': 'upgrade-insecure-requests', 'x-frame-options': 'SAMEORIGIN', 'Last-Modified': 'Tue, 03 Sep 2024 02:20:16 GMT', 'ETag': '"16a03-6212db2bd7722-gzip"', 'Accept-Ranges': 'bytes', 'Content-Type': 'text/html;charset=utf-8', 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'max-age=600', 'Expires': 'Tue, 03 Sep 2024 03:37:42 GMT', 'X-Akamai-Transformed': '9 13362 0 pmb=mTOE,2', 'Content-Encoding': 'gzip', 'Date': 'Tue, 03 Sep 2024 03:27:42 GMT', 'Content-Length': '13562', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Strict-Transport-Security': 'max-age=31536000'}

#We can obtain the date the request was sent using the key Date.
header['date']   #answer: 'Tue, 03 Sep 2024 03:27:42 GMT'
#Content-Type indicates the type of data:
header['Content-Type']   #answer: 'text/html;charset=utf-8'
#check the encoding:
r.encoding  #answer:'utf-8'
#we can use the attribute text to display the HTML in the body. We can review the first 100 characters:
r.text[0:100]  #answer:'\n<!DOCTYPE HTML>\n<html lang="en">\n<head>\r\n    \r\n    \r\n    \r\n    \r\n    \r\n    \r\n    \r\n    \r\n    <meta '


#You can load other types of data for non-text requests, like images. Consider the URL of the following image:
# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r.headers)  
#answer:{'Date': 'Tue, 03 Sep 2024 04:14:35 GMT', 'X-Clv-Request-Id': 'c115e287-b06d-43f2-a28b-d4c0549d6d58', 'Server': 'Cleversafe', 'X-Clv-S3-Version': '2.5', 'Accept-Ranges': 'bytes', 'x-amz-request-id': 'c115e287-b06d-43f2-a28b-d4c0549d6d58', 'ETag': '"8bb44578fff8fdcc3d2972be9ece0164"', 'Content-Type': 'image/png', 'Last-Modified': 'Wed, 16 Nov 2022 03:32:41 GMT', 'Content-Length': '78776'}

#We can see the 'Content-Type'
r.headers['Content-Type']  #answer: 'image/png'
path=os.path.join(os.getcwd(),'image.png')  
with open(path,'wb') as f:
    f.write(r.content)
Image.open(path)  #here we can see the image


