# Enoch Wang
# 2/19/2020
# Homework 4 Program 4
# CSCI 6651
# Professor Gulnora Nurmatova 

import uuid

urllist = []

def shorten_url(url):
    urllist.append(url)
    id = uuid.uuid3(uuid.NAMESPACE_URL, url)
    mystring = str(id.bytes_le.hex())
    return ("https://enoch.ly/" + mystring[-4:])

def get_original_url(url):
    mystring = url[-4:]
    for i in range(0,len(urllist)):
        id = uuid.uuid3(uuid.NAMESPACE_URL,urllist[i])
        origin = str(id.bytes_le.hex())
        if mystring == origin[-4:]:
            return urllist[i]
    print("HTTP 404")
    
        
    
if __name__ == '__main__': 
    print(shorten_url("https://docs.python.org/3/library/uuid.html"))
    print(get_original_url("https://enoch.ly/847c"))
    
# =============================================================================
  # Method 1: UUID 
  # This was the method implemented above, UUID very basically utilizes 
  # the various functionalities already established in the UUID library.
  # By using UUID, we can obtain various elements from a given url or string,
  # including a built-in URL method. From here we are given any number of ways
  # that we might want to produce our "hash". 
  
  # In the version given above, a global list is used to keep track of all urls
  # the user has submitted, simulating a webserver database. The url is then
  # plugged into the uuid3 method which produces a MD5 hash out of the url string.
  # The hash is then converted to hex/string and concatenated by its last 4 char/bytes.
  # We can choose the likeliness for a collusion by choosing how many bytes we wish to
  # concatenate from the hash. The chances for a collision using 4 hex bytes is 
  # denoted by 16 to the nth power where n is the number of bytes used (65536) uniques
  # The original url can be generated by reverseing the process above and recalculating
  # the MD5 hashes from the urllist, this unforunately is the crux of using UUID3
  # as hashes are one way processes and the only way to check is to recalculate.
  
  
  # Method 2: Timestamp
  # Theortically a url shortner could be created by utilizing the pseudo random 
  # element of time seeding. This random time has the benefit of garenteeing 
  # non-collision depending on where it is concatenated, for example if we were
  # to take the values indicating hours, minutes, and seconds, we could garentee
  # that in a 24 hour period no collision would occur given that inputs are done 
  # with at least a second between them. Effectively this would create 86400 uniques.
  # Due to the incremental nature of timestamps and a user's likely hood to only
  # use a shortened link for a brief period of time, this method is extremely effective.
  
  
  # Method 3: MD5
  # The MD5 hash method was used in our UUID implementation and shares all the same
  # Pros and Cons as mentioned as before; however, it is important to note that UUID
  # consists within it a variety of functions including timestamp.
  
  
  # Method 4: maps (iterator)
  # Similar to the hash table, a python map could use a elements iterator to
  # seed a new link. For example, if we were to if https://docs.python.org/3/library/uuid.html
  # is added to the map as the first element, we could just make the link https://enoch.ly/0
  # and pull the url element from position 0 of the map. We could use literally any container 
  # to implement this method. The caviate of simply using the iterator to seed a url is 
  # the production of urls in different lengths, this may ultimately lead to url's longer
  # than the original. Perodic list purges may be required. 
# =============================================================================

