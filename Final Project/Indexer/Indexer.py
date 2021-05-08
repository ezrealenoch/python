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
                        link = domain + link 
                        if link not in linkDic.values():
                            # print("HREF LINK : " + link)
                            getcontent(link, domain)
                
        except URLError as e:
            add_bad()
            print("Error Opening : " + link)
            badLinkDic.add(baditerator, link)
        
        except:
            print("Probably a suspecious link")
        

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
    
    if(int(userinput) == 1):
        userurl = input("Enter URL: ")
        userdomain = input("Enter Domain: ")
        
        getcontent(userurl, userdomain)
        print(linkDic)
        print(keywordDic)
        print(titleDic)
        
        print("Current Directory:",os.getcwd())
        directory = "Indexer"
        if (not os.path.exists(directory)):
            os.mkdir(directory)
            print("Created ", directory)
        os.chdir(os.getcwd())    
        os.chdir(directory)    
        
        out = open("links.txt", "w")
        for i in linkDic:
            out.write(linkDic.get(i))
            out.write("\n")    
        out.close()
        
        with io.open("keywords.txt", "w", encoding="utf-8") as out:
            for i in keywordDic:
                out.write(keywordDic.get(i))
                out.write("\n")
        out.close()
        
        with io.open("titles.txt", "w", encoding="utf-8") as out:
            for i in titleDic:
                out.write(titleDic.get(i))
                out.write("\n")
        out.close()
        
    elif(int(userinput) == 2):
        directory = "Indexer"
        print("Current Directory:",os.getcwd())
        os.chdir(os.getcwd())
        if (not os.path.exists(directory)):
            print("No Index to Load")
        else:
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
     
    elif(int(userinput) == 3):
        if keywordDic:
            userinput = input("Search Keyword: ")
            found = []
            for key, keyword in keywordDic.items():
                if keyword.find(userinput) != -1:
                    found.append(key)
                    
            for i in range(len(found)):
                foundlink = " "
                foundkeyword = " "
                foundtitle = " "
                if linkDic.has_key(found[i]):
                    foundlink = linkDic.get(found[i])
                if titleDic.has_key(found[i]):
                    foundtitle = titleDic.get(found[i]) 
                if keywordDic.has_key(found[i]):
                    foundkeyword = keywordDic.get(found[i])
                tempstring = '{ "link": "' + foundlink + '", "title": "' + foundtitle + '", "keywords": "' + foundkeyword + '"}'
                newjson = json.dumps(tempstring)
                print(newjson)
            print("Results Found: " + str(len(found)))
        else:
            print("Empty Index")
    elif(int(userinput) == 4):
        if titleDic:
            userinput = input("Search Title: ")
            found = []
            for key, title in titleDic.items():
                if title.find(userinput) != -1:
                    found.append(key)
            
            for i in range(len(found)):
                foundlink = " "
                foundkeyword = " "
                foundtitle = " "
                if linkDic.has_key(found[i]):
                    foundlink = linkDic.get(found[i])
                if titleDic.has_key(found[i]):
                    foundtitle = titleDic.get(found[i]) 
                if keywordDic.has_key(found[i]):
                    foundkeyword = keywordDic.get(found[i])
                tempstring = '{ "link": "' + foundlink + '", "title": "' + foundtitle + '", "keywords": "' + foundkeyword + '"}'
                newjson = json.dumps(tempstring)    
                print(newjson)
            print("Results Found: " + str(len(found)))
                
    elif(int(userinput) == 5):
        sys.exit()
    else:
        print("invalid selection")
    
        
       