SpaceInvaders README
Enoch Wang
5/6/2020
Final Project: 1 Indexer, Crawler, File Traverser and Search
CSCI 6651
Professor Gulnora Nurmatova 

INSTRUCTIONS:

	1) Install modules: "pip install requests"
	
	2) Run with "python indexer.py"
	
	3) Make selection with menu. 5 options: Crawl URL, Load, Keyword Search, Title Search and Exit
	
	Crawl URL: Requests user to input a root URL to crawl and requests a domain 
	The crawl search will recusively search all URL's contained within the root URL and any href links. 
	The data crawled includes titles, keywords, and url's which are added to a individual dictonaries
	
	Load: Navigates to a dictory containing index information and reads in the files necessary to load dictonaries
	
	Keyword Search: Requests a keyword and searches keyword dictonary for indidices containing the keyword 
	then loads up all stored information relating to the URL and returns a JSON!
	
	Title Search: Not all indexed pages have keywords. Requests a title from user to input and searches for the title 
	within the title dictonary. The indidices are recorded and used to return all information related to the URL and returns a JSON!
	
	
	
Extra Credit 1: Ways to crawl content 
	Originally, 10 different API's were explored to obtain all the URL's which can be returned from the newhaven.edu/search website. 
	Each API returned different information when the URL's were parsed but none contained a recrusive method capable of pulling all URL'search
	found in source code and repeats a search. Most API's would enable google search results and provided similar results with the input
	site:newhaven.edu/ which provided the JSON's obtained from the URL's the API was able to indicate. MOST API's only returned a limited 
	number of results (less than 100) and required a subscription service to obtain more than 100 queries. The Google API is limited to 10,000 queries.
	The benefits of returning a JSON enabled very distinct requests for URL content, references, objects, etc, but not all links stored within source.
	As a result, it was determined the best way to obtain the most URL's for the most comprehensive index was to build a crawler from scratch 
	and manually parse in links founds with regex and a link that could be built off the root domain by adding the crawled data from href.
	Href URL's were a bit troublesome as URL links require a maximum length, and no special symbols within the URL's.
	
	The best results mirrored came from the Custom Search API requriring an API key and service management. The results mirrored google's search exactly
	but only enabled 10-12 results per page and only 31 pages. The API returned crawled JSON objects which could be specified from content, description, languages, 
	page crawled, etc. MOST of the API's and alternative crawlers used would get blocked within 5 executions as the server viewed repeat requests for the same query as 
	a form of DoS attack.
	
	API's explored: elasticsearch, Custom Search API by google, beautifulsoup4, google-search-results, googleScrapy, SerpApi, urlparse, colorama, and many more
	

Extra Credit 2: File Traverser Optional  
	Once all the information has been crawled and indexed into dictonaries, all the dictonaries are read into a txt. file stored within a created directory
	There is an extra option called load which navigates to the indexer directory from the working directory and loads all the information from the 
	txt file respective to the dictonary. Multiple crawl iterations require loading the dictonaries from option 2 to refresh the indexed information.
	The loaded dictonaries can then be searched and created into a JSON.
	