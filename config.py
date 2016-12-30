
from xml.dom.minidom import parse
import xml.dom.minidom
import httplib,urllib

DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print "Root element : %s" % collection.getAttribute("shelf")
movies = collection.getElementsByTagName("movie")
for movie in movies:
   print "*****Movie*****"
   if movie.hasAttribute("title"):
      print "Title: %s" % movie.getAttribute("title")
   type = movie.getElementsByTagName('type')[0]
   print "Type: %s" % type.childNodes[0].data
   format = movie.getElementsByTagName('format')[0]
   print "Format: %s" % format.childNodes[0].data
   rating = movie.getElementsByTagName('rating')[0]
   print "Rating: %s" % rating.childNodes[0].data
   description = movie.getElementsByTagName('description')[0]
   print "Description: %s" % description.childNodes[0].data
conn = httplib.HTTPConnection("www.baidu.com")
conn.request("GET","/")
res=conn.getresponse()
print res.status, res.reason
data=res.read()
print(len(data))

def postData(json ,url,port)
	try:
		urllib.urlencode(json)
		headers = {"Content-type":
			"application/x-wwww-urlencoded",
			"Accept":"text/plain" }
		httpClient=httplib.HTTPConnection(url,port,timeout=30)
		httpClient.request("POST",url,json,headers)
		response =httpClient.getresponse()
		print response.status
		print response.reason
		print response.read()
		print response.getheaders()
	except Exception e:
		print e
	finally:
		if httpClient:
			httpClient.close()
def xmlParse(file)
	DOMTree = xml.dom.minidom.parse(file)
	collection = DOMTree.documentElement
	row=collection.getElementsByTagName("DATA");
	


	
