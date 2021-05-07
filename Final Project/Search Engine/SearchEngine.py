from wsgiref.simple_server import make_server
import re, time

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
