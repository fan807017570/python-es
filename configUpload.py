#!/usr/bin/python
from xml.dom.minidom import parse 
import xml.dom.minidom
DOMTree= xml.dom.minidom.perse("movies.xml")
collection =DOMTree.documentElement
if collection.hasAttribute("shelf"):
	print("root element :%s " % collection.getAttribute("shelf")
movies = collection.getElemetnsByTagName("movie")
for movie in movies: 
	print "********movie*********"
	if(movie.hasAttribute("title");
		print "title :%s " % moviw.getAttribute("title")
	type=movie.getElementsByTagName('type')[0]
	print "type:%s " % type.childNodes[0].data
	format =movie.getElementByTagName('format')
	print "format:%s " %  format.childNodes[0].data
	rating=movie.getElementsByTagName('rating')[0]
	print "rating:%s " %  rating.childNodes[0].data
	description=movie.getElementsByTagName('description')[0]
	print "description:%s " %  rating.childNodes[0].data
