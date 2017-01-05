
from xml.dom.minidom import parse
import xml.dom.minidom
import httplib,urllib
import json

def xmlParse(file):
	DOMTree = xml.dom.minidom.parse(file)
	root = DOMTree.documentElement
	rows=root.getElementsByTagName("ROW")
	for row in rows:
		groupId=row.getElementsByTagName("GROUP_ID")[0].childNodes[0].data
		tagName=row.getElementsByTagName("TAG_NAME")[0].childNodes[0].data
		appId=row.getElementsByTagName("APP_ID")[0].childNodes[0].data
		serviceId=row.getElementsByTagName("SERVICE_ID")[0].childNodes[0].data
		reqClass=row.getElementsByTagName("REQUEST_CLASS")[0].childNodes[0].data
		reqMethod =row.getElementsByTagName("REQUEST_METHOD")[0].childNodes[0].data
		respClass=row.getElementsByTagName("RESPONSE_CLASS")[0].childNodes[0].data
		respMethod=row.getElementsByTagName("RESPONSE_METHOD")[0].childNodes[0].data
		objstr=json.dumps({"groupId":groupId,"tagName":tagName,"appId":appId,"serviceId":serviceId,"reqClass":reqClass,"reqMethod":reqMethod,"respClass":respClass,"respMethod":respMethod})
		print objstr
		postData(objstr,localhost,9200)
		obj=json.loads(objstr)
		print obj["tagName"]		
def postData(json,url,port):
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
	except Exception:
		print "error"
	finally:
		if httpClient:
			httpClient.close()
if __name__ == '__main__':
	xmlParse("data_total.xml")		

	
