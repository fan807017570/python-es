#!/usr/bin/python 
from elasticsearch import Elasticsearch
es=Elasticsearch(['http://localhost:9200'])
doc={'author':'Kimchy'}
res=es.index(index="test-index",doc_type='tweet',id=1,body=doc)
print (res['created'])
