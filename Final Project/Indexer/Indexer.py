# Enoch Wang
# 5/7/2020
# Final Project: 2 Crawler Indexer Search
# CSCI 6651
# Professor Gulnora Nurmatova 

import requests
import urllib.request
from urllib.error import  URLError
import re
import os
import json
import sys
import io

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
  
     

start = 1
size = 10
firstsearch = 0

iterator = 0
baditerator = 0

seedList = []

linkDic = my_dictonary()
titleDic = my_dictonary()
keywordDic = my_dictonary()
badLinkDic = my_dictonary()


def getcontent(link, domain):
    if link not in badLinkDic.values():
        try:
            page = urllib.request.urlopen(link)
            code = page.getcode()
            if code == 200:
                add()
                linkDic.add(iterator, link)
                content = page.read()
                content_string = content.decode("utf-8")
                regextitle = re.compile('<title>(?P<title>(.*))</title>')
                regexkeywords = re.compile('<meta name="Keywords" content="(?P<keywords>(.*))" />')
                regexlink = re.compile(domain + "[/\w+]*")
                
                result = regextitle.search(content_string, re.IGNORECASE)
                if result:
                    title = result.group("title")
                    titleDic.add(iterator, title)
                    
                result = regexkeywords.search(content_string, re.IGNORECASE)
                if result:
                    keyword = result.group("keywords")
                    keywordDic.add(iterator, keyword)
                    print(keyword)
                    
                for link in re.findall(regexlink, content_string):
                    if link not in linkDic.values():
                        getcontent(link, domain)
                
                for link in re.findall(r'href=[\'"]?([^\'" >]+)', content_string):
                     if (False == bool(re.search(":", link))) and (False == bool(re.search(".pdf", link)) and (False == bool(re.search("title-ix.", link)))):
                        if link[0].isalpha() or link[0] == '/':
                            if link[-4:] != ".css" and link[-4:] != "docx" and (link.find("_resources") == -1):
                                link = domain + link 
                                if link not in linkDic.values():
                                    print("HREF LINK : " + link)
                                    getcontent(link, domain)
                    
        except URLError as e:
            add_bad()
            print("Error Opening : " + link)
            badLinkDic.add(baditerator, link)
        
        except:
            print("Probably a suspecious link")
        
def reset():
    global iterator
    iterator = 0

def add():
    global iterator
    iterator += 1

def add_bad():
    global baditerator
    baditerator += 1

while True:
    print("1) Crawl URL")
    print("2) Load Index")
    print("3) Keyword Search")
    print("4) Title Search")
    print("5) Exit")
    userinput = input("User Selection : ")
    userint = 0
    if userinput.isdigit():
        userint = int(userinput)

    if(userint == 1):
        keywordDic.clear()
        titleDic.clear()
        linkDic.clear()
        reset()
        userurl = input("Enter URL: ")
        userdomain = input("Enter Domain: ")
        
        getcontent(userurl, userdomain)
        print(linkDic)
        print(keywordDic)
        print(titleDic)
        os.chdir(sys.path[0])
        print(os.chdir(sys.path[0]))
        directory = "Indexed"
        if (not os.path.exists(directory)):
            os.mkdir(directory)
            print("Created ", directory)   
        os.chdir(directory)    
        
        out = open("links.txt", "w", encoding="utf-8")
        for i in linkDic:
            out.write(linkDic.get(i))
            out.write("\n")    
        out.close()
        
        out = open("keywords.txt", "w", encoding="utf-8")
        for i in keywordDic:
            out.write(keywordDic.get(i))
            out.write("\n")
        out.close()
        
        out = open("titles.txt", "w", encoding="utf-8")
        for i in titleDic:
            out.write(titleDic.get(i))
            out.write("\n")
        out.close()
        
    elif(userint == 2):
        directory = "Indexed"
        os.chdir(sys.path[0])
        if (not os.path.exists(directory)):
            print("No Index to Load")
        else:
            os.chdir(directory)
            
            count = 1
            with open("links.txt", "r", encoding="utf-8") as link_file:
                while True:
                    link = link_file.readline()
                    if not link:
                        break
                    linkDic.add(count, link)
                    count += 1
            
            count = 1
            with open("keywords.txt", "r", encoding="utf-8") as link_file:
                while True:
                    link = link_file.readline()
                    if not link:
                        break
                    keywordDic.add(count, link)
                    count += 1
                    
            count = 1
            with open("titles.txt", "r", encoding="utf8") as link_file:
                while True:
                    link =  link_file.readline()
                    if not link:
                        break
                    titleDic.add(count, link)
                    count += 1         
     
    elif(userint == 3):
        if keywordDic:
            userinput = input("Search Keyword: ")
            found = []
            userinput = userinput.lower()
            for key, keyword in keywordDic.items():
                newkeyword = keyword.lower()
                if newkeyword.find(userinput) != -1:
                    found.append(key)
            
            res = []
            for i in found:
                if i not in res:
                    res.append(i)
            
            for i in range(len(found)):
                foundlink = " "
                foundkeyword = " "
                foundtitle = " "
                if linkDic.has_key(res[i]):
                    foundlink = linkDic.get(res[i])
                if titleDic.has_key(res[i]):
                    foundtitle = titleDic.get(res[i]) 
                if keywordDic.has_key(res[i]):
                    foundkeyword = keywordDic.get(res[i])
                tempstring = '{ "link": "' + foundlink + '", "title": "' + foundtitle + '", "keywords": "' + foundkeyword + '"}'
                newjson = json.dumps(tempstring)
                print(newjson)
            print("Results Found: " + str(len(res)))
        else:
            print("Empty Index")
    elif(userint == 4):
        if titleDic:
            userinput = input("Search Title: ")
            found = []
            userinput = userinput.lower()
            for key, title in titleDic.items():
                newtitle = title.lower()
                if newtitle.find(userinput) != -1:
                    found.append(key)
                    
            res = []
            for i in found:
                if i not in res:
                    res.append(i)   
            
            for i in range(len(found)):
                foundlink = " "
                foundkeyword = " "
                foundtitle = " "
                if linkDic.has_key(res[i]):
                    foundlink = linkDic.get(res[i])
                if titleDic.has_key(res[i]):
                    foundtitle = titleDic.get(res[i]) 
                if keywordDic.has_key(res[i]):
                    foundkeyword = keywordDic.get(res[i])
                tempstring = '{ "link": "' + foundlink + '", "title": "' + foundtitle + '", "keywords": "' + foundkeyword + '"}'
                newjson = json.dumps(tempstring)    
                print(newjson)
            print("Results Found: " + str(len(res)))
                
    elif(userint == 5):
        sys.exit()
    else:
        print("invalid selection")
    
        
       