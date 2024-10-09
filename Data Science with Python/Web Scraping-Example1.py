#Web Scraping

#first install the necessary packages
#!mamba install bs4==4.10.0 -y
#!pip install lxml==4.6.4
#!mamba install html5lib==1.1 -y
# !pip install requests==2.26.0

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#Consider the following HTML:
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
#We can use the method prettify() to display the HTML in the nested structure:
print(soup.prettify())
#find title
tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))  #find the type of tag_object
#find h3 (heading3)
tag_object=soup.h3

#Children, Parents, and Siblings
tag_child =tag_object.b  #find the child of hte tag
#parent
parent_tag=tag_child.parent
#sibiling
sibling_1=tag_object.next_sibling
sibling_2=sibling_1.next_sibling

#HTML Attributes
tag_child['id']   #the tag id="boldest" has an attribute id
tag_child.attrs  #another way to find the attributs is using 'attrs' method
tag_child.get('id')  #another way to find the attributes is to use .get() method

#Navigable String
tag_string=tag_child.string  #find string

#Filter (like find, find_all mthod)
table="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

#find_all()
table_rows=table_bs.find_all('tr')
first_row =table_rows[0]
first_row.td  #to obtain a child

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

list_input=table_bs.find_all(name=["tr", "td"])

#Attributes
table_bs.find_all(id="flight")
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
table_bs.find_all(href=True)  #set the hred to True means find the tags which has href











