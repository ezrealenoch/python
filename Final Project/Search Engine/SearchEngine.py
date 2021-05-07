# Enoch Wang
# 5/7/2020
# Final Project: 3 Search Engine
# CSCI 6651
# Professor Gulnora Nurmatova 

from wsgiref.simple_server import make_server
from googleapiclient.discovery import build
import re, time, requests

my_api_key = "AIzaSyAioFz0uycfBtqicoGeWXB7dK8gHc5GMUI" #The API_KEY you acquired
my_cse_id = "30def17c2d9c73cb8" #The search-engine-ID you created

start = 1
size = 10
firstsearch = 0

def add():
    global firstsearch
    firstsearch += 1

def google_search2():    
    link = "https://www.googleapis.com/customsearch/v1?key="+ my_api_key+ "&cx="+ my_cse_id +"&q=*"+"&alt=json"+"&start="+ str(start)+"&num="+ str(10)
    response = requests.get(link)
    if firstsearch == 0:
            print("Search Time   : " + str(response.json()['searchInformation']['searchTime']))
            print("Total Results : " + str(response.json()['searchInformation']['totalResults']))
            add()
    links = response.json()['items']
    return links


def execution_time(r):
    def inner():
        start = time.time()
        s = r()
        end = time.time()
        total = end - start
        return  {"(":total, "seconds)":s}
    return 

def hello_world_app(environ, start_response):
	#print("ENVIRON:", environ)
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	if(len(environ['QUERY_STRING'])>1):
		message += "<br> Your data has been recieved:"
		for param in environ['QUERY_STRING'].split("&"):
			message += "<br>"+param
            
	message += "<h1>Search Engine</h1>"                           
	message += "<form><br>Animal:<input type=text name='Search'>"
	message += "<br><br><input type='submit' name='Search' ></form>"
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")


httpd.serve_forever()
