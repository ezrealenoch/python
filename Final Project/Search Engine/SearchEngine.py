# Enoch Wang
# 5/7/2020
# Final Project: 3 Search Engine
# CSCI 6651
# Professor Gulnora Nurmatova 

from wsgiref.simple_server import make_server
import re, os, json

class my_dictonary(dict):
    
    def __init__(self):
        self = dict()
        
    def add(self, key, value):
        self[key] = value
    
    def has_key(self, key):
        if key in self.keys():
            return True
        else:
            return False

linkDic = my_dictonary()
titleDic = my_dictonary()
keywordDic = my_dictonary()

def get_form_vals(post_str):
    form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    return form_vals

def load():
    print("Current Directory:",os.getcwd())
    directory = "Indexer"
    os.chdir(os.getcwd())    
    os.chdir(directory)    
    count = 1
    with open("links.txt", "r") as link_file:
        while True:
            link = link_file.readline()
            if not link:
                break
            linkDic.add(count, link)
            count += 1
            
    count = 1
    with open("keywords.txt", "r") as link_file:
        while True:
            link = link_file.readline()
            if not link:
                break
            keywordDic.add(count, link)
            count += 1
        
    count = 1
    with open("titles.txt", "r") as link_file:
        while True:
            link = link_file.readline()
            if not link:
                break
            titleDic.add(count, link)
            count += 1       

def searchbar(environ, start_response):
    foundlink = " "
    foundkeyword = " "
    foundtitle = " "
    message = ""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    message += "<h1>New Haven Search Bar</h1>"
    message += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">'
    message += '<br><br><form class="example" action="action_page.php"><input type="text" placeholder="Search.." name="search"><button type="submit"><i class="fa fa-search"></i></button></form>'
    if(len(environ['QUERY_STRING']) > 1):
        message += "<br> Search Recieved"
        for param in environ['QUERY_STRING'].split("&"):
            found = []
            paramlower = param[7:]
            paramlower = paramlower.lower()
            for key, keyword in keywordDic.items():
                lower = keyword.lower()
                if lower.find(paramlower) != -1:
                    found.append(key)
                    
            for key, title in titleDic.items():
                lower = title.lower()
                if lower.find(paramlower) != -1:
                    found.append(key)        
                    
            res = []
            for i in found:
                if i not in res:
                    res.append(i)
                    
                    
            print(res)
            for i in range(len(res)):
                foundlink = " "
                foundkeyword = " "
                foundtitle = " "
                if linkDic.has_key(res[i]):
                    foundlink = linkDic.get(res[i])
                if titleDic.has_key(res[i]):
                    foundtitle = titleDic.get(res[i]) 
                if keywordDic.has_key(res[i]):
                    foundkeyword = keywordDic.get(res[i])
                
                message += '<br><br><p style="font-size:30px;">' + foundtitle + '</p>'
                message += '<a href="url">' + foundlink +'</a>'
                message += '<p>' + foundkeyword + '</p>'    
    
    
    return[bytes(message,'utf-8')]

load()
httpd = make_server('', 8000, searchbar)
print("Serving on port 8000...")

httpd.serve_forever()